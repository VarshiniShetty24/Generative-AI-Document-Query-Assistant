import logging
from typing import List, Optional, Dict, Tuple
from pathlib import Path
import json
from datetime import datetime
from document_loader import DocumentLoader
from embeddings import EmbeddingManager
from vector_store import VectorStoreManager
from llm import LLMManager
from config import MAX_HISTORY

logger = logging.getLogger(__name__)


class RAGPipeline:
    """Complete RAG pipeline orchestration"""
    
    def __init__(self):
        self.document_loader = DocumentLoader()
        self.embedding_manager = EmbeddingManager()
        self.vector_store = VectorStoreManager(self.embedding_manager)
        self.llm = LLMManager()
        self.chat_history: List[Dict] = []
        self.processed_documents: List[str] = []
        
        # Try to load existing vectorstore
        self.vector_store.load_vectorstore()
    
    def ingest_document(self, file_path: str) -> Tuple[bool, str]:
        """Ingest a new document into the RAG system"""
        try:
            # Load document
            chunks, doc_name = self.document_loader.load_documents(file_path)
            
            # Add to vectorstore
            success = self.vector_store.add_documents(chunks, doc_name)
            
            if success:
                self.processed_documents.append(doc_name)
                logger.info(f"Successfully ingested document: {doc_name}")
                return True, f"Document '{doc_name}' ingested successfully ({len(chunks)} chunks)"
            else:
                return False, "Failed to add document to vectorstore"
        except Exception as e:
            logger.error(f"Error ingesting document: {e}")
            return False, str(e)
    
    def query(self, question: str) -> str:
        """Process a query through the RAG pipeline"""
        try:
            # Retrieve relevant documents
            results = self.vector_store.search(question)
            
            if not results:
                logger.warning("No relevant documents found")
                answer = self.llm.generate_answer(question, "No relevant context found.")
            else:
                # Prepare context from top results
                context = "\n\n---\n\n".join([doc for doc, _ in results])
                
                # Generate answer with context
                answer = self.llm.generate_answer(question, context)
            
            # Store in chat history
            self._add_to_history(question, answer, len(results))
            
            return answer
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return f"Error processing query: {str(e)}"
    
    def conversational_query(self, question: str) -> str:
        """Process query with conversation history"""
        try:
            # Build context from history
            history_context = self._build_history_context()
            
            # Retrieve relevant documents
            results = self.vector_store.search(question)
            
            if results:
                doc_context = "\n\n---\n\n".join([doc for doc, _ in results])
                full_context = f"{history_context}\n\nRelevant Documentation:\n{doc_context}"
            else:
                full_context = history_context
            
            # Generate answer
            answer = self.llm.generate_answer(question, full_context)
            
            # Store in chat history
            self._add_to_history(question, answer, len(results))
            
            return answer
        except Exception as e:
            logger.error(f"Error processing conversational query: {e}")
            return f"Error processing query: {str(e)}"
    
    def _add_to_history(self, question: str, answer: str, results_count: int):
        """Add query to chat history"""
        self.chat_history.append({
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "results_count": results_count
        })
        
        # Keep only recent history
        if len(self.chat_history) > MAX_HISTORY:
            self.chat_history = self.chat_history[-MAX_HISTORY:]
    
    def _build_history_context(self) -> str:
        """Build context from chat history"""
        if not self.chat_history:
            return "No previous conversation."
        
        history = []
        for item in self.chat_history[-3:]:  # Keep last 3 exchanges
            history.append(f"Q: {item['question']}\nA: {item['answer']}")
        
        return "Previous conversation:\n" + "\n\n".join(history)
    
    def get_chat_history(self) -> List[Dict]:
        """Get current chat history"""
        return self.chat_history
    
    def clear_chat_history(self):
        """Clear chat history"""
        self.chat_history = []
        logger.info("Chat history cleared")
    
    def get_processed_documents(self) -> List[str]:
        """Get list of processed documents"""
        return self.processed_documents
    
    def get_system_info(self) -> Dict:
        """Get system information"""
        return {
            "documents_processed": len(self.processed_documents),
            "processed_documents": self.processed_documents,
            "vectorstore_info": self.vector_store.get_vectorstore_info(),
            "chat_history_length": len(self.chat_history),
            "embedding_model": self.embedding_manager.model,
            "llm_model": self.llm.model
        }
