from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from a .env file for local development
load_dotenv()

from .schemas import URLRequest, AnalysisResponse, ErrorResponse
from .services import get_ai_analysis_from_url

# Check for the Google API Key on startup
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY environment variable not set. Please set it in a .env file or export it.")

app = FastAPI(
    title="Web Page Analyzer API",
    description="An API that uses AI to analyze a web page, providing a summary and keywords."
)

# CORS Middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you would restrict this to your specific frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/analyze-url",
    response_model=AnalysisResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid URL or content"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
def analyze_url(request: URLRequest):
    """
    Accepts a URL, validates it, extracts main content via the service layer,
    and returns the AI-generated analysis.
    """
    try:
        # The endpoint's logic is now very clean, just a single call to the service function.
        analysis_result = get_ai_analysis_from_url(str(request.url))
        
        if analysis_result is None:
            raise HTTPException(
                status_code=400,
                detail="Could not process the URL. It might be invalid, inaccessible, not an HTML page, or the AI analysis failed."
            )
            
        return AnalysisResponse(
            summary=analysis_result.get("summary", "No summary generated."),
            keywords=analysis_result.get("keywords", [])
        )
        
    except Exception as e:
        print(f"An unexpected error occurred in the endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected internal server error occurred."
        )
