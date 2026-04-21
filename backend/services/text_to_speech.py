import pyttsx3
import threading

def speak_text(text):
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=run)
    thread.start()