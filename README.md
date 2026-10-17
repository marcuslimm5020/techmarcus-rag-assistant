# TechMarcus — AI Customer Support Assistant

TechMarcus is a local AI-powered customer support assistant built using **Retrieval-Augmented Generation (RAG)**. Designed for a fictional consumer electronics company, it answers customer questions using information retrieved from a dedicated support knowledge base.

The project demonstrates how document processing, semantic search, vector databases, and Large Language Models (LLMs) can work together to build a practical AI application.

## Project Objectives

- Build a functional AI customer support assistant using a real-world-inspired use case.
- Retrieve relevant information from company documentation before generating answers.
- Improve retrieval relevance by combining semantic similarity with keyword matching.
- Reduce unsupported responses by grounding the LLM in retrieved knowledge.
- Run the application locally using open-source tools, without requiring a paid LLM API.

## Key Features

- **Retrieval-Augmented Generation (RAG):** Retrieves relevant knowledge-base content to provide context for answer generation.
- **Document Processing:** Extracts and splits PDF documentation into manageable text chunks.
- **Vector Search:** Uses embeddings and ChromaDB to find semantically relevant information.
- **Hybrid Retrieval:** Combines semantic similarity and keyword matching to improve retrieval relevance.
- **Grounded Responses:** Instructs the language model to answer using the available knowledge base and handle questions when supporting information is missing.
- **Interactive Chat Interface:** Provides a conversational interface built with Streamlit.
- **Local LLM Inference:** Uses Ollama to run Llama 3.2 3B locally.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive user interface |
| Ollama | Local LLM inference |
| Llama 3.2 3B | Response generation |
| ChromaDB | Vector storage and retrieval |
| Sentence Transformers | Text embeddings |
| PyPDF | PDF text extraction |
| Pytest | Automated testing |

## System Architecture

```text
PDF Knowledge Base
        |
        v
Document Text Extraction
        |
        v
Text Chunking
        |
        v
Embedding Generation
        |
        v
ChromaDB Vector Store
        |
        v
Customer Question
        |
        v
Hybrid Retrieval
(Semantic + Keyword Matching)
        |
        v
Relevant Context + Question
        |
        v
Ollama — Llama 3.2 3B
        |
        v
Grounded Answer in Streamlit
```

## How It Works

1. **Document ingestion:** Extract text from the customer support PDF.
2. **Text chunking:** Divide the extracted text into smaller sections suitable for retrieval.
3. **Embedding and indexing:** Convert text chunks into vector embeddings and store them in ChromaDB.
4. **Question processing:** Receive a customer question through the Streamlit interface.
5. **Context retrieval:** Combine semantic similarity and keyword matching to identify relevant document chunks.
6. **Answer generation:** Provide the retrieved context and customer question to Llama 3.2 3B through Ollama.
7. **Response grounding:** Instruct the model to answer using the retrieved information and indicate when the knowledge base does not contain sufficient information.

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

The local `.venv/` environment and generated `chroma_db/` database are excluded from version control.

## Getting Started

### Prerequisites

- Python 3.9 or a compatible Python version
- [Ollama](https://ollama.com/)
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

### 4. Download the language model

Install Ollama, then download Llama 3.2 3B:

```bash
ollama pull llama3.2:3b
```

Ensure the Ollama service is running before using the application.

### 5. Build the vector database

Generate the local vector store from the knowledge-base documents:

```bash
python -m src.vector_store
```

Run this step when setting up the project for the first time or when rebuilding the index after changing the knowledge base.

### 6. Launch the application

```bash
streamlit run app.py
```

Open the local URL printed in the terminal, typically `http://localhost:8501`.

## Testing

Run the available test suite from the project root:

```bash
pytest
```

Tests help verify the RAG pipeline's behaviour. Retrieval and answer quality should also be evaluated with representative questions, including questions that are outside the knowledge base.

## Current Project Status

- Local RAG customer support application implemented.
- PDF ingestion, text chunking, vector retrieval, and LLM response generation integrated.
- Hybrid semantic and keyword retrieval implemented.
- Project source code and sample knowledge base available on GitHub.
- Designed for local execution; cloud deployment is not currently part of the project.

## Future Improvements

- Build a dedicated retrieval evaluation dataset.
- Measure retrieval quality using metrics such as Recall@k.
- Evaluate answer relevance and groundedness systematically.
- Add latency and retrieval-performance monitoring.
- Improve handling of document updates and knowledge-base versioning.

## Disclaimer

TechMarcus is an independent portfolio project using a fictional consumer electronics company and sample customer support documentation. It is intended for educational and demonstration purposes and is not affiliated with a real company.

