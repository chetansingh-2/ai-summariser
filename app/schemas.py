from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class URLRequest(BaseModel):
    url: HttpUrl

class AnalysisResponse(BaseModel):
    summary: str
    keywords: List[str]

class ErrorResponse(BaseModel):
    detail: str

