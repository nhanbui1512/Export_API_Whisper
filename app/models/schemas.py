from typing import List, Optional
from pydantic import BaseModel


class Segment(BaseModel):
    text: str
    start: float
    end: float


class TranscriptionResponse(BaseModel):
    text: str
    corrected_text: Optional[str] = None
    segments: List[Segment]
