import os

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

information = """
    Michael Joseph Jackson (August 29, 1958 – June 25, 2009) was an American singer, songwriter, dancer, and philanthropist. 
    Dubbed the "King of Pop", he is regarded as one of the most culturally significant figures of the 20th century. 
    Over a four-decade career, his music achievements broke racial barriers in America and made him a dominant figure across the world.
"""

if __name__ == "__main__":
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    print(gemini_api_key)

    summary_template = """
        given the following information {information} about a person, I want you to create:
        1. a short summary
        2. a funny fact about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", google_api_key=gemini_api_key
    )

    # "|" is an llm operator to supply information to the llm
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
