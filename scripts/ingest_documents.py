from pathlib import Path
import json
import re

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"


def clean_text(text: str) -> str:
    """
    Basic preprocessing:
    - Remove extra whitespace
    - Normalize line breaks
    - Strip leading/trailing spaces
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def ingest_documents():
    raw_path = Path(RAW_DATA_DIR)
    processed_path = Path(PROCESSED_DATA_DIR)

    processed_path.mkdir(parents=True, exist_ok=True)

    documents = []

    for file in raw_path.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned_content = clean_text(content)

        document = {
            "filename": file.name,
            "content": cleaned_content,
            "word_count": len(cleaned_content.split())
        }

        documents.append(document)

    output_file = processed_path / "documents.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=4)

    print(
        f"Successfully processed {len(documents)} documents."
    )
    print(
        f"Output saved to: {output_file}"
    )


if __name__ == "__main__":
    ingest_documents()
  
