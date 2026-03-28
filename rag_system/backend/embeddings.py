import logging
from typing import List
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL, OPENAI_API_KEY, HF_API_TOKEN

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Manage embeddings for documents"""
    
    def __init__(self, model: str = EMBEDDING_MODEL):
        self.model = model
        self.embeddings = self._initialize_embeddings()
    
    def _initialize_embeddings(self):
        """Initialize embeddings based on model choice"""
        if "openai" in self.model.lower() or "text-embedding" in self.model.lower():
            if not OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is required for OpenAI embeddings")
            logger.info(f"Initializing OpenAI embeddings: {self.model}")
            return OpenAIEmbeddings(
                model=self.model,
                openai_api_key=OPENAI_API_KEY
            )
        else:
            logger.info(f"Initializing HuggingFace embeddings: {self.model}")
            return HuggingFaceEmbeddings(
                model_name=self.model,
                model_kwargs={"device": "cpu"}
            )
    
    def embed_text(self, text: str) -> List[float]:
        """Embed a single text"""
        return self.embeddings.embed_query(text)
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple documents"""
        return self.embeddings.embed_documents(texts)
    
    def get_embeddings_object(self):
        """Return the embeddings object for use with vector stores"""
        return self.embeddings
