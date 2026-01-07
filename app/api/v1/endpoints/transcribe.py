import shutil
import tempfile
import os
from fastapi import APIRouter, Depends, File, UploadFile, Query, HTTPException
from app.models.schemas import TranscriptionResponse
from app.core.security import verify_api_key
from app.services.transcription import transcribe_file

router = APIRouter()


@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(
    file: UploadFile = File(...), api_key: str = Depends(verify_api_key)
):
    if not file.filename.endswith(".mp3"):
        raise HTTPException(status_code=400, detail="Only .mp3 files are supported")

    # Save uploaded file momentarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        shutil.copyfileobj(file.file, tmp_file)
        tmp_file_path = tmp_file.name

    try:
        # 1. Transcribe
        full_text, segments_data = transcribe_file(tmp_file_path)

        final_corrected_text = None

        return TranscriptionResponse(
            text=full_text,
            corrected_text=final_corrected_text,
            segments=segments_data,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"transcription failed: {str(e)}")
    finally:
        # Cleanup temp file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
