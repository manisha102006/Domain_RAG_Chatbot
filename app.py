from langchain_ollama import OllamaLLM
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


st.title("📚 Domain RAG Chatbot")


# Load PDF
loader = PyPDFLoader("data/textbook.pdf")
documents = loader.load()


# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(documents)


# Create embeddings
# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load LLM
llm = OllamaLLM(
    model="llama3.2"
)


# Create vector database
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="new_chroma_db"
)


st.success("Document loaded successfully!")


# User question
question = st.text_input("Ask a question from your document")



if question:

    results = vectorstore.similarity_search(
        question,
        k=2
    )

    context = "\n\n".join(
        [result.page_content for result in results]
    )

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = llm.invoke(prompt)

    st.subheader("Answer:")
    st.write(answer)