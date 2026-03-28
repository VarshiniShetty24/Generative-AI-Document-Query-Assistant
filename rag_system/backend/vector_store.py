import logging
from typing import List, Tuple
from langchain.vectorstores import Chroma, FAISS
from langchain.schema import Document
from config import VECTORSTORE_TYPE, VECTOR_DB_PATH, TOP_K_RESULTS, SIMILARITY_THRESHOLD
from embeddings import EmbeddingManager

logger = logging.getLogger(__name__)


class VectorStoreManager:
    """Manage vector database operations"""
    
    def __init__(self, embedding_manager: EmbeddingManager):
        self.embedding_manager = embedding_manager
        self.vectorstore = None
        self.vectorstore_type = VECTORSTORE_TYPE.lower()
    
    def create_vectorstore(self, chunks: List[str], doc_name: str) -> bool:
        """Create or update vectorstore with document chunks"""
        try:
            # Create document objects with metadata
            docs = [
                Document(page_content=chunk, metadata={"source": doc_name, "chunk_id": i})
                for i, chunk in enumerate(chunks)
            ]
            
            embeddings = self.embedding_manager.get_embeddings_object()
            
            if self.vectorstore_type == "chroma":
                logger.info("Creating Chroma vectorstore...")
                self.vectorstore = Chroma.from_documents(
                    documents=docs,
                    embedding=embeddings,
                    persist_directory=VECTOR_DB_PATH,
                    collection_name="rag_documents"
                )
                self.vectorstore.persist()
            elif self.vectorstore_type == "faiss":
                logger.info("Creating FAISS vectorstore...")
                self.vectorstore = FAISS.from_documents(docs, embeddings)
                self.vectorstore.save_local(VECTOR_DB_PATH)
            else:
                raise ValueError(f"Unsupported vectorstore type: {self.vectorstore_type}")
            
            logger.info(f"Vectorstore created successfully with {len(docs)} documents")
            return True
        except Exception as e:
            logger.error(f"Error creating vectorstore: {e}")
            raise
    
    def load_vectorstore(self) -> bool:
        """Load existing vectorstore"""
        try:
            embeddings = self.embedding_manager.get_embeddings_object()
            
            if self.vectorstore_type == "chroma":
                logger.info("Loading Chroma vectorstore...")
                self.vectorstore = Chroma(
                    persist_directory=VECTOR_DB_PATH,
                    embedding_function=embeddings,
                    collection_name="rag_documents"
                )
            elif self.vectorstore_type == "faiss":
                logger.info("Loading FAISS vectorstore...")
                self.vectorstore = FAISS.load_local(VECTOR_DB_PATH, embeddings)
            else:
                raise ValueError(f"Unsupported vectorstore type: {self.vectorstore_type}")
            
            logger.info("Vectorstore loaded successfully")
            return True
        except Exception as e:
            logger.error(f"Error loading vectorstore: {e}")
            return False
    
    def search(self, query: str, k: int = TOP_K_RESULTS) -> List[Tuple[str, float]]:
        """Search vectorstore for similar documents"""
        if not self.vectorstore:
            logger.warning("Vectorstore not loaded")
            return []
        
        try:
            results = self.vectorstore.similarity_search_with_score(query, k=k)
            # Filter by similarity threshold
            filtered_results = [
                (doc.page_content, score) 
                for doc, score in results 
                if score >= SIMILARITY_THRESHOLD
            ]
            logger.info(f"Found {len(filtered_results)} relevant documents")
            return filtered_results
        except Exception as e:
            logger.error(f"Error searching vectorstore: {e}")
            return []
    
    def add_documents(self, chunks: List[str], doc_name: str) -> bool:
        """Add new documents to existing vectorstore"""
        try:
            docs = [
                Document(page_content=chunk, metadata={"source": doc_name, "chunk_id": i})
                for i, chunk in enumerate(chunks)
            ]
            
            embeddings = self.embedding_manager.get_embeddings_object()
            
            if not self.vectorstore:
                return self.create_vectorstore(chunks, doc_name)
            
            self.vectorstore.add_documents(docs)
            
            if self.vectorstore_type == "chroma":
                self.vectorstore.persist()
            elif self.vectorstore_type == "faiss":
                self.vectorstore.save_local(VECTOR_DB_PATH)
            
            logger.info(f"Added {len(docs)} documents to vectorstore")
            return True
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            return False
    
    def get_vectorstore_info(self) -> dict:
        """Get information about vectorstore"""
        if not self.vectorstore:
            return {"status": "not_loaded"}
        
        return {
            "type": self.vectorstore_type,
            "path": VECTOR_DB_PATH,
            "status": "loaded"
        }
