import pyttsx3
import speech_recognition as sr
import Function

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """it take microphone input from the user and return an value"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresehold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("user said ",query)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    Function.wishMe()
    Function.operation()
