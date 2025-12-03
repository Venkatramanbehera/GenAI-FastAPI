from abc import ABC, abstractmethod
from typing import Any

class BaseLoader(ABC):
    """
    Abstract Base Class for all document loaders.
    """

    @abstractmethod
    def load(self, source: Any) -> str:
        """
        Accepts a source (filepath, bytes, etc.) and returns extracted text.
        """
        pass