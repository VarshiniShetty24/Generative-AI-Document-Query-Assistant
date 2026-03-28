# 🚀 RAG System - Installation & Deployment Guide

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.8 or higher installed
- [ ] OpenAI API key (from https://platform.openai.com/api-keys)
- [ ] OR HuggingFace token (from https://huggingface.co/settings/tokens)
- [ ] 2GB free disk space
- [ ] Git (optional, for version control)
- [ ] Docker (optional, for containerized deployment)

---

## Windows Installation

### Option 1: Automated Setup (Recommended)

1. **Open Command Prompt or PowerShell**
   - Navigate to project directory: `cd C:\Users\your_username\Desktop\project\rag_system`

2. **Run Setup Script**
   ```batch
   setup.bat
   ```

3. **Configure API Keys**
   - Open `.env` in notepad or your editor
   - Add your API keys:
     ```env
     OPENAI_API_KEY=sk-your-actual-key-here
     ```

4. **Start Application**
   ```batch
   cd frontend
   streamlit run app.py
   ```

### Option 2: Manual Setup

1. **Create Virtual Environment**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Setup Configuration**
   ```cmd
   copy .env.example .env
   # Edit .env with your API keys
   ```

4. **Create Data Directories**
   ```cmd
   mkdir data\documents
   mkdir data\vectorstore
   ```

5. **Run Application**
   ```cmd
   cd frontend
   streamlit run app.py
   ```

---

## Linux/macOS Installation

### Option 1: Automated Setup

1. **Navigate to Project**
   ```bash
   cd ~/Desktop/project/rag_system
   ```

2. **Run Setup Script**
   ```bash
   chmod +x setup.sh
   bash setup.sh
   ```

3. **Configure API Keys**
   ```bash
   nano .env
   # Add: OPENAI_API_KEY=sk-your-key
   ```

4. **Start Application**
   ```bash
   source venv/bin/activate
   cd frontend
   streamlit run app.py
   ```

### Option 2: Manual Setup

1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Configuration**
   ```bash
   cp .env.example .env
   # Edit .env and add API keys
   ```

4. **Create Data Directories**
   ```bash
   mkdir -p data/documents
   mkdir -p data/vectorstore
   ```

5. **Run Application**
   ```bash
   cd frontend
   streamlit run app.py
   ```

---

## Docker Installation

### Using Docker (Recommended for Production)

1. **Build Docker Image**
   ```bash
   docker build -t rag-system .
   ```

2. **Run Container**
   ```bash
   docker run -p 8501:8501 \
     -e OPENAI_API_KEY=sk-your-key \
     -e HF_API_TOKEN=hf-your-token \
     -v $(pwd)/data:/app/data \
     rag-system
   ```

3. **Access Application**
   - Open http://localhost:8501

### Using Docker Compose (Recommended)

1. **Create .env File**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

2. **Start Services**
   ```bash
   docker-compose up
   ```

3. **Access Services**
   - Streamlit: http://localhost:8501
   - API: http://localhost:8000
   - Database: localhost:5432

4. **Stop Services**
   ```bash
   docker-compose down
   ```

---

## Configuration Guide

### Essential Configuration

Create or edit `.env` file with these settings:

```env
# OpenAI API Key (Required for GPT models)
OPENAI_API_KEY=sk-your-key-here

# HuggingFace Token (Required for HF models)
HF_API_TOKEN=hf-your-token-here

# LLM Model Selection
LLM_MODEL=gpt-3.5-turbo
# Alternatives: gpt-4, meta-llama/Llama-2-7b-hf, mistralai/Mistral-7B

# Embedding Model
EMBEDDING_MODEL=text-embedding-3-small
# Alternatives: text-embedding-3-large, all-MiniLM-L6-v2

# Vector Database
VECTORSTORE_TYPE=chroma
# Alternatives: faiss

# Processing Parameters
CHUNK_SIZE=1024          # Characters per chunk
CHUNK_OVERLAP=256        # Overlap between chunks
MAX_FILE_SIZE_MB=50      # Max file size

# Retrieval Parameters
TOP_K_RESULTS=5          # Number of documents to retrieve
SIMILARITY_THRESHOLD=0.3 # Minimum similarity score

# Chat Configuration
MAX_HISTORY=10           # Messages to keep in memory
CONTEXT_WINDOW=3000      # Token context for LLM

# Performance
USE_CACHE=true
CACHE_TTL=3600          # Cache lifetime in seconds
```

### Configuration Profiles

#### Speed-Optimized
```env
CHUNK_SIZE=512
EMBEDDING_MODEL=text-embedding-3-small
TOP_K_RESULTS=3
VECTORSTORE_TYPE=faiss
```

#### Accuracy-Optimized
```env
CHUNK_SIZE=1024
EMBEDDING_MODEL=text-embedding-3-large
TOP_K_RESULTS=5
LLM_MODEL=gpt-4
VECTORSTORE_TYPE=chroma
```

#### Budget-Friendly (Free)
```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=mistralai/Mistral-7B-Instruct
USE_CACHE=true
VECTORSTORE_TYPE=faiss
```

---

## API Keys Setup

### Getting OpenAI API Key

1. Visit https://platform.openai.com/account/api-keys
2. Click "Create new secret key"
3. Copy the key immediately (you won't see it again)
4. Add to `.env`:
   ```env
   OPENAI_API_KEY=sk-...
   ```

### Getting HuggingFace Token

1. Visit https://huggingface.co/settings/tokens
2. Click "New token"
3. Give it a name, select "Read"
4. Copy and add to `.env`:
   ```env
   HF_API_TOKEN=hf_...
   ```

---

## Verification Steps

### 1. Check Installation
```bash
python --version  # Should be 3.8+
pip list          # Should show langchain, streamlit, etc.
```

### 2. Test Backend
```bash
cd backend
python -c "from rag_pipeline import RAGPipeline; print('✓ Backend OK')"
```

### 3. Test Frontend
```bash
cd frontend
streamlit run app.py --logger.level=debug
```

### 4. Test API (Optional)
```bash
cd backend
python api.py
# In another terminal:
curl http://localhost:8000/health
```

---

## First-Time Usage

### 1. Start the Application
```bash
streamlit run frontend/app.py
```

### 2. Upload a Document
- Click "📤 Upload Documents" in sidebar
- Select a PDF, CSV, or TXT file
- Wait for processing to complete

### 3. Ask a Question
- Type your question in the chat input
- Click "Send" or press Enter
- Read the AI response

### 4. Continue Conversation
- Ask follow-up questions
- The system remembers context
- View chat history in System Info

---

## Troubleshooting

### Installation Issues

**Issue: "pip command not found"**
```bash
# Windows
python -m pip install -r requirements.txt

# Linux/Mac
python3 -m pip install -r requirements.txt
```

**Issue: "Virtual environment not activating"**
```bash
# Windows
python -m venv venv
venv\Scripts\activate.bat  # Use .bat, not .bat

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**Issue: Module import errors**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Configuration Issues

**Issue: "OPENAI_API_KEY is required"**
1. Check `.env` file exists in project root
2. Verify key format: `OPENAI_API_KEY=sk-...`
3. No spaces around `=` sign
4. Restart application after editing `.env`

**Issue: API Key not being recognized**
```bash
# Verify .env is being read
streamlit run frontend/app.py --logger.level=debug
```

### Runtime Issues

**Issue: "No module named 'openai'"**
```bash
pip install openai>=1.0.0
```

**Issue: "FAISS import error"**
```bash
pip install faiss-cpu
# Or for GPU:
pip install faiss-gpu
```

**Issue: Port 8501 already in use**
```bash
streamlit run frontend/app.py --server.port=8502
```

---

## Performance Optimization

### For Faster Response Times
```env
CHUNK_SIZE=512
TOP_K_RESULTS=3
EMBEDDING_MODEL=text-embedding-3-small
USE_CACHE=true
```

### For Better Accuracy
```env
CHUNK_SIZE=1024
TOP_K_RESULTS=5
EMBEDDING_MODEL=text-embedding-3-large
LLM_MODEL=gpt-4
```

### For Batch Processing
```python
from rag_pipeline import RAGPipeline
from pathlib import Path

rag = RAGPipeline()
for doc in Path("data/documents").glob("*.pdf"):
    rag.ingest_document(str(doc))
```

---

## Testing the Installation

### Test Script
```python
# test_installation.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "backend"))

print("✓ Testing installation...")

try:
    from document_loader import DocumentLoader
    print("  ✓ Document loader OK")
except Exception as e:
    print(f"  ✗ Document loader: {e}")

try:
    from embeddings import EmbeddingManager
    print("  ✓ Embeddings OK")
except Exception as e:
    print(f"  ✗ Embeddings: {e}")

try:
    from vector_store import VectorStoreManager
    print("  ✓ Vector store OK")
except Exception as e:
    print(f"  ✗ Vector store: {e}")

try:
    from llm import LLMManager
    print("  ✓ LLM manager OK")
except Exception as e:
    print(f"  ✗ LLM manager: {e}")

try:
    from rag_pipeline import RAGPipeline
    print("  ✓ RAG pipeline OK")
except Exception as e:
    print(f"  ✗ RAG pipeline: {e}")

print("\n✓ Installation test complete!")
```

Run with:
```bash
python test_installation.py
```

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys
3. ✅ Upload sample documents
4. ✅ Test Q&A functionality
5. ⬜ Customize configuration for your use case
6. ⬜ Deploy to production
7. ⬜ Integrate with your applications

---

## Getting Help

### Logs
```bash
# View Streamlit logs
streamlit run frontend/app.py --logger.level=debug

# View API logs
python backend/api.py
```

### Documentation
- **README.md**: Complete documentation
- **GETTING_STARTED.md**: Quick start guide
- **PROJECT_SUMMARY.md**: Architecture overview
- **Inline comments**: Code documentation

### Common Commands

```bash
# Clear cache
rm -rf data/cache/*.cache

# Reset vectorstore
rm -rf data/vectorstore/

# View configuration
cat .env

# Run tests
python -m pytest backend/test_rag.py -v

# Run CLI interface
python quickstart.py
```

---

## Production Checklist

Before deploying to production:

- [ ] Use strong API key management
- [ ] Enable HTTPS/TLS
- [ ] Add authentication
- [ ] Configure rate limiting
- [ ] Setup monitoring and logging
- [ ] Test with production data
- [ ] Document custom configurations
- [ ] Backup vector database
- [ ] Setup error alerting
- [ ] Plan for scaling

---

**You're all set! 🎉**

Start the application and upload your first document to get started!
