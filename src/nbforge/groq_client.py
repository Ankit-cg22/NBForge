import os
from langchain_groq import ChatGroq
class GroqClient:
    """Class to manage ChatGroq instance."""

    def __init__(self , api_key: str = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.model = model

        if not self.api_key:
            raise ValueError("Groq API key is required. Set GROQ_API_KEY in env or pass it explicitly.")

        self.llm = ChatGroq(
            model = self.model,
            temperature = 0 ,
            groq_api_key = self.api_key
        )

    def get_model(self):
        """Return the ChatGroq model instance."""
        return self.llm
