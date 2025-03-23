from web_scraper import page_data
from llm_client import llm
from prompt_template import prompt_extract, prompt_email
from chroma_db_client import ChromaDBClient
import pandas as pd
from langchain_core.output_parsers import JsonOutputParser

# Email generation
def generate_email(job_description, link_list):
    chain_email = prompt_email | llm
    res = chain_email.invoke({"job_description": str(job_description), "link_list": link_list})
    return res.content

# Main function
def main():
    # Load data from CSV
    df = pd.read_csv("my_portfolio.csv")

    # Create ChromaDB client
    chroma_db_client = ChromaDBClient("portfolio")
    chroma_db_client.add_documents(df)

    # Extract job postings
    chain_extract = prompt_extract | llm
    res = chain_extract.invoke(input={'page_data': page_data})
    json_parser = JsonOutputParser()
    json_res = json_parser.parse(res.content)

    # Generate email
    job_description = json_res
    links = chroma_db_client.collection.query(query_texts=json_res['skills'], n_results=2).get('metadatas', [])
    email = generate_email(job_description, links)
    print(email)

if __name__ == '__main__':
    main()