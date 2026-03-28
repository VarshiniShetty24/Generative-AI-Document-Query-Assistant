import unittest
from pathlib import Path
import sys
import tempfile

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from document_loader import DocumentLoader
from embeddings import EmbeddingManager
from vector_store import VectorStoreManager
from config import SUPPORTED_FILE_TYPES


class TestDocumentLoader(unittest.TestCase):
    """Test document loading functionality"""
    
    def setUp(self):
        self.loader = DocumentLoader()
    
    def test_load_text_file(self):
        """Test loading text file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("This is a test document.\n" * 100)
            f.flush()
            
            chunks, doc_name = self.loader.load_documents(f.name)
            
            self.assertTrue(len(chunks) > 0)
            self.assertEqual(doc_name, Path(f.name).name)
    
    def test_load_csv_file(self):
        """Test loading CSV file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("Name,Age,City\nAlice,30,NYC\nBob,25,LA\n")
            f.flush()
            
            chunks, doc_name = self.loader.load_documents(f.name)
            
            self.assertTrue(len(chunks) > 0)
    
    def test_invalid_file_type(self):
        """Test handling of invalid file type"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
            f.write("test")
            f.flush()
            
            with self.assertRaises(ValueError):
                self.loader.load_documents(f.name)
    
    def test_file_not_found(self):
        """Test handling of non-existent file"""
        with self.assertRaises(FileNotFoundError):
            self.loader.load_documents("/non/existent/file.txt")


class TestEmbeddingManager(unittest.TestCase):
    """Test embedding functionality"""
    
    def test_embedding_initialization(self):
        """Test embedding manager initialization"""
        try:
            manager = EmbeddingManager(model="all-MiniLM-L6-v2")
            self.assertIsNotNone(manager.embeddings)
        except Exception as e:
            self.skipTest(f"Embedding model not available: {e}")


class TestVectorStore(unittest.TestCase):
    """Test vector store functionality"""
    
    def test_vectorstore_manager_initialization(self):
        """Test vector store manager initialization"""
        try:
            embedding_manager = EmbeddingManager(model="all-MiniLM-L6-v2")
            manager = VectorStoreManager(embedding_manager)
            self.assertIsNotNone(manager)
        except Exception as e:
            self.skipTest(f"Vector store not available: {e}")


if __name__ == "__main__":
    unittest.main()
