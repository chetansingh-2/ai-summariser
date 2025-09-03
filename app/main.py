from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from a .env file for local development
load_dotenv()

# Import your schemas and services
# Assuming they are in the same directory or a reachable path
from .schemas import URLRequest, AnalysisResponse, ErrorResponse
from .services import get_ai_analysis_from_url

# Check for the Google API Key on startup
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY environment variable not set. Please set it in a .env file or export it.")

app = FastAPI(
    title="Web Page Analyzer API",
    description="An API that uses AI to analyze a web page, providing a summary and keywords."
)

# CORS Middleware to allow requests from your Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you would restrict this to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World from Railway!"}


@app.post(
    "/analyze-url",
    response_model=AnalysisResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid URL or content"},
        500: {"model": ErrorResponse, "description": "Internal server error during analysis"}
    }
)
def analyze_url(request: URLRequest):
    """
    Accepts a URL, validates it, extracts main content, and uses an AI model
    to generate a summary and keywords.
    """
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



# if __name__ == "__main__":
#     import uvicorn
#     # Railway provides the PORT environment variable
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
