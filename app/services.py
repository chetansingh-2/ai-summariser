import os
import json
from typing import Dict, Any, Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from .utils import ContentExtractor

class AIAnalyzer:

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
    
    def __init__(self, model_name: str = "gemini-1.5-flash-latest"):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
        self.prompt = PromptTemplate(template=self.PROMPT_TEMPLATE, input_variables=["text"])
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def _clean_response(self, response_str: str) -> str:
      
        if "```json" in response_str:
            start = response_str.find('{')
            end = response_str.rfind('}') + 1
            if start != -1 and end != 0:
                return response_str[start:end]
        return response_str

    def analyze(self, text: str) -> Optional[Dict[str, Any]]:
       
        try:
            print("Invoking Google Gemini model for analysis...")
            response_dict = self.chain.invoke({"text": text})
            ai_response_str = response_dict.get("text", "")
            
            cleaned_str = self._clean_response(ai_response_str)
            
            return json.loads(cleaned_str)
        except json.JSONDecodeError:
            print(f"CRITICAL: Failed to parse JSON response from the Gemini model. Raw response: {ai_response_str}")
            return None
        except Exception as e:
            print(f"CRITICAL: An error occurred during AI analysis: {repr(e)}")
            return None

def get_ai_analysis_from_url(url: str) -> Optional[Dict[str, Any]]:

    extractor = ContentExtractor(url)
    main_text = extractor.extract()
    
    if not main_text:
        return None
    
    analyzer = AIAnalyzer()
    analysis_result = analyzer.analyze(main_text)
    
    if analysis_result:
        print(f"AI analysis successful: {analysis_result}")
    
    return analysis_result

