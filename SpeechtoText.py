import speech_recognition as sr
# Record Audio
r = sr.Recognizer()
r.pause_threshold = 1.0
r.phrase_threshold = 1.0
r.non_speaking_duration = 1.0
r.energy_threshold =1000

##For live voice use 
#with sr.Microphone() as source:
with sr.AudioFile("G:\Dev\SpeechToText\d.wav") as source:
print("Say something!")
#listen for microphone, record for .wav 
audio = r.record(source)

try:
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
raise print("Could not request results from Google Speech Recognition service; {0}".format(e))
