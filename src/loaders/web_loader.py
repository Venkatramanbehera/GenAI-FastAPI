from langchain_community.document_loaders import WebBaseLoader
from src.loaders.base import BaseLoader
import bs4

class WebLoader(BaseLoader):
    def load(self, url:str) -> str:
        """
        Wraps langchain_community.document_loaders.WebBaseLoader
        to read websites.
        """
        try:
            loader = WebBaseLoader(web_paths=(url,))
            documents = loader.load()

            return "\n\n".join([doc.page_content for doc in documents])
        except Exception as e:
            return f"Error loading website: {str(e)}"