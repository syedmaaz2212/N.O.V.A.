import webbrowser
import random
from system_control import (
    set_brightness, change_brightness, set_volume, change_volume, extract_percent
)
from ai import chat_with_ai
from voice import speak

def say_hi():
    speak(random.choice([
        "Hello, boss!",
        "Hi there, ready when you are!",
        "At your service."
    ]))

def process_command(c):
    c = c.lower()

    if "nova" in c:
        return "reset"

    if any(greet in c for greet in ["hi", "hello", "hey"]):
        say_hi()
    elif any(x in c for x in ["tell me about yourself", "who are you", "what can you do"]):
        speak("I'm NOVA — your personal voice assistant built by Syed Mohammad Maaz.")
    elif any(x in c for x in ["how are you", "how r u", "hru"]):
        speak(random.choice([
            "I'm fully operational!", "Doing great, boss!", "Running smoothly."
        ]))

    elif "open google" in c:
        speak("Opening Google"); webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        speak("Opening YouTube"); webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn"); webbrowser.open("https://www.linkedin.com/in/maaz9764/")
    elif "open instagram" in c:
        speak("Opening Instagram"); webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c:
        speak("Opening Facebook"); webbrowser.open("https://www.facebook.com")

    # Brightness
    elif "increase brightness" in c:
        change_brightness(extract_percent(c) or 10)
    elif "decrease brightness" in c:
        change_brightness(-(extract_percent(c) or 10))
    elif "set brightness" in c:
        p = extract_percent(c)
        if p is not None:
            set_brightness(p)

    # Volume
    elif "increase volume" in c:
        change_volume(extract_percent(c) or 10)
    elif "decrease volume" in c:
        change_volume(-(extract_percent(c) or 10))
    elif "set volume" in c:
        p = extract_percent(c)
        if p is not None:
            set_volume(p)

    elif c.strip() in ["exit", "quit", "stop"]:
        speak("Powering down. Goodbye boss.")
        exit()

    else:
        speak(chat_with_ai(c))
