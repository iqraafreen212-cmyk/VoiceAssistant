import datetime
import webbrowser
from speech import speak, listen

# Sabhi custom modules ko import kiya
from weather import get_weather
from news import get_news
from reminder import set_reminder

speak("Hello I am your assistant. System initialized.")
while True:
    command = listen()
    print(f"User said: {command}")
    if not command or command.strip() == "":
        continue
    if "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day ahead.")
        break 
    elif "weather" in command:
        speak("Which city's weather would you like to check?")
        city = listen()
        if city and city.strip() != "":
            city = city.lower().replace("of", "").replace("in", "").strip()
            speak(f"Checking weather for {city}")
            try:
                temp = get_weather(city)
                speak(f"The current temperature in {city} is {temp} degree celsius")
            except Exception as e:
                speak("Sorry, I couldnt fetch the weather.")
        else:
            speak("I didnt catch the city name.")
    elif "news" in command:
        speak("Fetching top news headlines.")
        try:
            articles = get_news()
            for i, article in enumerate(articles[:3], 1):
                speak(f"Headline {i}: {article['title']}")
        except Exception as e:
            speak("Sorry, I ran into an error fetching the news.")
    elif "reminder" in command:
        speak("What should i remind you about?")
        msg = listen()
        speak("In how many seconds?")
        time_str = listen()
        try:
            digits = ''.join(filter(str.isdigit, time_str))
            if digits:
                seconds = int(digits)
                speak(f"Setting a reminder for {seconds} seconds")
                set_reminder(seconds, msg)
                speak("Time's Up!")
            else:
                speak("Sorry, I didn't hear a number.")
        except Exception as e:
            speak("Sorry, I couldn't set the reminder.")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    else:
        speak("Command not recognized. Please try again.")
    print("\n--- Ready for next command ---")