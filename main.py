from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.endpoints import transcribe
from app.core.config import load_api_keys, get_whisper_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load keys
    load_api_keys()
    # Eager load the model
    get_whisper_model()
    yield
    # Clean up if needed

app = FastAPI(title="Whisper Transcription Service", lifespan=lifespan)

# Include Routers
app.include_router(transcribe.router, prefix="/api/v1", tags=["transcription"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
