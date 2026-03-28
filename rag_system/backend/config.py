import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"
VECTORSTORE_DIR = DATA_DIR / "vectorstore"

# Create directories if they don't exist
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# LLM Configuration
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# Vector Database Configuration
VECTORSTORE_TYPE = os.getenv("VECTORSTORE_TYPE", "chroma")  # or "faiss"
VECTOR_DB_PATH = str(VECTORSTORE_DIR / "chroma_db")

# Document Processing Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1024"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "256"))
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "50"))

# Retrieval Configuration
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "5"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.3"))

# Chat Configuration
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "10"))
CONTEXT_WINDOW = int(os.getenv("CONTEXT_WINDOW", "3000"))

# Supported file types
SUPPORTED_FILE_TYPES = {
    "pdf": [".pdf"],
    "csv": [".csv"],
    "text": [".txt", ".md", ".docx"],
}

# Cache configuration
USE_CACHE = os.getenv("USE_CACHE", "true").lower() == "true"
CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))
