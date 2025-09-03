import os
import uvicorn
from app.main import app  

if __name__ == "__main__":
    # Railway/Render/Heroku/Cloud Run provide PORT env var
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
