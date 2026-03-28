import logging
from typing import Dict, List, Optional
from enum import Enum

logger = logging.getLogger(__name__)


class ErrorSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RAGException(Exception):
    """Base exception for RAG system"""
    
    def __init__(self, message: str, severity: ErrorSeverity = ErrorSeverity.MEDIUM):
        self.message = message
        self.severity = severity
        super().__init__(self.message)


class DocumentProcessingError(RAGException):
    """Exception during document processing"""
    pass


class VectorStoreError(RAGException):
    """Exception in vector store operations"""
    pass


class LLMError(RAGException):
    """Exception in LLM operations"""
    pass


class ConfigurationError(RAGException):
    """Exception in configuration"""
    pass


class ErrorHandler:
    """Handle and log errors consistently"""
    
    def __init__(self):
        self.errors: List[Dict] = []
    
    def handle_error(self, error: Exception, context: str = "") -> str:
        """Handle an error and return user-friendly message"""
        error_record = {
            "type": type(error).__name__,
            "message": str(error),
            "context": context
        }
        self.errors.append(error_record)
        
        logger.error(f"Error in {context}: {error}")
        
        # Return user-friendly message
        if isinstance(error, RAGException):
            return error.message
        elif isinstance(error, FileNotFoundError):
            return "File not found. Please check the file path."
        elif isinstance(error, ValueError):
            return f"Invalid value: {str(error)}"
        else:
            return "An unexpected error occurred. Please try again."
    
    def get_errors(self) -> List[Dict]:
        """Get recorded errors"""
        return self.errors
    
    def clear_errors(self):
        """Clear error records"""
        self.errors = []
