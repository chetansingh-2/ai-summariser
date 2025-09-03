from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware # ADDED: Import the CORS middleware


load_dotenv()

from .schemas import URLRequest, AnalysisResponse, ErrorResponse
from .services import get_ai_analysis_from_url

if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY environment variable not set. Please set it in a .env file or export it.")

app = FastAPI(
    title="Web Page Analyzer API",
    description="An API that uses AI to analyze a web page, providing a summary and keywords."
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins (you can restrict this to specific domains in production)
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"], # Allow all headers
)

@app.post(
    "/analyze-url",
    response_model=AnalysisResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid URL or content"},
        422: {"model": ErrorResponse, "description": "Validation error in request"},
        500: {"model": ErrorResponse, "description": "Internal server error during analysis"}
    }
)
def analyze_url(request: URLRequest):
    
    url = str(request.url)
    
    try:    
        analysis_result = get_ai_analysis_from_url(url)
        
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
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected internal server error occurred."
        )

