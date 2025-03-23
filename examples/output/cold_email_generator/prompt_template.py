from langchain_core.prompts import PromptTemplate

prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        For skills put it as an array of strings , each string representing one of the required skills.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
)

prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Ankit, a software engineer with 1 year of experience.
        You have expertise in Java , ReactJs , Springboot and Data structures & Algorithms.
        
        Your job is to write a cold email to the HR regarding the job mentioned above describing how you are suited for the job. 
        
        Also add the most relevant ones from the following links to showcase your portfolio: {link_list}
        Remember you are Ankit , a software engineer.
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )