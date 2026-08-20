
import re

def clean_document(text):

    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text
  
