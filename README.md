## Corpus Description

The knowledge source used for this RAG chatbot is a Machine Learning textbook PDF. 
The document contains concepts related to machine learning, including supervised learning, unsupervised learning, feature extraction, and other ML topics.

The PDF is processed by splitting the text into smaller chunks of approximately 500 characters/tokens. These chunks are converted into vector embeddings using the Sentence Transformer model and stored in ChromaDB for efficient retrieval.

## RAG Pipeline

1. User enters a question through the Streamlit interface.
2. The question is converted into an embedding.
3. ChromaDB retrieves the most relevant document chunks.
4. The retrieved context is passed to Llama 3.2 through Ollama.
5. The model generates an answer based only on the provided document context.

## Demo Questions and Answers

### Question 1:
What is unsupervised learning?

### Answer:
Unsupervised learning is a machine learning approach where models learn patterns from data without labeled examples. It includes tasks such as clustering, dimensionality reduction, representation learning, and density estimation.

---

### Question 2:
What is feature extraction?

### Answer:
Feature extraction is the process of transforming raw data into meaningful representations that help machine learning models learn patterns from data.

---

### Question 3:
What are the types of machine learning?

### Answer:
The main types of machine learning are supervised learning, unsupervised learning, and reinforcement learning.

---

## Out-of-Scope Example

### Question:
Who is the Prime Minister of India?

### Answer:
I don't have enough information from the provided document to answer this question.