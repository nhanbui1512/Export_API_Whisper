import sys
import os

# Ensure the app module can be imported
sys.path.append(os.getcwd())

from app.services.transcription import transcribe_file

def main():
    audio_file = "giong-hue.mp3"
    if not os.path.exists(audio_file):
        print(f"Error: File '{audio_file}' not found.")
        return

    print(f"Transcribing '{audio_file}'...")
    try:
        text, segments = transcribe_file(audio_file)
        print("\nTranscription Result:")
        print(text)
        print("\nSegments:")
        for segment in segments:
            print(f"[{segment.start:.2f} - {segment.end:.2f}]: {segment.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
