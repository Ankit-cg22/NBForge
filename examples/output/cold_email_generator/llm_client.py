from langchain_groq import ChatGroq

llm = ChatGroq(
    model = "llama-3.3-70b-versatile" ,
    temperature = 0 ,
    groq_api_key = "<your_api_key>"
)