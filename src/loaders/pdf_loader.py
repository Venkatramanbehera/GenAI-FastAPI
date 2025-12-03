import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from src.loaders.base import BaseLoader

class PdfLoader(BaseLoader):
    def load(self, file_content: bytes) -> str:
        """
        Wraps langchain_community.document_loaders.PyPDFLoader
        to read pdf files.
        """

        temp_path = None

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file_content)
            temp_path = tmp.name

        try:
            loader = PyPDFLoader(temp_path)
            documents = loader.load()
            print(type (documents[0]))
            return "\n\n".join([doc.page_content for doc in documents])
        except Exception as e:
            return f"Error reading PDF with LangChain: {str(e)}"
        
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)