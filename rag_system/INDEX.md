# 📖 RAG System - Complete Index & Quick Reference

## 🎯 Start Here

**First Time?** → Read in this order:
1. [README.md](README.md) - Overview & features
2. [INSTALLATION.md](INSTALLATION.md) - Setup instructions
3. [GETTING_STARTED.md](GETTING_STARTED.md) - First use

**Want Details?** → Explore:
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Architecture & design
- [FILE_STRUCTURE.md](FILE_STRUCTURE.md) - Code organization
- This file - Navigation & quick reference

---

## 📚 Documentation Guide

### Core Documentation

| Document | Purpose | Read Time | Best For |
|----------|---------|-----------|----------|
| **README.md** | Complete project documentation | 15 min | Overview, features, API docs |
| **GETTING_STARTED.md** | Quick start and feature guide | 10 min | First-time users |
| **INSTALLATION.md** | Detailed installation guide | 20 min | Setup & troubleshooting |
| **PROJECT_SUMMARY.md** | Architecture & design overview | 15 min | Understanding the system |
| **FILE_STRUCTURE.md** | Code organization reference | 10 min | Finding code |
| **This file** | Index & quick reference | 5 min | Navigation |

---

## 🚀 Quick Start (Choose Your Path)

### Path 1: Windows Users (Fastest)
```batch
1. setup.bat                          # Automated setup
2. Edit .env with API keys
3. cd frontend && streamlit run app.py
4. Open http://localhost:8501
```

### Path 2: Linux/Mac Users
```bash
1. bash setup.sh                      # Automated setup
2. nano .env && add API keys
3. source venv/bin/activate
4. cd frontend && streamlit run app.py
5. Open http://localhost:8501
```

### Path 3: Docker Users
```bash
1. cp .env.example .env               # Configure
2. docker-compose up                  # Start
3. Open http://localhost:8501
```

### Path 4: Manual Setup
```bash
1. python -m venv venv
2. source venv/bin/activate  # or venv\Scripts\activate (Windows)
3. pip install -r requirements.txt
4. cp .env.example .env && edit .env
5. mkdir -p data/documents data/vectorstore
6. cd frontend && streamlit run app.py
```

---

## 📂 File Structure Quick Reference

```
rag_system/
│
├── 📄 Documentation
│   ├── README.md              ← Start here!
│   ├── GETTING_STARTED.md     ← Quick guide
│   ├── INSTALLATION.md        ← Setup help
│   ├── PROJECT_SUMMARY.md     ← Architecture
│   ├── FILE_STRUCTURE.md      ← Code map
│   └── INDEX.md               ← This file
│
├── 🔧 Setup & Config
│   ├── .env.example           ← Config template
│   ├── requirements.txt       ← Python packages
│   ├── setup.bat              ← Windows setup
│   └── setup.sh               ← Linux/Mac setup
│
├── 🐳 Docker
│   ├── Dockerfile             ← Container image
│   └── docker-compose.yml     ← Services config
│
├── 🐍 Backend (Python)
│   └── backend/
│       ├── config.py          ← Settings
│       ├── document_loader.py ← PDF/CSV/TXT handling
│       ├── embeddings.py      ← Vector embeddings
│       ├── vector_store.py    ← Vector database (Chroma/FAISS)
│       ├── llm.py             ← LLM interactions
│       ├── rag_pipeline.py    ← Main orchestration
│       ├── cache.py           ← Caching layer
│       ├── error_handler.py   ← Error management
│       ├── api.py             ← REST API (FastAPI)
│       └── test_rag.py        ← Unit tests
│
├── 🎨 Frontend (Streamlit)
│   └── frontend/
│       └── app.py             ← Web UI
│
├── 💾 Data Storage
│   └── data/
│       ├── documents/         ← Your uploaded files
│       ├── vectorstore/       ← Embeddings database
│       └── cache/             ← Cache files
│
└── 🚀 Scripts
    ├── quickstart.py          ← CLI interface
    └── run.py                 ← (Optional) Main entry point
```

---

## 🔍 Finding What You Need

### "How do I..."

| Question | Answer | Location |
|----------|--------|----------|
| Install the system? | INSTALLATION.md | [Link](INSTALLATION.md) |
| Get started quickly? | GETTING_STARTED.md | [Link](GETTING_STARTED.md) |
| Configure settings? | .env.example + INSTALLATION.md | [Link](.env.example) |
| Use the API? | backend/api.py + README.md | [Link](backend/api.py) |
| Understand architecture? | PROJECT_SUMMARY.md | [Link](PROJECT_SUMMARY.md) |
| Find code modules? | FILE_STRUCTURE.md | [Link](FILE_STRUCTURE.md) |
| Get API keys? | INSTALLATION.md | [Link](INSTALLATION.md#getting-api-keys) |
| Deploy to production? | README.md - Deployment section | [Link](README.md#deployment) |
| Troubleshoot issues? | INSTALLATION.md - Troubleshooting | [Link](INSTALLATION.md#troubleshooting) |
| Run tests? | backend/test_rag.py | [Link](backend/test_rag.py) |
| Use CLI? | quickstart.py | [Link](quickstart.py) |

---

## 🎯 Common Tasks

### Setup
```bash
# Windows
setup.bat

# Linux/Mac
bash setup.sh

# Manual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Configuration
```bash
# Edit settings
nano .env          # Linux/Mac
notepad .env       # Windows

# Key settings to update:
# - OPENAI_API_KEY=sk-...
# - LLM_MODEL=gpt-3.5-turbo
# - EMBEDDING_MODEL=text-embedding-3-small
```

### Run Application
```bash
# Streamlit (Web)
cd frontend
streamlit run app.py

# FastAPI (REST)
cd backend
python api.py

# CLI
python quickstart.py
```

### Upload Documents
1. Open http://localhost:8501
2. Click "📤 Upload Documents" in sidebar
3. Select PDF/CSV/TXT/MD/DOCX files
4. Wait for processing

### Ask Questions
1. Type question in chat
2. Press Enter or click Send
3. View AI response with sources
4. Continue conversation with context

### Check System Info
1. Select "System Info" mode
2. View documents processed
3. Check models in use
4. Review chat history

---

## 🔑 Environment Variables

### Essential
```env
OPENAI_API_KEY=sk-...           # Required for GPT models
HF_API_TOKEN=hf_...             # Required for HF models
```

### Models
```env
LLM_MODEL=gpt-3.5-turbo         # or gpt-4
EMBEDDING_MODEL=text-embedding-3-small
VECTORSTORE_TYPE=chroma         # or faiss
```

### Processing
```env
CHUNK_SIZE=1024
CHUNK_OVERLAP=256
MAX_FILE_SIZE_MB=50
```

### Retrieval
```env
TOP_K_RESULTS=5
SIMILARITY_THRESHOLD=0.3
```

### Chat
```env
MAX_HISTORY=10
CONTEXT_WINDOW=3000
```

### Performance
```env
USE_CACHE=true
CACHE_TTL=3600
```

See [.env.example](.env.example) for all options.

---

## 🐍 Python Module Reference

### Core Modules

**config.py**
```python
from config import (
    CHUNK_SIZE, CHUNK_OVERLAP,      # Processing
    TOP_K_RESULTS, SIMILARITY_THRESHOLD,  # Retrieval
    LLM_MODEL, EMBEDDING_MODEL,     # Models
    DOCUMENTS_DIR, VECTORSTORE_DIR  # Paths
)
```

**document_loader.py**
```python
from document_loader import DocumentLoader
loader = DocumentLoader()
chunks, name = loader.load_documents("file.pdf")
```

**embeddings.py**
```python
from embeddings import EmbeddingManager
embedder = EmbeddingManager()
vector = embedder.embed_text("text")
vectors = embedder.embed_documents(["text1", "text2"])
```

**vector_store.py**
```python
from vector_store import VectorStoreManager
vs = VectorStoreManager(embedder)
vs.create_vectorstore(chunks, "doc_name")
results = vs.search("query", k=5)
```

**llm.py**
```python
from llm import LLMManager
llm = LLMManager()
answer = llm.generate_answer("question", "context")
```

**rag_pipeline.py**
```python
from rag_pipeline import RAGPipeline
rag = RAGPipeline()
rag.ingest_document("file.pdf")
answer = rag.query("question")
history = rag.get_chat_history()
```

---

## 🔗 API Endpoints Reference

### REST API (backend/api.py)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/upload` | Upload document |
| POST | `/query` | Ask question |
| GET | `/documents` | List documents |
| GET | `/history` | Get chat history |
| DELETE | `/history` | Clear history |
| GET | `/system-info` | System stats |
| GET | `/health` | Health check |

### Examples

```bash
# Upload
curl -X POST "http://localhost:8000/upload" \
  -F "file=@document.pdf"

# Query
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this about?"}'

# Get documents
curl "http://localhost:8000/documents"
```

---

## 📊 Performance Tips

### For Speed
```env
CHUNK_SIZE=512
TOP_K_RESULTS=3
EMBEDDING_MODEL=text-embedding-3-small
VECTORSTORE_TYPE=faiss
```

### For Accuracy
```env
CHUNK_SIZE=1024
TOP_K_RESULTS=5
EMBEDDING_MODEL=text-embedding-3-large
LLM_MODEL=gpt-4
```

### For Low Cost
```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
VECTORSTORE_TYPE=faiss
USE_CACHE=true
CACHE_TTL=7200
```

---

## 🐛 Troubleshooting Quick Reference

| Issue | Solution | Docs |
|-------|----------|------|
| "API key required" | Add to .env | [INSTALLATION.md](INSTALLATION.md#getting-api-keys) |
| "Module not found" | Run setup.bat/setup.sh | [INSTALLATION.md](INSTALLATION.md) |
| Slow responses | Reduce CHUNK_SIZE | [INSTALLATION.md](INSTALLATION.md#performance-optimization) |
| Memory error | Reduce MAX_HISTORY | [INSTALLATION.md](INSTALLATION.md#runtime-issues) |
| Port in use | Use different port | [INSTALLATION.md](INSTALLATION.md#port-already-in-use) |
| FAISS error | pip install faiss-cpu | [INSTALLATION.md](INSTALLATION.md) |

---

## 🚀 Deployment Paths

### Development
```bash
streamlit run frontend/app.py
```

### Testing
```bash
python -m pytest backend/test_rag.py
```

### Local API
```bash
python backend/api.py
```

### Docker
```bash
docker-compose up
```

### Production
See README.md - Deployment section for:
- Nginx reverse proxy setup
- Gunicorn/Uvicorn deployment
- Kubernetes configuration
- Security best practices

---

## 📚 Learning Resources

### Key Concepts to Understand
1. **Embeddings**: Converting text to vectors
2. **Vector Search**: Finding similar documents
3. **RAG**: Combining retrieval + generation
4. **Chunking**: Splitting text for processing
5. **Prompting**: Crafting effective prompts

### Documentation to Read
1. **For Overview**: README.md
2. **For Setup**: INSTALLATION.md
3. **For Quick Start**: GETTING_STARTED.md
4. **For Architecture**: PROJECT_SUMMARY.md
5. **For Code**: FILE_STRUCTURE.md

### Code to Explore
1. **Main Logic**: backend/rag_pipeline.py
2. **Web Interface**: frontend/app.py
3. **REST API**: backend/api.py
4. **Tests**: backend/test_rag.py

---

## ✅ Checklist for Success

### Initial Setup
- [ ] Read README.md
- [ ] Run setup script
- [ ] Add API keys to .env
- [ ] Verify installation (run setup.bat/setup.sh)
- [ ] Start application
- [ ] Upload sample document

### First Use
- [ ] Ask test question
- [ ] Check response quality
- [ ] Try multi-document queries
- [ ] Review chat history
- [ ] Check system info

### Customization
- [ ] Adjust CHUNK_SIZE
- [ ] Tune TOP_K_RESULTS
- [ ] Select better LLM if needed
- [ ] Enable caching for performance
- [ ] Configure retention policies

### Production
- [ ] Setup Docker deployment
- [ ] Configure reverse proxy
- [ ] Add authentication
- [ ] Enable monitoring
- [ ] Setup backups
- [ ] Document custom config

---

## 🎓 Next Steps

1. ✅ **Setup**: Follow INSTALLATION.md
2. ✅ **Learn**: Read GETTING_STARTED.md
3. ✅ **Explore**: Test features in UI
4. ✅ **Understand**: Review PROJECT_SUMMARY.md
5. ⬜ **Customize**: Adjust .env settings
6. ⬜ **Integrate**: Use REST API
7. ⬜ **Deploy**: Use Docker + production setup
8. ⬜ **Scale**: Monitor and optimize

---

## 🆘 Getting Help

### Resources
- Documentation files in this directory
- Code comments and docstrings
- Unit tests for examples
- Error messages in logs

### Debugging
```bash
# Enable debug logging
streamlit run frontend/app.py --logger.level=debug

# Check API logs
python backend/api.py

# Run tests
python -m pytest backend/test_rag.py -v
```

### Common Issues
See [INSTALLATION.md - Troubleshooting](INSTALLATION.md#troubleshooting)

---

## 📞 Support & Resources

- **Docs**: All .md files in project root
- **Code**: See FILE_STRUCTURE.md
- **Examples**: quickstart.py and test_rag.py
- **Config**: .env.example
- **Tests**: backend/test_rag.py

---

## 🎉 You're Ready!

Everything is set up and documented. Start with:

1. **INSTALLATION.md** for setup
2. **GETTING_STARTED.md** for first use
3. **README.md** for complete reference

Happy document querying! 🚀

---

**Last Updated**: March 28, 2024
**Version**: 1.0.0
**Status**: Production Ready ✅
