
def split_text(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100
) -> list[str]:
    """Split text into overlapping character-based chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be non-negative and smaller than chunk_size"
        )

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


if __name__ == "__main__":
    sample_text = (
        "TechMarcus provides technical support, warranty information, "
        "shipping assistance, and troubleshooting guides for customers. "
        * 50
    )

    chunks = split_text(sample_text)

    print(f"Original characters: {len(sample_text)}")
    print(f"Number of chunks: {len(chunks)}")
    print(f"\nFirst chunk:\n{chunks[0]}")
