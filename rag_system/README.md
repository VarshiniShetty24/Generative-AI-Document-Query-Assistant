# RAG Document QA System

A complete Retrieval-Augmented Generation (RAG) system for semantic question answering over PDFs, CSVs, and text documents.

## Features

✨ **Document Processing**
- Support for multiple file formats: PDF, CSV, TXT, MD, DOCX
- Intelligent text chunking with configurable overlap
- Automatic metadata extraction

🔍 **Semantic Retrieval**
- FAISS and ChromaDB vector database support
- OpenAI and HuggingFace embedding models
- Similarity-based document retrieval with configurable thresholds

🤖 **LLM Integration**
- Support for OpenAI GPT models
- HuggingFace model support
- Context-aware question answering

💬 **Interactive UI**
- Clean Streamlit web interface
- Real-time document upload and processing
- Conversational chat with history
- Document management dashboard
- System information and monitoring

⚙️ **Configuration**
- Environment variable configuration
- Flexible model selection
- Customizable retrieval parameters
- Caching support

## Project Structure

```
rag_system/
├── backend/
│   ├── config.py              # Configuration management
│   ├── document_loader.py     # Document loading and parsing
│   ├── embeddings.py          # Embedding management
│   ├── vector_store.py        # Vector database management
│   ├── llm.py                 # LLM interactions
│   └── rag_pipeline.py        # Main RAG orchestration
├── frontend/
│   └── app.py                 # Streamlit web application
├── data/
│   ├── documents/             # Uploaded documents
│   └── vectorstore/           # Vector database storage
├── .env.example               # Environment variables template
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (for GPT models)
- Or HuggingFace API token (for HF models)

### Setup Steps

1. **Clone or create the project directory:**
```bash
cd rag_system
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys
# OPENAI_API_KEY=your_key_here
# HF_API_TOKEN=your_token_here
```

## Configuration

Edit `.env` file to customize:

```env
# API Keys
OPENAI_API_KEY=your_openai_api_key
HF_API_TOKEN=your_huggingface_token

# Models
LLM_MODEL=gpt-3.5-turbo              # or gpt-4, meta-llama/Llama-2-7b, etc.
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database (chroma or faiss)
VECTORSTORE_TYPE=chroma

# Processing
CHUNK_SIZE=1024                       # Characters per chunk
CHUNK_OVERLAP=256                     # Overlap between chunks
MAX_FILE_SIZE_MB=50                   # Maximum file size

# Retrieval
TOP_K_RESULTS=5                       # Number of documents to retrieve
SIMILARITY_THRESHOLD=0.3              # Minimum similarity score

# Chat
MAX_HISTORY=10                        # Messages to keep in memory
CONTEXT_WINDOW=3000                   # Max context length for LLM
```

## Usage

### Starting the Application

```bash
# Navigate to the frontend directory
cd frontend

# Run the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Main Features

#### 1. **Chat Mode**
- Upload documents from the sidebar
- Ask questions about your documents
- Maintains conversation history
- View loaded documents

#### 2. **Document Management**
- Upload multiple documents (PDF, CSV, TXT, MD, DOCX)
- View processing status
- Track ingested documents
- Manage vectorstore

#### 3. **System Info**
- View system statistics
- Monitor document processing
- Check active models
- Review chat history

## API Usage (Backend)

### Python Integration

```python
from rag_pipeline import RAGPipeline

# Initialize pipeline
rag = RAGPipeline()

# Ingest document
success, message = rag.ingest_document("path/to/document.pdf")

# Query
answer = rag.query("What is the main topic?")

# Conversational query (uses history)
answer = rag.conversational_query("Tell me more about this")

# Get processed documents
docs = rag.get_processed_documents()

# Get system info
info = rag.get_system_info()
```

## Performance Optimization

### Tips for Better Performance

1. **Chunk Size Selection**
   - Smaller chunks (512-768): Better precision, more chunks
   - Larger chunks (1024-2048): Faster processing, broader context

2. **Embedding Models**
   - text-embedding-3-small: Fast, cost-effective
   - text-embedding-3-large: Better accuracy
   - all-MiniLM-L6-v2: Free, runs locally

3. **Vector Database**
   - Chroma: Better for persistence and updates
   - FAISS: Better for large-scale retrieval

4. **LLM Selection**
   - gpt-3.5-turbo: Fast, cost-effective
   - gpt-4: Higher accuracy, slower, more expensive
   - Open source: Free but requires setup

## Troubleshooting

### Common Issues

**Issue: "OPENAI_API_KEY is required"**
- Solution: Add your OpenAI API key to `.env` file

**Issue: "No relevant documents found"**
- Solution: Upload documents first or adjust similarity threshold

**Issue: Slow performance**
- Solution: Reduce CHUNK_SIZE or use faster embedding model

**Issue: Out of memory**
- Solution: Reduce MAX_HISTORY or use smaller embedding model

## Advanced Features

### Custom Prompts
Edit the prompt templates in `backend/llm.py` for domain-specific responses.

### Caching
Enable caching in `.env` for faster repeated queries:
```env
USE_CACHE=true
CACHE_TTL=3600  # 1 hour
```

### Batch Processing
Process multiple documents:
```python
from pathlib import Path
from rag_pipeline import RAGPipeline

rag = RAGPipeline()
doc_dir = Path("path/to/documents")

for doc_file in doc_dir.glob("*.pdf"):
    rag.ingest_document(str(doc_file))
```

## Security Best Practices

1. **Never commit .env file** - Use `.env.example` as template
2. **Use environment variables** for all sensitive data
3. **Validate file uploads** - Size and type checking included
4. **Rate limiting** - Implement in production deployment
5. **Authentication** - Add user authentication for web deployment

## Deployment

### Using Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "frontend/app.py"]
```

Build and run:
```bash
docker build -t rag-system .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key rag-system
```

### Using Streamlit Cloud

1. Push to GitHub
2. Connect at https://share.streamlit.io
3. Add environment secrets in settings

## Contributing

Feel free to contribute! Areas for improvement:
- [ ] Additional document formats (Excel, JSON, HTML)
- [ ] Multi-language support
- [ ] Custom fine-tuning
- [ ] API endpoint exposure
- [ ] Database persistence for chat history
- [ ] Advanced retrieval (BM25 hybrid search)

## License

MIT License - feel free to use for personal and commercial projects.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review configuration settings
3. Check API key validity
4. Review logs for detailed error messages

## Changelog

### v1.0.0 (Initial Release)
- Document ingestion (PDF, CSV, TXT, MD, DOCX)
- FAISS and ChromaDB support
- OpenAI and HuggingFace integration
- Streamlit web interface
- Conversation history
- System monitoring

---

**Happy questioning! 🚀**
