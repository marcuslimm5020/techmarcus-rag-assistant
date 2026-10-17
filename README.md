# TechMarcus — AI Customer Support Assistant

TechMarcus is a Retrieval-Augmented Generation (RAG) customer support assistant built for a fictional consumer electronics company. It uses a company knowledge base to answer customer questions about products, troubleshooting, and support policies.

The project demonstrates how Large Language Models (LLMs), semantic search, and document retrieval can be combined to build a practical AI application.

## Features

- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from a knowledge base before generating answers.
- **Semantic Search:** Finds relevant document content based on the meaning of a customer's question.
- **Hybrid Retrieval:** Combines semantic similarity and keyword matching to improve retrieval relevance.
- **Grounded Responses:** Instructs the model to answer using the available knowledge base rather than inventing unsupported information.
- **Customer Support Use Cases:** Supports product questions, troubleshooting, and policy-related queries.
- **Interactive Web Interface:** Provides a conversational interface built with Streamlit.
- **Local LLM Inference:** Uses Ollama with Llama 3.2 3B for local inference.

## Technology Stack

- Python
- Streamlit
- Ollama
- Llama 3.2 3B
- ChromaDB
- Sentence Transformers
- PyPDF

## Architecture

1. **Document ingestion:** Extract text from the PDF knowledge base.
2. **Text processing:** Split the extracted text into smaller chunks.
3. **Vector storage:** Generate embeddings and store document chunks in ChromaDB.
4. **Retrieval:** Retrieve relevant chunks using semantic similarity and keyword matching.
5. **Response generation:** Pass the retrieved context and customer question to the LLM.
6. **User interface:** Display the generated response in the Streamlit application.

## Project Structure

```text
techmarcus-rag-assistant/
├── app.py
├── requirements.txt
├── data/
│   └── TechMarcus_Knowledge_Base.pdf
├── src/
│   ├── document_loader.py
│   ├── process_documents.py
│   ├── rag_pipeline.py
│   ├── text_splitter.py
│   └── vector_store.py
├── tests/
│   └── test_rag_pipeline.py
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.9 or a compatible Python version
- Ollama
- Git

### 1. Clone the repository

```bash
git clone https://github.com/marcuslimm5020/techmarcus-rag-assistant.git
cd techmarcus-rag-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install and start the local language model

Install Ollama from [ollama.com](https://ollama.com/), then run:

```bash
ollama pull llama3.2:3b
```

### 5. Build the vector database

Follow the project's document-processing workflow to create the local ChromaDB vector store:

```bash
python -m src.vector_store
```

### 6. Launch the application

```bash
streamlit run app.py
```

## Current Status

- Local RAG application implemented and tested.
- Source code and knowledge base published on GitHub.
- Cloud deployment is a planned next step.

## Future Improvements

- Deploy the application to a cloud hosting platform.
- Evaluate retrieval quality using a dedicated test dataset.
- Add automated evaluation for answer relevance and groundedness.
- Improve document ingestion and knowledge-base management.
- Add monitoring for latency and retrieval performance.

## Disclaimer

TechMarcus is a portfolio project using a fictional consumer electronics company and sample support documentation. It is intended for educational and demonstration purposes.
