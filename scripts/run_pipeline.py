from pathlib import Path
import json

from app.ingestion.ingestion_pipeline import process_documents


RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"


def run_pipeline():
    print("Starting document ingestion pipeline...")

    documents = process_documents(RAW_DATA_PATH)

    output_dir = Path(PROCESSED_DATA_PATH)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "documents.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "id": idx,
                    "content": doc,
                    "word_count": len(doc.split())
                }
                for idx, doc in enumerate(documents)
            ],
            f,
            indent=4
        )

    print(f"Processed {len(documents)} documents")
    print(f"Saved output to {output_file}")
    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
  
