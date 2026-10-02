from langchain_ollama.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from typing import List
from chroma_utils import vectorstore
from langchain_core.documents import Document
import os

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
output_parser = StrOutputParser()

contextualize_q_system_prompt = """
Given a conversation history and the latest user query, 
generate a contextualized question that incorporates relevant information from the conversation history. 
The contextualized question should be clear, concise, and provide enough context for the model to understand the user's 
intent. If the latest user query is already clear and does not require additional context, return it as is.
"""

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ('system',contextualize_q_system_prompt),
        (MessagesPlaceholder("chat_history")),
        ('human',"{input}")
    ]
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful assistant, Use the following context to answer the user's question."),
        ('system', "Context: {context}"),
        MessagesPlaceholder('chat_history'),
        ('human','{input}')
    ]
)

def get_rag_chain(model="mistral:7b"):
    llm = ChatOllama(model=model)
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)    
    return rag_chain


