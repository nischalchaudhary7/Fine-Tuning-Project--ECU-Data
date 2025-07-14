#This codes checks weatherv my deepseek api is working properly or not. It is the step NLP process after ecu_qa_data2.py

import requests
import json

# ✅ Replace with your actual OpenRouter API key
API_KEY = "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"

# API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Headers for the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://yourwebsite.com",  # Optional for OpenRouter rankings
    "X-Title": "ECU Chatbot Project",  # Optional project title
}

# Payload (the question to ask DeepSeek)
payload = {
    "model": "deepseek/deepseek-r1:free",  # ✅ Free version of DeepSeek R1
    "messages": [
        {"role": "system", "content": "You are an ECU university assistant."},
        {"role": "user", "content": "What programs does East Central University offer?"}
    ]
}

# Make the API request
response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

# ✅ Debugging: Print full API response
print("Full Response:", response.text)

# ✅ Check if response is valid JSON
try:
    data = response.json()
except json.JSONDecodeError:
    print("❌ Error: API response is not valid JSON.")
    exit()

# ✅ Check if "choices" key exists
if "choices" in data:
    print("✅ DeepSeek API Test Successful!")
    print("Response:", data["choices"][0]["message"]["content"])
else:
    print("❌ DeepSeek API Error: 'choices' key missing in response.")
    print("Full Response:", json.dumps(data, indent=4))


