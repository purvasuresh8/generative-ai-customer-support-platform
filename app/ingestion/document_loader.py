from pathlib import Path

def load_documents(folder_path):

    documents = []

    for file in Path(folder_path).glob("*.txt"):
        with open(file, "r") as f:
            documents.append(f.read())

    return documents
  
