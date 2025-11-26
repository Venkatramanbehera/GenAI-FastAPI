from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    async def generate_text() -> str:
        """
        Abstract Method to generate text.
        Must be implmented by child class
        """
        pass