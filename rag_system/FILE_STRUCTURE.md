# Complete RAG System - File Structure & Overview

## 📦 Project Root

```
rag_system/
├── backend/                          # Backend services (Python)
├── frontend/                         # Frontend application (Streamlit)
├── data/                            # Data storage
├── .env                             # Configuration (SENSITIVE - not in git)
├── .env.example                     # Configuration template
├── .gitignore                       # Git ignore rules
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker image definition
├── docker-compose.yml               # Docker services composition
├── setup.sh                         # Linux/Mac setup script
├── setup.bat                        # Windows setup script
├── quickstart.py                    # CLI interface
├── README.md                        # Complete documentation
├── GETTING_STARTED.md              # Quick start guide
├── INSTALLATION.md                 # Detailed installation guide
├── PROJECT_SUMMARY.md              # Project overview
└── LICENSE                         # MIT License
```

---

## 🎯 Backend Module Structure

```
backend/
├── __init__.py                     # Package initialization
│
├── config.py                       # Configuration management
│   ├── PROJECT_ROOT
│   ├── DATA_DIR, DOCUMENTS_DIR
│   ├── VECTORSTORE_DIR
│   ├── API Keys (OPENAI_API_KEY, HF_API_TOKEN)
│   ├── Model configuration
│   ├── Processing parameters
│   ├── Retrieval settings
│   └── Cache configuration
│
├── document_loader.py              # Document processing
│   ├── DocumentLoader class
│   ├── load_documents()
│   ├── _load_pdf()
│   ├── _load_csv()
│   ├── _load_text()
│   ├── _load_markdown()
│   └── _load_docx()
│
├── embeddings.py                   # Embedding management
│   ├── EmbeddingManager class
│   ├── _initialize_embeddings()
│   ├── embed_text()
│   ├── embed_documents()
│   └── get_embeddings_object()
│
├── vector_store.py                 # Vector database operations
│   ├── VectorStoreManager class
│   ├── create_vectorstore()
│   ├── load_vectorstore()
│   ├── search()
│   ├── add_documents()
│   └── get_vectorstore_info()
│
├── llm.py                          # LLM interactions
│   ├── LLMManager class
│   ├── _initialize_llm()
│   ├── _create_qa_prompt()
│   ├── generate_answer()
│   └── refine_answer()
│
├── rag_pipeline.py                 # Main orchestration
│   ├── RAGPipeline class
│   ├── ingest_document()
│   ├── query()
│   ├── conversational_query()
│   ├── get_chat_history()
│   ├── clear_chat_history()
│   ├── get_processed_documents()
│   ├── get_system_info()
│   ├── _add_to_history()
│   └── _build_history_context()
│
├── cache.py                        # Caching layer
│   ├── CacheManager class
│   ├── get()
│   ├── set()
│   ├── clear()
│   └── @cache_result decorator
│
├── error_handler.py                # Error management
│   ├── ErrorSeverity enum
│   ├── RAGException (base)
│   ├── DocumentProcessingError
│   ├── VectorStoreError
│   ├── LLMError
│   ├── ConfigurationError
│   ├── ErrorHandler class
│   ├── handle_error()
│   ├── get_errors()
│   └── clear_errors()
│
├── api.py                          # REST API (FastAPI)
│   ├── FastAPI application setup
│   ├── CORS configuration
│   ├── POST /upload
│   ├── POST /query
│   ├── GET /documents
│   ├── GET /history
│   ├── DELETE /history
│   ├── GET /system-info
│   ├── GET /health
│   └── Error handlers
│
└── test_rag.py                     # Unit tests
    ├── TestDocumentLoader
    ├── TestEmbeddingManager
    └── TestVectorStore
```

---

## 🎨 Frontend Structure

```
frontend/
├── app.py                          # Main Streamlit application
│   ├── Page configuration
│   ├── Custom CSS styling
│   ├── Session state management
│   │
│   ├── Sidebar:
│   │   ├── Mode selection (Chat, Document Management, System Info)
│   │   └── Document upload
│   │
│   ├── Chat Mode:
│   │   ├── Document list display
│   │   ├── Chat container
│   │   ├── Message display (user/assistant)
│   │   ├── Input area
│   │   └── History management
│   │
│   ├── Document Management Mode:
│   │   ├── Upload interface
│   │   ├── Processing feedback
│   │   └── Document inventory
│   │
│   └── System Info Mode:
│       ├── Statistics display
│       ├── Model information
│       ├── Vectorstore status
│       └── Chat history details
```

---

## 💾 Data Directory Structure

```
data/
├── documents/                      # Uploaded documents directory
│   ├── sample_ml_guide.txt        # Sample document for testing
│   ├── document1.pdf
│   ├── document2.csv
│   └── ...
│
├── vectorstore/                    # Vector database storage
│   ├── chroma_db/                 # If using Chroma
│   │   ├── chroma_index/
│   │   └── metadata
│   └── faiss_index/               # If using FAISS
│
└── cache/                          # Cache directory
    ├── hash1.cache
    ├── hash2.cache
    └── ...
```

---

## 📝 Configuration Files

### .env (Environment Variables)
```
OPENAI_API_KEY=sk-...              # OpenAI key (sensitive)
HF_API_TOKEN=hf_...                # HuggingFace token (sensitive)

LLM_MODEL=gpt-3.5-turbo            # Language model selection
EMBEDDING_MODEL=text-embedding-3-small  # Embedding model

VECTORSTORE_TYPE=chroma            # Vector database type
CHUNK_SIZE=1024                    # Text chunk size
CHUNK_OVERLAP=256                  # Chunk overlap
MAX_FILE_SIZE_MB=50                # File size limit

TOP_K_RESULTS=5                    # Retrieval count
SIMILARITY_THRESHOLD=0.3           # Min similarity score

MAX_HISTORY=10                     # Chat history size
CONTEXT_WINDOW=3000                # Context length

USE_CACHE=true                     # Enable caching
CACHE_TTL=3600                     # Cache lifetime
```

### requirements.txt
```
Core Dependencies:
- langchain>=0.1.0                 # LLM framework
- openai>=1.0.0                    # OpenAI API
- chromadb>=0.4.0                  # Vector DB (Chroma)
- faiss-cpu>=1.7.4                 # Vector DB (FAISS)

Document Processing:
- PyPDF2>=3.0.1                    # PDF extraction
- pandas>=2.0.0                    # CSV processing
- python-docx>=0.8.11              # DOCX support

Frontend:
- streamlit>=1.28.0                # Web UI
- streamlit-chat>=0.1.1            # Chat component

API:
- fastapi>=0.104.0                 # REST API
- uvicorn>=0.24.0                  # ASGI server
- pydantic>=2.0.0                  # Data validation

Optional:
- sentence-transformers>=2.2.0     # Local embeddings
- huggingface-hub>=0.17.0          # HF model access

Development:
- pytest>=7.4.0                    # Testing
- black>=23.7.0                    # Code formatting
- flake8>=6.0.0                    # Linting
```

### Dockerfile
```dockerfile
FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gcc g++
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p data/documents data/vectorstore
EXPOSE 8501
CMD ["streamlit", "run", "frontend/app.py"]
```

### docker-compose.yml
```yaml
Services:
- rag-system: Main Streamlit application (port 8501)
- postgres: Optional PostgreSQL database (port 5432)

Volumes:
- data directory: Persisted for documents and vectorstore
- postgres_data: Database persistence
```

---

## 📚 Documentation Files

### README.md
- Project overview
- Features list
- Installation instructions
- Configuration guide
- Usage examples
- API documentation
- Troubleshooting
- Deployment options
- Contributing guidelines

### GETTING_STARTED.md
- Quick start (5 minutes)
- Feature overview
- Configuration examples
- Usage scenarios
- API usage
- Performance tips
- Docker deployment
- Troubleshooting quick reference

### INSTALLATION.md
- Prerequisites checklist
- Windows installation
- Linux/macOS installation
- Docker installation
- Configuration profiles
- API key setup
- Verification steps
- Production checklist

### PROJECT_SUMMARY.md
- Project overview
- Architecture diagram
- Technology stack
- System configuration
- Usage scenarios
- Feature list
- Performance metrics
- Security features

---

## 🔑 Key Features by File

| Feature | Primary File | Supporting Files |
|---------|-------------|-----------------|
| Document Loading | document_loader.py | config.py |
| Text Embedding | embeddings.py | config.py |
| Vector Storage | vector_store.py | embeddings.py, config.py |
| LLM Interaction | llm.py | config.py |
| Pipeline Orchestration | rag_pipeline.py | All backend modules |
| Web Interface | frontend/app.py | rag_pipeline.py |
| REST API | backend/api.py | rag_pipeline.py |
| Caching | cache.py | config.py |
| Error Handling | error_handler.py | All modules |
| Configuration | config.py | .env file |

---

## 🔄 Data Flow

```
User Input (Upload Document)
         ↓
    Document Loader
         ↓
    Text Chunking
         ↓
    Embedding Manager (Convert to vectors)
         ↓
    Vector Store (Store in DB)
         ↓
    Success Response

---

User Input (Question)
         ↓
    Embedding Manager (Convert question to vector)
         ↓
    Vector Store (Semantic search)
         ↓
    Retrieved Documents
         ↓
    LLM Manager (Generate answer with context)
         ↓
    RAG Pipeline (Format response)
         ↓
    Chat History (Store interaction)
         ↓
    User Response
```

---

## 🚀 Execution Entry Points

### Streamlit Frontend
```bash
cd frontend
streamlit run app.py
```
**Location**: `frontend/app.py`
**Main Class**: RAGPipeline (imported from backend)

### FastAPI Backend
```bash
cd backend
python api.py
```
**Location**: `backend/api.py`
**Port**: 8000
**Endpoints**: /upload, /query, /documents, etc.

### CLI Interface
```bash
python quickstart.py
```
**Location**: `quickstart.py`
**Purpose**: Command-line Q&A interface

### Tests
```bash
python -m pytest backend/test_rag.py
```
**Location**: `backend/test_rag.py`
**Framework**: pytest

---

## 📦 Module Dependencies

```
frontend/app.py
├── rag_pipeline.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   └── config.py
│
backend/api.py
├── rag_pipeline.py
│   └── [same as above]
├── pydantic (BaseModel)
└── fastapi

backend/cache.py
└── config.py

backend/test_rag.py
├── document_loader.py
├── embeddings.py
├── vector_store.py
└── config.py

quickstart.py
├── rag_pipeline.py
│   └── [same as above]
└── config.py
```

---

## ✨ Code Statistics

| Category | Files | Lines of Code |
|----------|-------|---------------|
| Backend Modules | 10 | ~2,000 |
| Frontend | 1 | ~400 |
| Configuration | 1 | ~80 |
| Tests | 1 | ~150 |
| CLI | 1 | ~100 |
| Docker | 2 | ~40 |
| Scripts | 2 | ~50 |
| Documentation | 5 | ~2,000 |
| **Total** | **23** | **~4,820** |

---

## 🔧 Development Workflow

### Adding a Feature

1. **Backend Enhancement**: Edit relevant backend module
2. **Update Configuration**: Add new settings to config.py
3. **Frontend Update**: Modify frontend/app.py
4. **Test**: Run backend/test_rag.py
5. **Documentation**: Update README.md

### Debugging

1. Check logs: `streamlit run app.py --logger.level=debug`
2. View error messages in UI
3. Check error_handler.py for error details
4. Review config.py for settings
5. Check .env for API keys

### Optimization

1. Profile with `cProfile`
2. Review vector_store.py search efficiency
3. Check chunk_size and top_k settings
4. Enable caching in config.py
5. Use faster embedding model

---

## 📋 Checklist for New Users

- [ ] Read README.md for overview
- [ ] Follow INSTALLATION.md for setup
- [ ] Review GETTING_STARTED.md for quick start
- [ ] Check .env.example for available options
- [ ] Run setup.sh or setup.bat
- [ ] Add API keys to .env
- [ ] Upload sample document
- [ ] Test Q&A functionality
- [ ] Review PROJECT_SUMMARY.md for architecture
- [ ] Customize configuration as needed

---

**Complete RAG system ready to use! 🎉**
