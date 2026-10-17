from src.document_loader import load_pdf
from src.text_splitter import split_text


def process_documents(pdf_path: str) -> list[str]:
    """Load a PDF and split its extracted text into chunks."""

    document_text = load_pdf(pdf_path)

    chunks = split_text(
        document_text,
        chunk_size=500,
        chunk_overlap=100,
    )

    print(f"Extracted characters: {len(document_text)}")
    print(f"Total chunks created: {len(chunks)}")

    if chunks:
        print("\nFirst chunk:\n")
        print(chunks[0])

    return chunks


if __name__ == "__main__":
    pdf_path = "data/TechMarcus_Knowledge_Base.pdf"
    process_documents(pdf_path)
