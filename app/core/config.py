import json
import os
from faster_whisper import WhisperModel
import dotenv
import torch


dotenv.load_dotenv()

# Global State
_whisper_model = None
_valid_api_keys = set()
AUTH_KEYS_FILE = "auth_keys.json"


def get_whisper_model():
    global _whisper_model

    if _whisper_model is not None:
        return _whisper_model

    use_cuda = torch.cuda.is_available()

    if use_cuda:
        device = "cuda"
        compute_type = "float32"  # nhanh nhất cho GPU
        print("🚀 Loading Whisper model on GPU (CUDA, float32)")
    else:
        device = "cpu"
        compute_type = "int8"  # tối ưu cho CPU
        print("🖥️ Loading Whisper model on CPU (int8)")

    _whisper_model = WhisperModel(
        "medium",
        device=device,
        compute_type=compute_type,
        cpu_threads=4 if not use_cuda else 0,  # chỉ cần cho CPU
        num_workers=1,
    )

    return _whisper_model


def load_api_keys():
    global _valid_api_keys
    if os.path.exists(AUTH_KEYS_FILE):
        try:
            with open(AUTH_KEYS_FILE, "r") as f:
                keys = json.load(f)
                _valid_api_keys = set(keys)
                print(f"Loaded {len(_valid_api_keys)} API keys.")
        except Exception as e:
            print(f"Error loading auth keys: {e}")


def get_valid_api_keys():
    return _valid_api_keys


# Initialize on import (optional, or call explicitly in main startup)
load_api_keys()
