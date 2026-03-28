# RAG Document QA System

A production-ready **Retrieval-Augmented Generation (RAG)** system for semantic question answering over documents.

## ✨ Features

- 📄 **Multi-format support**: PDF, CSV, TXT, MD, DOCX
- 🔍 **Semantic search**: OpenAI & HuggingFace embeddings
- 🤖 **LLM powered**: GPT-3.5/4 & HuggingFace models
- 💬 **Web interface**: Beautiful Streamlit UI
- ⚙️ **Production ready**: REST API, Docker, caching
- 📊 **Vector databases**: Chroma & FAISS support

## Quick Start

### 1. Setup
```bash
# Windows
setup.bat

# Linux/Mac
bash setup.sh
```

### 2. Configure
Edit `.env`:
```env
OPENAI_API_KEY=sk-your-key-here
LLM_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-small
```

### 3. Run
```bash
cd frontend
streamlit run app.py
```

Access at: **http://localhost:8501**

## Project Structure

```
├── backend/              # Python backend modules
│   ├── config.py        # Configuration
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   ├── cache.py
│   ├── error_handler.py
│   ├── api.py           # FastAPI REST endpoints
│   └── test_rag.py
│
├── frontend/
│   └── app.py           # Streamlit web app
│
├── data/                # Document storage
│
├── requirements.txt     # Python dependencies
├── .env.example         # Configuration template
├── setup.bat / setup.sh # Setup scripts
├── Dockerfile           # Docker image
└── README.md            # This file
```

## Core Modules

| Module | Purpose |
|--------|---------|
| `config.py` | Configuration management |
| `document_loader.py` | Multi-format document processing |
| `embeddings.py` | Text-to-vector conversion |
| `vector_store.py` | Vector database operations |
| `llm.py` | LLM interactions |
| `rag_pipeline.py` | Main orchestration |
| `api.py` | REST API endpoints |

## Configuration

Key environment variables in `.env`:

```env
# API Keys
OPENAI_API_KEY=sk-...
HF_API_TOKEN=hf_...

# Models
LLM_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-small
VECTORSTORE_TYPE=chroma

# Processing
CHUNK_SIZE=1024
CHUNK_OVERLAP=256
TOP_K_RESULTS=5

# Chat
MAX_HISTORY=10
CONTEXT_WINDOW=3000
```

## Usage

### Web UI
1. Upload documents (PDF, CSV, TXT, MD, DOCX)
2. Ask questions
3. Get context-aware answers
4. View conversation history

### REST API
```bash
# Upload document
curl -X POST "http://localhost:8000/upload" \
  -F "file=@document.pdf"

# Query
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this about?"}'
```

### Python
```python
from backend.rag_pipeline import RAGPipeline

rag = RAGPipeline()
rag.ingest_document("document.pdf")
answer = rag.query("Your question?")
```

## Deployment

### Docker
```bash
docker-compose up
```

Access at: http://localhost:8501

## Performance Tips

**For Speed:**
- `CHUNK_SIZE=512`
- `EMBEDDING_MODEL=text-embedding-3-small`
- `TOP_K_RESULTS=3`

**For Accuracy:**
- `CHUNK_SIZE=1024`
- `EMBEDDING_MODEL=text-embedding-3-large`
- `LLM_MODEL=gpt-4`

**For Low Cost:**
- `EMBEDDING_MODEL=all-MiniLM-L6-v2`
- `LLM_MODEL=mistralai/Mistral-7B`

## Requirements

- Python 3.8+
- 2GB RAM minimum
- OpenAI API key OR HuggingFace token

## License

MIT License

## Support

For issues or questions:
1. Check configuration in `.env`
2. Review logs for error messages
3. Verify API keys are valid
4. Run unit tests: `python backend/test_rag.py`

---

**Happy querying! 🚀**
