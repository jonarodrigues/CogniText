import logging
import os
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

# Configure logging for production observability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CogniText")

class AnalysisResult(BaseModel):
    \"\"\"
    Structured schema for AI analysis.
    This ensures that the output is always consistent and valid.
    \"\"\"
    summary: str = Field(description="A brief summary of the text")
    sentiment: str = Field(description="The emotional tone of the text (Positive/Negative/Neutral)")
    key_points: List[str] = Field(description="A list of 3-5 main points extracted from the text")
    suggested_actions: Optional[List[str]] = Field(description="Next steps based on the text content")

class CogniTextEngine:
    def __init__(self, api_key: str, provider: str = "openai", model: str = "gpt-4-turbo-preview"):
        self.api_key = api_key
        self.provider = provider
        self.model_name = model
        
        # Initialize provider logic
        if provider == "openai":
            self.llm = ChatOpenAI(model=model, openai_api_key=api_key, temperature=0.1)
        else:
            raise ValueError(f"Provider {provider} is currently not implemented in this version.")
            
        logger.info(f"Initialized CogniTextEngine with provider: {provider}")

    def analyze(self, text: str) -> AnalysisResult:
        \"\"\"
        Analyzes the provided text and returns a structured AnalysisResult.
        \"\"\"
        logger.info(f"Starting analysis for text (length: {len(text)} chars)")
        
        # 1. Setup Parser
        parser = PydanticOutputParser(pydantic_object=AnalysisResult)
        
        # 2. Define Prompt with schema instructions
        prompt = ChatPromptTemplate.from_template(
            \"\"\"
            Analyze the following text and provide a structured JSON response.
            
            Text: {text}
            
            Format Instructions: {format_instructions}
            \"\"\"
        )
        
        # 3. Chain execution
        chain = prompt | self.llm | parser
        
        try:
            result = chain.invoke({
                "text": text,
                "format_instructions": parser.get_format_instructions()
            })
            logger.info("Analysis completed successfully.")
            return result
        except Exception as e:
            logger.error(f"Error during AI analysis: {str(e)}")
            raise e

# Designed by Jonathan Rodrigues