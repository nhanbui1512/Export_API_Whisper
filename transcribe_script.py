import sys
import os
import time

# Ensure the app module can be imported
sys.path.append(os.getcwd())

from app.services.transcription import transcribe_file
from app.core.config import get_whisper_model

def main():
    audio_file = "giong-hue.mp3"
    if not os.path.exists(audio_file):
        print(f"Error: File '{audio_file}' not found.")
        return

    # Pre-load the model so its loading time is not included in the transcription time
    print("Pre-loading model...")
    get_whisper_model()
    print("Model loaded.")

    print(f"Transcribing '{audio_file}'...")
    try:
        start_time = time.time()
        text, segments = transcribe_file(audio_file)
        end_time = time.time()
        
        duration = end_time - start_time
        
        print("\nTranscription Result:")
        print(text)
        print("\nSegments:")
        for segment in segments:
            print(f"[{segment.start:.2f} - {segment.end:.2f}]: {segment.text}")
            
        print(f"\nTime taken for transcription (excluding model load): {duration:.2f} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
