import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from groq_client import GroqClient
from dotenv import load_dotenv
import yaml
from nbforge.utils.constants import *
import platform

load_dotenv()

class Chains:
    def __init__(self):
        self.llm = GroqClient().get_model()
        self.prompts = self.load_prompts("src/nbforge/utils/prompts.yml")
    
    @staticmethod
    def load_prompts(file_path):
        """Loads a specific prompt from a YAML file."""
        with open(file_path, "r") as file:
            prompts = yaml.safe_load(file)
        return prompts
    
    def get_prompt(self, key):
        """Fetches a specific prompt by key."""
        if key not in self.prompts:
            raise Exception(f"Prompt '{key}' not found in prompts.yml")
        return self.prompts[key]


    def get_file_structure(self, code_blocks , markdown_blocks , streamlit_desc_block,fastAPI_desc_block):
        prompt_name = None 
        if streamlit_desc_block is not None : 
            prompt_name = NB_TO_MODULE_STREAMLIT_PROMPT
        elif fastAPI_desc_block is not None:
            prompt_name = NB_TO_MODULE_FASTAPI_PROMPT
        else: 
            prompt_name = NB_TO_MODULE_PROMPT
        print(f"using prompt {prompt_name}")
        prompt_file_structure = PromptTemplate.from_template(self.get_prompt(prompt_name))
        chain_extract = prompt_file_structure | self.llm
        res = chain_extract.invoke(
            input={
                "code_blocks": code_blocks , 
                "markdown_blocks" : markdown_blocks ,
                "streamlit_desc_block" :streamlit_desc_block , 
                "fastAPI_desc_block" : fastAPI_desc_block ,
                "platform":platform.system()
            }
        )
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse data.")
        return res
