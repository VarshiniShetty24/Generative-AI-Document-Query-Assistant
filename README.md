# 📄 Generative AI Document Query Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** application that enables users to upload documents and ask natural language questions. The system retrieves the most relevant document chunks using vector embeddings and generates accurate, context-aware responses using Large Language Models (LLMs).

---

## 🚀 Features

- 📂 Upload PDF, DOCX and TXT documents
- 🔍 Semantic document search using vector embeddings
- 🤖 AI-powered question answering
- 📑 Retrieval-Augmented Generation (RAG)
- 💬 Interactive Streamlit chat interface
- ⚡ FastAPI REST API support
- 🗂️ Vector database using FAISS / ChromaDB
- 🧠 LangChain-powered document retrieval pipeline
- 🐳 Docker support for deployment
- 📈 Modular backend architecture

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| Framework | LangChain |
| LLM | OpenAI GPT |
| Vector Database | FAISS / ChromaDB |
| Embedding Model | Sentence Transformers |
| Document Processing | PyPDF2, python-docx, pandas |
| API Testing | FastAPI Docs (Swagger) |
| Deployment | Docker |

---

# 📂 Project Structure

```
Generative-AI-Document-Query-Assistant
│
├── rag_system
│   ├── backend
│   │   ├── api.py
│   │   ├── rag_pipeline.py
│   │   ├── document_loader.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── llm.py
│   │   ├── cache.py
│   │   ├── config.py
│   │   └── error_handler.py
│   │
│   ├── frontend
│   │   └── app.py
│   │
│   ├── data
│   │   └── documents
│   │
│   ├── requirements.txt
│   ├── docker-compose.yml
│   └── Dockerfile
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/VarshiniShetty24/Generative-AI-Document-Query-Assistant.git

cd Generative-AI-Document-Query-Assistant/rag_system
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file

```
OPENAI_API_KEY=your_api_key
```

---

# ▶️ Run Streamlit Application

```bash
streamlit run frontend/app.py
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn backend.api:app --reload
```

---

# 🌐 API Documentation

Once the FastAPI server is running, visit

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will be available.

---

# 🔄 System Workflow

```
User Uploads Document
          │
          ▼
Document Loader
          │
          ▼
Text Chunking
          │
          ▼
Embedding Generation
          │
          ▼
Vector Database (FAISS/ChromaDB)
          │
          ▼
User Question
          │
          ▼
Similarity Search
          │
          ▼
Relevant Chunks Retrieved
          │
          ▼
OpenAI LLM
          │
          ▼
Context-Aware Answer
```

---

# 🧠 RAG Architecture

```
             User
               │
               ▼
      Streamlit Frontend
               │
               ▼
         FastAPI Backend
               │
               ▼
        RAG Pipeline
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
Document Loader    User Query
      │                 │
      └──────┬──────────┘
             ▼
     Embedding Model
             │
             ▼
      Vector Database
             │
             ▼
     Relevant Chunks
             │
             ▼
        OpenAI GPT
             │
             ▼
      Generated Answer
```

---

# 📌 Supported File Formats

- PDF
- DOCX
- TXT

---

# 📡 REST API Endpoints

## Health Check

```
GET /
```

---

## Upload Document

```
POST /upload
```

---

## Ask Question

```
POST /query
```

Example Request

```json
{
    "question":"Explain Retrieval-Augmented Generation"
}
```

Example Response

```json
{
    "answer":"Retrieval-Augmented Generation combines information retrieval with Large Language Models..."
}
```

---

# 🎯 Key Features

- Semantic Search
- Retrieval-Augmented Generation
- Context-aware responses
- Document chunking
- Embedding generation
- Vector similarity search
- Chat history support
- FastAPI REST APIs
- Streamlit UI
- Docker deployment

---

# 🔮 Future Enhancements

- Multi-document conversations
- Authentication and user management
- OCR support for scanned PDFs
- Voice-based document querying
- Cloud deployment (AWS/Azure/GCP)
- Support for local LLMs (Llama, Mistral)
- Conversation memory using LangChain

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Document Upload
- Chat Interface
- FastAPI Swagger UI

---

# 👩‍💻 Author

**Varshini Shetty**

GitHub: https://github.com/VarshiniShetty24

LinkedIn: *(Add your LinkedIn profile here)*

---

# ⭐ If you found this project useful, consider giving it a Star!
