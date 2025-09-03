from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class URLRequest(BaseModel):
    """The request model containing the URL to be analyzed."""
    url: HttpUrl

class AnalysisResponse(BaseModel):
    """
    The response model for a successful analysis.
    It now includes a summary and a curated list of keywords from the AI.
    """
    summary: str
    keywords: List[str]

class ErrorResponse(BaseModel):
    """A response model for errors."""
    detail: str

