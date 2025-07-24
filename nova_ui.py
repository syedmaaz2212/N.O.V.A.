import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from voice import speak
from ai import chat_with_ai
from commands import process_command
import speech_recognition as sr
import threading
import os
import time
import sys

recognizer = sr.Recognizer()
recognizer.energy_threshold = 600
recognizer.dynamic_energy_threshold = True

class NovaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N.O.V.A. - AI Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#000000")

        # === Main frame to center ===
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(expand=True)

        # === Load & display animated GIF ===
        gif_path = os.path.join("theme", "NOVA2.0.gif")
        self.gif_label = tk.Label(self.main_frame, bg="black")
        self.gif_label.pack(pady=(20, 10))  # moved up slightly

        self.frames = [ImageTk.PhotoImage(img.copy().resize((350, 350))) for img in ImageSequence.Iterator(Image.open(gif_path))]
        self.gif_frame_index = 0
        self.animate_gif()

        # === Status Label ===
        self.status_var = tk.StringVar(value="N.O.V.A. Initializing system...")
        self.status_label = tk.Label(self.main_frame, textvariable=self.status_var,
                                     font=("Consolas", 16), fg="magenta", bg="black")
        self.status_label.pack(pady=(0, 5))

        self.typing_job = None  # For managing typing animation

        # === Start initialization ===
        threading.Thread(target=self.run_initial_sequence, daemon=True).start()

    def animate_gif(self):
        self.gif_label.config(image=self.frames[self.gif_frame_index])
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.frames)
        self.root.after(100, self.animate_gif)

    def update_status(self, text, delay=30):
        if self.typing_job:
            self.root.after_cancel(self.typing_job)

        self.status_var.set("")
        self.typing_index = 0
        self.typing_text = text

        def animate():
            if self.typing_index < len(self.typing_text):
                self.status_var.set(self.typing_text[:self.typing_index + 1])
                self.typing_index += 1
                self.typing_job = self.root.after(delay, animate)
            else:
                self.typing_job = None

        animate()

    def run_initial_sequence(self):
        self.update_status("Initializing system...")
        speak("Initializing system...")
        time.sleep(1.5)

        self.update_status("Speaking...")
        speak("Hello! I am NOVA. How can I help you today?")
        time.sleep(1.5)

        self.update_status("Listening for wake word...")

        # Start background listener after greeting
        threading.Thread(target=self.listen_for_wake_word_loop, daemon=True).start()

    def listen_for_wake_word_loop(self):
        while True:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio).lower()
                print(f"Wake Word Detected Input: {word}")
                if "nova" in word:
                    self.update_status("Wake word detected!")
                    time.sleep(0.5)
                    self.update_status("Speaking...")
                    speak("Yes sir")
                    self.handle_command_mode()
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except Exception as e:
                print("Wake loop error:", e)
                self.update_status("Wake loop error")

    def handle_command_mode(self):
        activation_start = time.time()
        while time.time() - activation_start < 300:
            try:
                self.update_status("Listening for command...")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.3)
                    audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                if command in ["exit", "quit", "stop"]:
                    self.update_status("Shutting down...")
                    speak("Shutting down. Goodbye sir..")
                    self.root.destroy()
                    sys.exit()

                self.update_status("Speaking...")
                result = process_command(command)
                if result:
                    speak(result)

                if result == "reset":
                    speak("Yes boss")
                    activation_start = time.time()

                self.update_status("Listening for command...")

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                speak("I didn't catch that. Please repeat.")
                self.update_status("Listening for command...")
            except Exception as e:
                print("Command mode error:", e)
                speak("An error occurred while processing your command.")
                self.update_status("Command error")

if __name__ == "__main__":
    root = tk.Tk()
    app = NovaApp(root)
    root.mainloop()
