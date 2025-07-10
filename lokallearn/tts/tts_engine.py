# TTS module
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speed of speech
    engine.say(text)
    engine.runAndWait()
