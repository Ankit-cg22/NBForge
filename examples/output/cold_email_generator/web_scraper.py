from langchain_community.document_loaders import WebBaseLoader

# Web Scraping
loader = WebBaseLoader("https://careers.nike.com/cdn-security-engineer/job/R-48004")
page_data = loader.load().pop().page_content