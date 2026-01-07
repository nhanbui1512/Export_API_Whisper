from app.core.config import get_whisper_model
from app.models.schemas import Segment

def transcribe_file(file_path: str) -> tuple[str, list[Segment]]:
    model = get_whisper_model()
    segments_gen, info = model.transcribe(file_path, beam_size=3)
    
    segments_data = []
    full_text_list = []
    
    for segment in segments_gen:
        segments_data.append(Segment(
            text=segment.text,
            start=segment.start,
            end=segment.end
        ))
        full_text_list.append(segment.text)
    
    full_text = "".join(full_text_list)
    return full_text, segments_data
