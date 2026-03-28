# RAG System - Getting Started Guide

## 🚀 Quick Start (5 minutes)

### Step 1: Setup
```bash
# Navigate to project directory
cd rag_system

# Run setup script (Windows)
setup.bat

# Or for Linux/Mac
bash setup.sh
```

### Step 2: Configure API Keys
Edit `.env` file and add your keys:
```env
OPENAI_API_KEY=sk-your-key-here
HF_API_TOKEN=hf_your-token-here
```

### Step 3: Start the Application
```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

# Run Streamlit
cd frontend
streamlit run app.py
```

The app will open at **http://localhost:8501** 🎉

---

## 📚 Features Overview

### 1. **Document Upload & Processing**
- Drag-and-drop upload
- Automatic text extraction and chunking
- Support for PDF, CSV, TXT, MD, DOCX
- Real-time processing feedback

### 2. **Intelligent Retrieval**
- Semantic search with embeddings
- Configurable similarity thresholds
- Multi-document context fusion
- Smart chunk selection

### 3. **Conversational AI**
- Context-aware responses
- Chat history maintenance
- Multi-turn conversations
- History export

### 4. **System Management**
- Document inventory
- Model configuration
- System metrics
- Cache management

---

## 🛠️ Configuration Guide

### Basic Configuration (.env)

```env
# Essential Keys
OPENAI_API_KEY=sk-...
HF_API_TOKEN=hf_...

# Model Selection
LLM_MODEL=gpt-3.5-turbo           # or: gpt-4, meta-llama/Llama-2-7b
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database
VECTORSTORE_TYPE=chroma            # or: faiss

# Processing
CHUNK_SIZE=1024                     # 512-2048 recommended
CHUNK_OVERLAP=256                   # 20-30% of CHUNK_SIZE
MAX_FILE_SIZE_MB=50                 # Safety limit

# Retrieval
TOP_K_RESULTS=5                     # 3-10 recommended
SIMILARITY_THRESHOLD=0.3            # 0.2-0.5 recommended

# Chat
MAX_HISTORY=10                      # Messages to keep
CONTEXT_WINDOW=3000                 # Tokens for context

# Performance
USE_CACHE=true
CACHE_TTL=3600                      # Seconds
```

---

## 💡 Usage Examples

### Example 1: Upload and Ask
1. Click "📤 Upload Documents" in sidebar
2. Select PDF/CSV/TXT files
3. Wait for processing (shows chunk count)
4. Ask questions in the chat

### Example 2: Multi-Document Queries
1. Upload multiple documents
2. Ask cross-document questions
3. System retrieves relevant chunks from all docs
4. Generates contextualized answers

### Example 3: Conversation Flow
```
User: "Summarize the main topics"
AI: [Generates summary from documents]

User: "Tell me more about topic X"
AI: [Uses previous context + retrieval]

User: "Compare X and Y"
AI: [Uses history + retrieval]
```

---

## 🔑 API Keys Setup

### OpenAI API
1. Visit https://platform.openai.com/api-keys
2. Create new secret key
3. Add to `.env`: `OPENAI_API_KEY=sk-...`

### HuggingFace Token
1. Visit https://huggingface.co/settings/tokens
2. Create new token
3. Add to `.env`: `HF_API_TOKEN=hf_...`

---

## 📊 Performance Tips

### For Better Speed
```env
CHUNK_SIZE=768
EMBEDDING_MODEL=text-embedding-3-small
VECTORSTORE_TYPE=faiss
TOP_K_RESULTS=3
```

### For Better Accuracy
```env
CHUNK_SIZE=1024
EMBEDDING_MODEL=text-embedding-3-large
VECTORSTORE_TYPE=chroma
TOP_K_RESULTS=5
LLM_MODEL=gpt-4
```

### For Local/Free Setup
```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=mistralai/Mistral-7B-Instruct-v0.1
USE_CACHE=true
```

---

## 🐳 Docker Deployment

### Build and Run
```bash
# Build image
docker build -t rag-system .

# Run container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=sk-... \
  -v $(pwd)/data:/app/data \
  rag-system
```

### Using Docker Compose
```bash
# Create .env with your keys
cp .env.example .env
# Edit .env with API keys

# Start services
docker-compose up

# Access at http://localhost:8501
```

---

## 🔌 REST API Usage

### Start API Server
```bash
cd backend
python api.py
```

### Example API Calls

**Upload Document:**
```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@document.pdf"
```

**Query:**
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic?"}'
```

**Get Documents:**
```bash
curl "http://localhost:8000/documents"
```

**Get Chat History:**
```bash
curl "http://localhost:8000/history"
```

**System Info:**
```bash
curl "http://localhost:8000/system-info"
```

---

## 🔧 Troubleshooting

### Issue: "OPENAI_API_KEY is required"
**Solution:** Make sure `.env` is in project root with valid key

### Issue: "Module not found" errors
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Slow response times
**Solution:**
- Reduce CHUNK_SIZE to 512
- Reduce TOP_K_RESULTS to 3
- Use faster embedding model

### Issue: Out of memory
**Solution:**
- Reduce MAX_HISTORY
- Use smaller embedding model
- Process smaller files

### Issue: FAISS import error
**Solution:**
```bash
pip install faiss-cpu  # or faiss-gpu
```

---

## 📖 Advanced Features

### Custom Prompts
Edit `backend/llm.py` to modify system prompts for domain-specific responses.

### Batch Processing
```python
from rag_pipeline import RAGPipeline
from pathlib import Path

rag = RAGPipeline()
for doc in Path("documents").glob("*.pdf"):
    rag.ingest_document(str(doc))
```

### Programmatic Usage
```python
from backend.rag_pipeline import RAGPipeline

rag = RAGPipeline()
rag.ingest_document("doc.pdf")
answer = rag.query("What is this about?")
print(answer)
```

---

## 🚀 Production Deployment

### Recommended Stack
- **Frontend:** Streamlit + Nginx reverse proxy
- **Backend:** FastAPI + Gunicorn/Uvicorn
- **Database:** PostgreSQL for persistence
- **Vector DB:** Chroma with persistence
- **Caching:** Redis
- **Deployment:** Docker + Kubernetes

### Security Checklist
- [ ] Use environment variables for secrets
- [ ] Enable input validation
- [ ] Add authentication
- [ ] Use HTTPS
- [ ] Rate limiting
- [ ] Log monitoring
- [ ] Regular backups

---

## 📞 Support & Resources

- **Documentation:** See README.md for detailed info
- **Issues:** Check troubleshooting section
- **Examples:** See quickstart.py for CLI usage
- **Tests:** Run `python backend/test_rag.py`

---

## 🎯 Next Steps

1. ✅ Complete setup
2. ✅ Add API keys
3. ✅ Upload sample documents
4. ✅ Ask test questions
5. ✅ Explore API endpoints
6. ✅ Customize configuration
7. ✅ Deploy to production

---

**Happy building! 🚀**
