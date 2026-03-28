import logging
from typing import List, Optional
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import LLM_MODEL, OPENAI_API_KEY, HF_API_TOKEN, CONTEXT_WINDOW

logger = logging.getLogger(__name__)


class LLMManager:
    """Manage LLM interactions"""
    
    def __init__(self, model: str = LLM_MODEL):
        self.model = model
        self.llm = self._initialize_llm()
        self.qa_prompt = self._create_qa_prompt()
    
    def _initialize_llm(self):
        """Initialize LLM based on model choice"""
        if "gpt" in self.model.lower():
            if not OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is required for GPT models")
            logger.info(f"Initializing OpenAI LLM: {self.model}")
            return ChatOpenAI(
                model_name=self.model,
                openai_api_key=OPENAI_API_KEY,
                temperature=0.7,
                max_tokens=1000
            )
        else:
            if not HF_API_TOKEN:
                raise ValueError("HF_API_TOKEN is required for HuggingFace models")
            logger.info(f"Initializing HuggingFace LLM: {self.model}")
            return HuggingFaceHub(
                repo_id=self.model,
                huggingfacehub_api_token=HF_API_TOKEN,
                model_kwargs={"temperature": 0.7, "max_new_tokens": 1000}
            )
    
    def _create_qa_prompt(self) -> PromptTemplate:
        """Create prompt template for QA"""
        template = """You are a helpful assistant answering questions based on provided context.

Context:
{context}

Question: {question}

Please provide a comprehensive answer based on the context above. If the context doesn't contain enough information to answer the question, say so and provide your best general knowledge response.

Answer:"""
        
        return PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )
    
    def generate_answer(self, question: str, context: str) -> str:
        """Generate answer based on question and context"""
        try:
            # Truncate context if too long
            if len(context) > CONTEXT_WINDOW:
                context = context[:CONTEXT_WINDOW] + "..."
            
            # Create chain
            chain = LLMChain(llm=self.llm, prompt=self.qa_prompt)
            
            # Generate response
            response = chain.run(context=context, question=question)
            logger.info("Answer generated successfully")
            return response.strip()
        except Exception as e:
            logger.error(f"Error generating answer: {e}")
            return f"Error generating answer: {str(e)}"
    
    def refine_answer(self, question: str, context: str, previous_answer: str) -> str:
        """Refine answer based on previous response"""
        refinement_template = """You are a helpful assistant. Based on the context and previous answer, provide a refined response.

Context:
{context}

Question: {question}

Previous Answer:
{previous_answer}

Please provide a more accurate or refined answer if possible.

Refined Answer:"""
        
        prompt = PromptTemplate(
            input_variables=["context", "question", "previous_answer"],
            template=refinement_template
        )
        
        try:
            chain = LLMChain(llm=self.llm, prompt=prompt)
            response = chain.run(
                context=context,
                question=question,
                previous_answer=previous_answer
            )
            return response.strip()
        except Exception as e:
            logger.error(f"Error refining answer: {e}")
            return previous_answer
