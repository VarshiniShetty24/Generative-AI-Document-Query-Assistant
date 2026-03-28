import streamlit as st
import sys
from pathlib import Path
import json
import tempfile
from datetime import datetime

# Add backend to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from rag_pipeline import RAGPipeline

# Page configuration
st.set_page_config(
    page_title="RAG Document QA System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #f5f5f5;
    }
    .stTitle {
        color: #2c3e50;
        text-align: center;
    }
    .stSubheader {
        color: #34495e;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .assistant-message {
        background-color: #f1f8e9;
        border-left: 4px solid #4caf50;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "rag_pipeline" not in st.session_state:
    st.session_state.rag_pipeline = RAGPipeline()

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Header
st.markdown("# 📚 RAG Document QA System")
st.markdown("*Semantic Question Answering over PDFs, CSVs, and Text Documents*")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Mode selection
    mode = st.radio(
        "Select Mode:",
        ["Chat", "Document Management", "System Info"]
    )
    
    st.markdown("---")
    
    # Document Upload
    if mode == "Document Management":
        st.subheader("📤 Upload Documents")
        uploaded_files = st.file_uploader(
            "Choose files to upload",
            type=["pdf", "csv", "txt", "md", "docx"],
            accept_multiple_files=True,
            help="Supported formats: PDF, CSV, TXT, MD, DOCX"
        )
        
        if uploaded_files:
            for uploaded_file in uploaded_files:
                with st.spinner(f"Processing {uploaded_file.name}..."):
                    try:
                        # Save temporary file
                        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
                            tmp_file.write(uploaded_file.getbuffer())
                            tmp_path = tmp_file.name
                        
                        # Ingest document
                        success, message = st.session_state.rag_pipeline.ingest_document(tmp_path)
                        
                        if success:
                            st.success(message)
                        else:
                            st.error(f"Failed to process {uploaded_file.name}: {message}")
                    except Exception as e:
                        st.error(f"Error processing {uploaded_file.name}: {str(e)}")

# Main content
if mode == "Chat":
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.markdown("### 📋 Documents Loaded")
        docs = st.session_state.rag_pipeline.get_processed_documents()
        if docs:
            for doc in docs:
                st.write(f"✓ {doc}")
        else:
            st.info("No documents loaded yet")
        
        if st.button("Clear Chat History", key="clear_history"):
            st.session_state.rag_pipeline.clear_chat_history()
            st.session_state.chat_messages = []
            st.success("Chat history cleared")
    
    with col1:
        st.markdown("### 💬 Conversation")
        
        # Display chat history
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.chat_messages:
                if message["role"] == "user":
                    st.markdown(f"<div class='user-message'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='assistant-message'><b>Assistant:</b> {message['content']}</div>", unsafe_allow_html=True)
        
        # Input area
        st.markdown("---")
        col_input, col_button = st.columns([4, 1])
        
        with col_input:
            user_input = st.text_input("Ask a question:", key="user_input", placeholder="Enter your question here...")
        
        with col_button:
            send_button = st.button("Send", key="send_button", use_container_width=True)
        
        # Process input
        if send_button and user_input:
            # Add user message to history
            st.session_state.chat_messages.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now().isoformat()
            })
            
            # Generate response
            with st.spinner("Thinking..."):
                response = st.session_state.rag_pipeline.conversational_query(user_input)
            
            # Add assistant message to history
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().isoformat()
            })
            
            # Rerun to display new messages
            st.rerun()

elif mode == "Document Management":
    st.header("📄 Document Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Processed Documents")
        docs = st.session_state.rag_pipeline.get_processed_documents()
        if docs:
            for i, doc in enumerate(docs, 1):
                st.write(f"{i}. {doc}")
        else:
            st.info("No documents have been processed yet. Upload documents from the sidebar.")
    
    with col2:
        st.subheader("System Status")
        info = st.session_state.rag_pipeline.get_system_info()
        st.metric("Documents Processed", info["documents_processed"])
        st.metric("Chat History Length", info["chat_history_length"])
        
        # Vectorstore info
        vs_info = info["vectorstore_info"]
        st.json(vs_info)

elif mode == "System Info":
    st.header("ℹ️ System Information")
    
    info = st.session_state.rag_pipeline.get_system_info()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Documents Processed", info["documents_processed"])
    
    with col2:
        st.metric("Embedding Model", info["embedding_model"].split("/")[-1] if "/" in info["embedding_model"] else info["embedding_model"])
    
    with col3:
        st.metric("LLM Model", info["llm_model"])
    
    st.markdown("---")
    
    with st.expander("Detailed System Info"):
        st.json(info)
    
    # Chat history details
    if st.session_state.chat_messages:
        st.markdown("### Chat History")
        with st.expander("View Chat History"):
            for i, msg in enumerate(st.session_state.chat_messages, 1):
                st.write(f"**{i}. [{msg['role'].upper()}]** {msg['timestamp']}")
                st.write(f"> {msg['content']}")
                st.divider()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>RAG Document QA System | Built with Streamlit, LangChain, and OpenAI</p>
</div>
""", unsafe_allow_html=True)
