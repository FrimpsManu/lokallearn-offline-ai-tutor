# Whisper STT module
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import whisper
from lokallearn.llm.local_llm import get_answer_from_llm


# Load the tiny model (offline)
model = whisper.load_model("tiny")

# Transcribe an audio file
result = model.transcribe("test.wav")
question = result["text"]
print("You said:", question)

# Use real LLM
answer = get_answer_from_llm(question)
print("AI Answer:", answer)
