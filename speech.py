import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init()
def speak(text):
    print(f"Assistant says: {text}")
    engine.say(text)
    engine.runAndWait()
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.adjust_for_ambient_noise(source, duration=1)
         audio=r.listen(source)
    try:
        command=r.recognize_google(audio)
        print(command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return " "
    except sr.RequestError:
        print("Internet connection problem")
        return " "
    