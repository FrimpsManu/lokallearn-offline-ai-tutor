import whisper

# Load the tiny model only once
model = whisper.load_model("tiny")

# Function to transcribe audio
def transcribe_audio(filename="test.wav"):
    result = model.transcribe(filename)
    return result["text"]
