import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="test.wav", duration=5, fs=44100):
    print("🎙️ Recording... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"Recording saved as {filename}")
