#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:8000"

# Files
AUDIO_FILE="giong-hue.mp3"

echo "=== Starting Verification ==="

# 1. Test Authentication Failure
echo "\n[Test 1] Testing Authentication Failure..."
curl -s -o /dev/null -w "%{http_code}" -X POST "${BASE_URL}/api/v1/transcribe" \
  -H "X-API-Key: invalid_key" \
  -F "file=@${AUDIO_FILE}"
echo " (Expected: 401)"

# 2. Test Success (No Correction)
echo "\n[Test 2] Testing Transcription (No Correction)..."
curl -X POST "${BASE_URL}/api/v1/transcribe" \
  -H "X-API-Key: key_12345" \
  -F "file=@${AUDIO_FILE}" | cut -c 1-100...
echo " (Expected: JSON with text and segments)"

# 3. Test Success (With Correction)
# Note: This might fail if OPENAI_API_KEY is not set in the server environment, but we test the endpoint mechanics.
echo "\n[Test 3] Testing Transcription (With Correction)..."
curl -X POST "${BASE_URL}/api/v1/transcribe?correct_spelling=true" \
  -H "X-API-Key: prod_secret_key" \
  -F "file=@${AUDIO_FILE}" | cut -c 1-100...
echo " (Expected: JSON output)"

echo "\n\n=== Verification Complete ==="
