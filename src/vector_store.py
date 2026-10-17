
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from src.document_loader import load_pdf
from src.text_splitter import split_text


# Project configuration
PDF_PATH = "data/TechMarcus_Knowledge_Base.pdf"
DB_PATH = "chroma_db"
COLLECTION_NAME = "techmarcus_knowledge"

# Load the local embedding model
print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a persistent local ChromaDB database
client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"},
)


def build_vector_store():
    """Extract, chunk, embed and store the knowledge-base PDF."""

    print("Reading PDF...")
    document_text = load_pdf(PDF_PATH)

    print("Splitting document into chunks...")
    chunks = split_text(
        document_text,
        chunk_size=500,
        chunk_overlap=100,
    )

    if not chunks:
        raise ValueError("No text chunks were extracted from the PDF.")

    print(f"Creating embeddings for {len(chunks)} chunks...")

    embeddings = embedding_model.encode(
        chunks,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()

    source = str(Path(PDF_PATH))

    # Remove older chunks from this source before rebuilding.
    existing = collection.get(
        where={"source": source},
        include=[],
    )

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # Store the vectors, text and metadata in ChromaDB.
    collection.upsert(
        ids=[f"techmarcus_chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {
                "source": source,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ],
    )

    print("\nVector store created successfully!")
    print(f"Chunks stored: {collection.count()}")
    print(f"Database location: {DB_PATH}")


def search_documents(question: str, top_k: int = 3):
    """Retrieve the most relevant document chunks for a question."""

    query_embedding = embedding_model.encode(
        question,
        normalize_embeddings=True,
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    for i, document in enumerate(results["documents"][0], start=1):
        metadata = results["metadatas"][0][i - 1]
        distance = results["distances"][0][i - 1]

        print(f"\n--- Result {i} ---")
        print(f"Source: {metadata['source']}")
        print(f"Chunk: {metadata['chunk_index']}")
        print(f"Cosine distance: {distance:.4f}")
        print(document)


if __name__ == "__main__":
    build_vector_store()

    print("\nTesting semantic search...")
    search_documents(
        "What should a customer do if their product is faulty?",
        top_k=3,
    )
