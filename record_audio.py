import sounddevice as sd
from scipy.io.wavfile import write

# Recording parameters
fs = 16000  # 16kHz sample rate (Whisper default)
duration = 5  # Duration in seconds
filename = "test.wav"

print("🎙️ Recording... Speak now!")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
write(filename, fs, recording)
print(f"✅ Recording saved as {filename}")
