# import os
# import json
# from typing import Dict, Any, Optional

# # Imports for Google Gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.summarize import load_summarize_chain
# from langchain.prompts import PromptTemplate

# from .utils import extract_documents_from_url

# # The prompt remains the same, as it's model-agnostic.
# PROMPT_TEMPLATE = """
# You are an expert analyst. Your task is to provide a structured analysis of the following web page content.

# Read the content carefully and perform two tasks:
# 1.  Write a concise, neutral, one-paragraph summary of the main subject matter.
# 2.  Extract the 5 most important and relevant keywords or concepts.

# Return your response as a single, valid JSON object with two keys: "summary" and "keywords".

# Content:
# "{text}"

# JSON Response:
# """

# PROMPT = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"])

# def get_ai_analysis_from_url(url: str) -> Optional[Dict[str, Any]]:
#     """
#     Orchestrates the full pipeline using the Google Gemini model.
#     """
#     documents = extract_documents_from_url(url)
#     if not documents:
#         return None

#     try:
#         # Initialize the ChatGoogleGenerativeAI model
#         llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

#         chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
        
#         print("Invoking Google Gemini model for analysis...")
        
#         response_dict = chain.invoke({"input_documents": documents})
#         ai_response_str = response_dict.get("output_text", "")
        
#         # --- ADDED: Robust JSON Cleaning Step ---
#         # This function cleans the string to remove markdown formatting (e.g., ```json ... ```)
#         # that LLMs often add to their responses.
#         if "```json" in ai_response_str:
#             # Extract the content between the first '{' and the last '}'
#             start_index = ai_response_str.find('{')
#             end_index = ai_response_str.rfind('}') + 1
#             if start_index != -1 and end_index != 0:
#                 ai_response_str = ai_response_str[start_index:end_index]
        
#         # The cleaned string is now ready for parsing.
#         analysis_result = json.loads(ai_response_str)
        
#         print(f"AI analysis successful: {analysis_result}")
#         return analysis_result

#     except json.JSONDecodeError:
#         print(f"CRITICAL: Failed to parse JSON response from the Gemini model. Raw response: {ai_response_str}")
#         return None
#     except Exception as e:
#         print(f"CRITICAL: An error occurred during AI analysis. Error Type: {type(e).__name__}, Details: {repr(e)}")
#         return None


import os
import json
from typing import Dict, Any, Optional

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from .utils import extract_main_content

PROMPT_TEMPLATE = """
You are an expert analyst. Your task is to provide a structured analysis of the following web page content.

Read the content carefully and perform two tasks:
1.  Write a concise, neutral, one-paragraph summary of the main subject matter.
2.  Extract the 5 most important and relevant keywords or concepts.

Return your response as a single, valid JSON object with two keys: "summary" and "keywords".

Content:
"{text}"

JSON Response:
"""

PROMPT = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"])

def get_ai_analysis_from_url(url: str) -> Optional[Dict[str, Any]]:
    
    main_text = extract_main_content(url)
    if not main_text:
        return None

    try:

        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

        chain = LLMChain(llm=llm, prompt=PROMPT)
        
        print("Invoking Google Gemini model for analysis...")
        
        response_dict = chain.invoke({"text": main_text})

        ai_response_str = response_dict.get("text", "")
        
        if "```json" in ai_response_str:
            start_index = ai_response_str.find('{')
            end_index = ai_response_str.rfind('}') + 1
            if start_index != -1 and end_index != 0:
                ai_response_str = ai_response_str[start_index:end_index]
        
        analysis_result = json.loads(ai_response_str)
        
        print(f"AI analysis successful: {analysis_result}")
        return analysis_result

    except json.JSONDecodeError:
        print(f"CRITICAL: Failed to parse JSON response from the Gemini model. Raw response: {ai_response_str}")
        return None
    except Exception as e:
        print(f"CRITICAL: An error occurred during AI analysis. Error Type: {type(e).__name__}, Details: {repr(e)}")
        return None

