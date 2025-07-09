# Whisper STT module
import whisper

# Load the tiny model (offline)
model = whisper.load_model("tiny")

# Transcribe an audio file
result = model.transcribe("test.wav")
question = result["text"]
print("You said:", question)

# Simulated LLM response
def get_answer_from_llm(prompt):
    prompt = prompt.lower()  # make lowercase for easier matching

    if "5 times 6" in prompt:
        return "The answer is 30"
    
    return "Sorry, I don't know yet."

# Get and print the answer
answer = get_answer_from_llm(question)
print("AI Answer:", answer)
