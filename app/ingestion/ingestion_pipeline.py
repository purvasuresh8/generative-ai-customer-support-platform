from app.ingestion.document_loader import load_documents
from app.ingestion.document_cleaner import clean_document

def process_documents(path):

    docs = load_documents(path)

    return [
        clean_document(doc)
        for doc in docs
    ]
  
