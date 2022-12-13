import speech_recognition as sr
import pyaudio

# Set up the audio input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Create a Recognizer object
recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
  print("Speak now:")
  frames = []
  for i in range(0, 44100):
    data = stream.read(1024)
    frames.append(data)

  # Convert the recorded audio into a DigitalData object
  audio = sr.AudioData(b''.join(frames), 44100, 2)

# Convert the recorded audio into text
text = recognizer.recognize_google(audio)

# Print the converted text
print(text)


# Stop recording
stream.stop_stream()
stream.close()
p.terminate()