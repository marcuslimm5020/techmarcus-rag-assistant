
from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """Extract text from a PDF knowledge-base document."""

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path.resolve()}"
        )

    reader = PdfReader(str(pdf_path))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages.append(f"[Page {page_number}]\n{text}")

    return "\n\n".join(pages)


if __name__ == "__main__":
    pdf_path = "data/TechMarcus_Knowledge_Base.pdf"

    document_text = load_pdf(pdf_path)

    print(f"Extracted {len(document_text)} characters")
    print("\nFirst 1,000 characters:\n")
    print(document_text[:1000])
