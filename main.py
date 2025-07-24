import time
import speech_recognition as sr
from voice import speak
from commands import process_command

recognizer = sr.Recognizer()
recognizer.energy_threshold = 600
recognizer.dynamic_energy_threshold = True

def listen_for_wake_word():
    """Listens for the wake word 'nova'."""
    with sr.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
    return recognizer.recognize_google(audio).lower()

def listen_for_command():
    """Listens for a follow-up command after wake word or button press."""
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)
    return recognizer.recognize_google(audio).lower()

if __name__ == "__main__":
    speak("Initializing system....")

    while True:
        try:
            word = listen_for_wake_word()
            print(f"Heard: {word}")

            if "nova" in word:
                print("Wake word detected!")
                speak("Yes boss")

                activation_start = time.time()
                while time.time() - activation_start < 180:
                    try:
                        command = listen_for_command()
                        print(f"Command: {command}")

                        result = process_command(command)

                        if result == "reset":
                            speak("Yes boss")
                            activation_start = time.time()

                    except sr.WaitTimeoutError:
                        print("Waiting for command...")
                    except sr.UnknownValueError:
                        speak("I didn't catch that. Please repeat.")
                    except Exception as e:
                        print("Command error:", e)
                        speak("An error occurred while processing your command.")

        except sr.WaitTimeoutError:
            print("Wake word timeout.")
        except sr.UnknownValueError:
            print("Didn't catch the wake word.")
        except Exception as e:
            print("Error:", e)
            speak("There was an error. Please check the system.")
