import pyttsx3
from gtts import gTTS
import pygame
import os

USE_PYTTS = False  # Change to False to use gTTS + pygame & True for pyttsx3

def speak(text):
    print(f"N.O.V.A.: {text}")
    
    if USE_PYTTS:
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 3.0)
        engine.say(text)
        engine.runAndWait()
    else:
        tts = gTTS(text=text, lang='en', slow=False)
        filename = "temp_voice.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.quit()
        os.remove(filename)
