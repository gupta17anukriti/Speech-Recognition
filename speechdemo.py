import speech_recognition as sr
import record

r = sr.Recognizer()
r.energy_threshold = 1000
 
harvard = sr.AudioFile('harvard.wav')
print("wait a moment!")

with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))

