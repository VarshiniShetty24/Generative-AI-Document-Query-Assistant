"""
Quick start script for RAG system
"""

import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

from rag_pipeline import RAGPipeline
from config import DOCUMENTS_DIR


def main():
    """Main entry point"""
    print("🚀 RAG System Quick Start")
    print("=" * 50)
    
    # Initialize pipeline
    print("\n📦 Initializing RAG pipeline...")
    rag = RAGPipeline()
    
    # Check for sample documents
    print("\n📁 Checking for documents...")
    docs = rag.get_processed_documents()
    
    if docs:
        print(f"✓ Found {len(docs)} documents loaded")
    else:
        print("⚠️  No documents loaded")
        print(f"   Place documents in: {DOCUMENTS_DIR}")
        print("   Supported formats: PDF, CSV, TXT, MD, DOCX")
    
    # Print system info
    info = rag.get_system_info()
    print("\n📊 System Information:")
    print(f"  LLM Model: {info['llm_model']}")
    print(f"  Embedding Model: {info['embedding_model']}")
    print(f"  Vector Store: {info['vectorstore_info']}")
    
    # Interactive mode
    print("\n💬 Starting interactive mode (type 'exit' to quit)")
    print("=" * 50)
    
    while True:
        try:
            question = input("\n❓ Ask a question: ").strip()
            
            if question.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            if not question:
                print("⚠️  Please enter a question")
                continue
            
            print("\n⏳ Thinking...")
            answer = rag.conversational_query(question)
            print(f"\n✓ Answer:\n{answer}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
