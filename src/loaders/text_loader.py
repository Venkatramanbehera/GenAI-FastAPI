import os
import tempfile
from langchain_community.document_loaders import TextLoader as LangChainTextLoader
from src.loaders.base import BaseLoader

class TextLoader(BaseLoader):
    def load(self, content) -> str:
        """
        Wraps langchain_community.document_loaders.TextLoader
        to read text files.
        """
        # LangChain loaders typically expect a file path, not bytes.
        # We create a temporary file to bridge this gap.

        temp_path = None

        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp:
            tmp.write(content)
            temp_path = tmp.name
            
        try:
            loader = LangChainTextLoader(temp_path)
            documents = loader.load()
            print(documents)
            return "\n\n".join([doc.page_content for doc in documents])
        except Exception as e:
            return f"Error loading text with LangChain: {str(e)}"
        
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

