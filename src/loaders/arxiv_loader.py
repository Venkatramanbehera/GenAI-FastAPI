from langchain_community.document_loaders import ArxivLoader as LangChainArxivLoader
from src.loaders.base import BaseLoader

class ArxivLoader(BaseLoader):
    def load(self, query: str) -> str:
        """
        Wraps langchain_community.document_loaders.ArxivLoader
            to read Arxiv Pdf
        """
        try:
            loader = LangChainArxivLoader(query= query, load_max_docs = 2,load_all_available_meta=False)
            documents = loader.load()

            if not documents:
                return "No papers found for this query."

            return "\n\n".join([doc.page_content for doc in documents])
        except Exception as e:
            return f"Error loading Arxiv: {str(e)}"