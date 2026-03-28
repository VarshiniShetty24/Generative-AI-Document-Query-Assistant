"""
FastAPI backend for RAG system (Optional)
Provides REST API endpoints for programmatic access
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import tempfile
import sys
from pathlib import Path
import logging

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from rag_pipeline import RAGPipeline

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="RAG System API",
    description="API for Retrieval-Augmented Generation System",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG pipeline
rag_pipeline = RAGPipeline()


# Request/Response models
class QueryRequest(BaseModel):
    question: str
    use_history: bool = True


class QueryResponse(BaseModel):
    question: str
    answer: str
    documents_found: int


class DocumentResponse(BaseModel):
    filename: str
    status: str
    message: str
    chunks: int


class SystemInfo(BaseModel):
    documents_processed: int
    embedding_model: str
    llm_model: str
    vectorstore_status: str


# API Endpoints

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "RAG System API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/upload", response_model=DocumentResponse)
async def upload_document(file: UploadFile = File(...)):
    """Upload and ingest a document"""
    try:
        # Validate file type
        allowed_extensions = {'.pdf', '.csv', '.txt', '.md', '.docx'}
        file_ext = Path(file.filename).suffix.lower()
        
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"File type {file_ext} not supported. Allowed: {allowed_extensions}"
            )
        
        # Save temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_path = tmp_file.name
        
        # Ingest document
        success, message = rag_pipeline.ingest_document(tmp_path)
        
        if success:
            # Extract number of chunks from message
            parts = message.split("(")
            chunks_text = parts[-1].replace(" chunks)", "") if "(" in message else "0"
            chunks = int(chunks_text.split()[0]) if chunks_text.isdigit() else 0
            
            return DocumentResponse(
                filename=file.filename,
                status="success",
                message=message,
                chunks=chunks
            )
        else:
            raise HTTPException(status_code=400, detail=message)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """Query the RAG system"""
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        if request.use_history:
            answer = rag_pipeline.conversational_query(request.question)
        else:
            answer = rag_pipeline.query(request.question)
        
        # Count documents in chat history
        history = rag_pipeline.get_chat_history()
        docs_found = history[-1]["results_count"] if history else 0
        
        return QueryResponse(
            question=request.question,
            answer=answer,
            documents_found=docs_found
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/documents")
async def get_documents():
    """Get list of processed documents"""
    try:
        docs = rag_pipeline.get_processed_documents()
        return {
            "documents": docs,
            "count": len(docs)
        }
    except Exception as e:
        logger.error(f"Error getting documents: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history")
async def get_history():
    """Get chat history"""
    try:
        history = rag_pipeline.get_chat_history()
        return {
            "history": history,
            "count": len(history)
        }
    except Exception as e:
        logger.error(f"Error getting history: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/history")
async def clear_history():
    """Clear chat history"""
    try:
        rag_pipeline.clear_chat_history()
        return {"status": "success", "message": "Chat history cleared"}
    except Exception as e:
        logger.error(f"Error clearing history: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/system-info", response_model=SystemInfo)
async def system_info():
    """Get system information"""
    try:
        info = rag_pipeline.get_system_info()
        vs_info = info["vectorstore_info"]
        
        return SystemInfo(
            documents_processed=info["documents_processed"],
            embedding_model=info["embedding_model"],
            llm_model=info["llm_model"],
            vectorstore_status=vs_info.get("status", "unknown")
        )
    except Exception as e:
        logger.error(f"Error getting system info: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
