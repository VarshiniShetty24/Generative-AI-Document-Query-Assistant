import logging
from pathlib import Path
from typing import List, Tuple
import PyPDF2
import pandas as pd
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP, SUPPORTED_FILE_TYPES, MAX_FILE_SIZE_MB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentLoader:
    """Load and process documents from various formats"""
    
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def load_documents(self, file_path: str) -> Tuple[List[str], str]:
        """
        Load and process a document from the given file path.
        
        Returns:
            Tuple of (chunks, document_name)
        """
        file_path = Path(file_path)
        
        # Validate file exists and size
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_size_mb = file_path.stat().st_size / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            raise ValueError(f"File size {file_size_mb:.2f}MB exceeds limit of {MAX_FILE_SIZE_MB}MB")
        
        # Load based on file type
        file_ext = file_path.suffix.lower()
        
        if file_ext == ".pdf":
            text = self._load_pdf(file_path)
        elif file_ext == ".csv":
            text = self._load_csv(file_path)
        elif file_ext == ".txt":
            text = self._load_text(file_path)
        elif file_ext == ".md":
            text = self._load_markdown(file_path)
        elif file_ext == ".docx":
            text = self._load_docx(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")
        
        # Split into chunks
        chunks = self.text_splitter.split_text(text)
        
        logger.info(f"Loaded {file_path.name}: {len(chunks)} chunks")
        return chunks, file_path.name
    
    def _load_pdf(self, file_path: Path) -> str:
        """Extract text from PDF"""
        text = []
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(pdf_reader.pages):
                    page_text = page.extract_text()
                    text.append(f"--- Page {page_num + 1} ---\n{page_text}")
            return "\n".join(text)
        except Exception as e:
            logger.error(f"Error loading PDF {file_path}: {e}")
            raise
    
    def _load_csv(self, file_path: Path) -> str:
        """Load CSV and convert to formatted text"""
        try:
            df = pd.read_csv(file_path)
            return df.to_string()
        except Exception as e:
            logger.error(f"Error loading CSV {file_path}: {e}")
            raise
    
    def _load_text(self, file_path: Path) -> str:
        """Load plain text file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Error loading text file {file_path}: {e}")
            raise
    
    def _load_markdown(self, file_path: Path) -> str:
        """Load markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Error loading markdown file {file_path}: {e}")
            raise
    
    def _load_docx(self, file_path: Path) -> str:
        """Extract text from DOCX"""
        try:
            doc = Document(file_path)
            paragraphs = [para.text for para in doc.paragraphs]
            return "\n".join(paragraphs)
        except Exception as e:
            logger.error(f"Error loading DOCX {file_path}: {e}")
            raise
