import time
from speech import speak
def set_reminder(seconds, message):
    time.sleep(seconds)
    print(message)
    speak(f"Reminder: {message}")