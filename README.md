
# 🤖 N.O.V.A. – Neural Operated Virtual Assistant

**Created by Syed Mohammad Maaz**

N.O.V.A. (Neural Operated Virtual Assistant) is a smart, fast, and voice-driven AI assistant built using modern APIs and Python libraries. It can control system features like volume and brightness, provide intelligent responses using large language models, and speak back to users in real-time.

---

## 🚀 Features

- 🧠 **AI Chat** powered by **LLaMA 3 (via Groq API)**  
- 🔊 **Voice Output** using `gTTS` (Google Text-to-Speech)  
- 💡 **System Control**:
  - Adjust volume using `pycaw`
  - Adjust brightness using `screen_brightness_control`
- 📈 **Smart Understanding** of user requests (e.g., number of points to return)
- ⚡ **Fast and concise responses**
- 🗣️ **Wake-word free**, instant trigger via function

---

## 🛠️ Built With

| Component               | Usage                                           |
|------------------------|--------------------------------------------------|
| `Groq API`             | Accessing LLaMA 3 model for AI reasoning        |
| `requests`             | Sending/receiving API calls                     |
| `re` (regex)           | Extracting numbers (e.g., "5 tips", "3 reasons")|
| `pycaw`                | Controlling system audio                        |
| `screen_brightness_control` | Adjusting screen brightness              |
| `gTTS`                 | Text-to-speech conversion (offline voice)       |

---

## 🧩 File Structure

```
NOVA/
│
├── nova_ui.py              # Main UI code with GIF + controls
├── ai.py                   # AI processing using Groq API
├── system_control.py       # Brightness and volume control
├── voice.py                # TTS voice module using gTTS
├── assets/                 # GIFs and resources
└── README.md               # Project documentation
```

---

## 🧪 Sample Questions to Try

> "Give me 5 facts about Mars"  
> "Increase volume by 20%"  
> "Reduce brightness"  
> "Tell me 3 tips for focus"

---

## 🔐 API Key Note

To run this locally, you’ll need a valid Groq API key. You can get one by signing up at [https://console.groq.com](https://console.groq.com)

```python
GROQ_API_KEY = "your_api_key_here"
```

---

## 📸 Preview

![NOVA UI Preview](assets/preview.gif)

---

## 🧑‍💻 Author

**Syed Mohammad Maaz**  
📫 [maaz582ss@gmail.com](mailto:maaz582ss@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/maaz9764) | [GitHub](https://github.com/syedmaaz2212)

---

## ⭐ Future Plans

- Add microphone input for voice conversation  
- Add weather, news, and personal productivity tools  
- Build offline fallback using open-source models  

---

## 🌟 Give it a star if you like it!
