import re
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pythoncom  # ✅ Required for COM initialization
from voice import speak

def extract_percent(text):
    match = re.search(r'(\d+)', text)
    return int(match.group(1)) if match else None

def set_brightness(percent):
    try:
        sbc.set_brightness(percent)
        speak(f"Brightness set to {percent} percent")
    except Exception as e:
        speak("Failed to adjust brightness")
        print("Brightness Error:", e)

def change_brightness(change_percent):
    try:
        current = sbc.get_brightness(display=0)[0]
        new = max(0, min(100, current + change_percent))
        sbc.set_brightness(new)
        speak(f"Brightness adjusted to {new} percent")
    except Exception as e:
        speak("Couldn't change brightness")
        print("Brightness Error:", e)

def set_volume(percent):
    try:
        pythoncom.CoInitialize()  # ✅ Initialize COM
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(percent / 100.0, None)
        speak(f"Volume set to {percent} percent")
    except Exception as e:
        speak("Failed to set volume")
        print("Volume Error:", e)

def change_volume(change_percent):
    try:
        pythoncom.CoInitialize()  # ✅ Initialize COM
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar() * 100
        new = max(0, min(100, current + change_percent))
        volume.SetMasterVolumeLevelScalar(new / 100.0, None)
        speak(f"Volume adjusted to {int(new)} percent")
    except Exception as e:
        speak("Couldn't change volume")
        print("Volume Error:", e)
