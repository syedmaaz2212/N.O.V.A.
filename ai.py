import re
import requests

GROQ_API_KEY = "#"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def extract_requested_points(prompt):
    match = re.search(r'\b(\d+)\b\s*(?:points|reasons|facts|tips|steps|names|countries|things|items)?', prompt, re.IGNORECASE)
    return int(match.group(1)) if match else 5

def chat_with_ai(prompt):
    try:
        num_points = extract_requested_points(prompt)

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are NOVA, a smart and fast assistant created by Syed Mohammad Maaz. Keep responses concise and useful."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 80 + (num_points * 20)  # Dynamic token cap
        }

        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        result = response.json()

        if 'choices' in result:
            full = result['choices'][0]['message']['content'].strip()

            # Try to extract numbered points like 1. 2. or 1) 2)
            points = re.findall(r'(\d+[\.\)]\s*.+?)(?=\n\d|$)', full, re.DOTALL)
            if not points:
                # fallback to sentence-based splitting
                points = re.split(r'[.!?]', full)

            cleaned_points = [p.strip() for p in points if p.strip()]
            return ' '.join(cleaned_points[:num_points]) + '.' if cleaned_points else full

        else:
            return "The AI response was not understood."

    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I couldn't connect to my online neural engine."
