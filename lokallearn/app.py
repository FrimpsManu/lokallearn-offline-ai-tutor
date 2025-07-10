# Main app entry point
from lokallearn.stt.whisper_model import transcribe_audio
from lokallearn.llm.local_llm import load_llm_model, get_llm_response
from lokallearn.tts.tts_engine import speak_text
from record_audio import record_audio  # Make sure this is a function now

def main():
    print("🧠 Loading models once...")

    # Load local LLM once
    llm = load_llm_model()

    while True:
        input("Press Enter to record your question... (Ctrl+C to quit)")
        record_audio("test.wav")

        question = transcribe_audio("test.wav")
        print("You said:", question)

        answer = get_llm_response(llm, question)
        print("AI Answer:", answer)

        speak_text(answer)
        print("Ready for next question...\n")

if __name__ == "__main__":
    main()
