'''import requests
import json
from fuzzywuzzy import fuzz
import time
import logging
logging.basicConfig(filename="ecu_chatbot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load local dataset
input_file = "ecu_finetune_dataset.json"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        local_data = json.load(file)
except FileNotFoundError:
    print(f"❌ Error: The file '{input_file}' was not found.")
    exit()
except json.JSONDecodeError as e:
    print(f"❌ Error: Failed to decode JSON - {e}")
    exit()

# DeepSeek API Setup
API_KEY = "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"  # Replace with your actual API key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to check for a local response using fuzzy matching
def get_local_response(user_input):
    best_match = None
    highest_score = 0

    for entry in local_data:
        score = fuzz.token_sort_ratio(user_input.lower(), entry["prompt"].lower())
        if score > 70:  # Lower threshold for better flexibility
            if score > highest_score:
                highest_score = score
                best_match = entry["completion"]

    if best_match:
        logging.info(f"Local Match Found: {best_match}")
        print(f"✅ Using Local Data: {best_match}")
    return best_match if best_match else None

# Function to call DeepSeek API
def call_deepseek_api(user_input):
    global conversation_history

    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Prepare payload with conversation history
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "system", "content": "You are an assistant for East Central University (ECU) in Ada, Oklahoma."},
            *conversation_history
        ],
        "temperature": 0.3,
        "max_tokens": 400
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        answer = data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
        conversation_history.append({"role": "assistant", "content": answer})
        logging.info(f"DeepSeek API Response: {answer}")
        return answer
    except requests.exceptions.Timeout:
        return "⚠️ Error: The response took too long. Please try again."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {e}"

# Simulate typing delay
def simulate_typing(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# Chatbot Interface
def chatbot():
    global conversation_history
    conversation_history = []

    print("🚀 ECU Chatbot: Ask me anything about East Central University! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # Get response from local data or DeepSeek API
        local_answer = get_local_response(user_input)
        if local_answer:
            response = local_answer
        else:
            response = call_deepseek_api(user_input)

        # Simulate typing for a more natural conversation
        print("ECU Bot: ", end="")
        simulate_typing(response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()'''


import requests
import json
from fuzzywuzzy import fuzz
import time
import logging

# Logging setup
logging.basicConfig(filename="ecu_chatbot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load local datasets (Both JSON Files)
finetune_file = "ecu_finetune_dataset.json"
qa_pairs_file = "qa_pairs.json"

try:
    with open(finetune_file, "r", encoding="utf-8") as file:
        finetune_data = json.load(file)
except FileNotFoundError:
    print(f"❌ Error: The file '{finetune_file}' was not found.")
    finetune_data = []
except json.JSONDecodeError as e:
    print(f"❌ Error: Failed to decode JSON - {e}")
    finetune_data = []

try:
    with open(qa_pairs_file, "r", encoding="utf-8") as file:
        qa_data = json.load(file)
except FileNotFoundError:
    print(f"❌ Error: The file '{qa_pairs_file}' was not found.")
    qa_data = []
except json.JSONDecodeError as e:
    print(f"❌ Error: Failed to decode JSON - {e}")
    qa_data = []

# Combine both datasets for searching
local_data = finetune_data + qa_data

# DeepSeek API Setup
API_KEY = "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"  # Replace with your actual API key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to check for a local response using fuzzy matching
def get_local_response(user_input):
    best_match = None
    highest_score = 0

    for entry in local_data:
        prompt = entry.get("prompt", "").strip()
        completion = entry.get("completion", "").strip()

        if not prompt or not completion:
            continue  # Skip entries with missing values

        score = fuzz.token_sort_ratio(user_input.lower(), prompt.lower())
        if score > 75:  # Adjustable threshold for better accuracy
            if score > highest_score:
                highest_score = score
                best_match = completion

    if best_match:
        logging.info(f"✅ Local Match Found: {best_match}")
        print(f"✅ Using Local Data: {best_match}")
    return best_match if best_match else None

# Function to call DeepSeek API
def call_deepseek_api(user_input):
    global conversation_history

    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Prepare payload with conversation history
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "system", "content": "You are an assistant for East Central University (ECU) in Ada, Oklahoma."},
            *conversation_history
        ],
        "temperature": 0.3,
        "max_tokens": 400
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        answer = data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")

        conversation_history.append({"role": "assistant", "content": answer})
        logging.info(f"✅ DeepSeek API Response: {answer}")
        return answer
    except requests.exceptions.Timeout:
        return "⚠️ Error: The response took too long. Please try again."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {e}"

# Simulate typing delay
def simulate_typing(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# Chatbot Interface
def chatbot():
    global conversation_history
    conversation_history = []

    print("🚀 ECU Chatbot: Ask me anything about East Central University! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # Get response from local data or DeepSeek API
        local_answer = get_local_response(user_input)
        if local_answer:
            response = local_answer
        else:
            response = call_deepseek_api(user_input)

        # Simulate typing for a more natural conversation
        print("ECU Bot: ", end="")
        simulate_typing(response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()



