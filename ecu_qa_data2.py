"""It converts ecu_qa_data.py into fine tuning format """

import json
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load the cleaned Q&A dataset
input_file = "ecu_qa_dataset.json"
output_file = "ecu_finetune_dataset.json"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        qa_data = json.load(file)
except FileNotFoundError:
    logging.error(f"The file '{input_file}' was not found.")
    exit()
except json.JSONDecodeError as e:
    logging.error(f"Failed to decode JSON - {e}")
    exit()

# Improved Question Templates
question_templates = [
    "What is {}?",
    "Tell me about {}.",
    "Can you explain {}?",
    "How does {} work?",
    "Where is {} located?",
    "What are the requirements for {}?",
    "What is the cost of {}?",
    "Who should I contact about {}?",
    "Is {} available online?",
    "How can I apply for {}?",
    "What are the benefits of {}?",
    "When is {}?",
    "What courses are included in {}?",
    "Give me an overview of {}.",
]

# Question-specific formatting rules
question_formats = {
    "cost": "The cost for {} is {}",
    "requirements": "The requirements for {} are {}",
    "contact": "You should contact {} for more information about {}",
    "benefits": "The benefits of {} include {}",
    "courses": "The courses included in {} are {}",
    "overview": "Here is an overview of {}: {}",
}

# Function to clean text data
def clean_text(text):
    text = re.sub(r"\s+", " ", text.strip())
    text = text.replace("\n", " ").replace("\r", "")
    text = re.sub(r"[^\w\s.,!?]", "", text)
    return text.lower()

# Function to truncate long answers
def truncate_answer(answer, max_length=300):
    if len(answer) <= max_length:
        return answer
    truncated = answer[:max_length].rsplit(".", 1)[0]
    if len(truncated) < len(answer):
        truncated += "..."
    return truncated

# Function to format the answer based on the question type
def format_answer(question, topic, answer):
    for key, format_str in question_formats.items():
        if key in question.lower():
            return format_str.format(topic, answer)
    return answer

# Function to classify response type
def classify_response_type(answer):
    if len(answer.split()) < 30:
        return "short-answer"
    elif "overview" in answer.lower() or "include" in answer.lower():
        return "detailed-answer"
    else:
        return "short-answer"

# Function to validate entries
def is_valid_entry(question, answer):
    if not question or not answer:
        return False
    if len(answer.split()) < 5:
        return False
    return True

# Process the dataset
seen_questions = {}
formatted_data = []

for entry in qa_data:
    topic = entry.get("question", "").strip()
    answer = entry.get("answer", "").strip()
    source_url = entry.get("source_url", "")

    if topic and answer:
        cleaned_answer = clean_text(truncate_answer(answer))

        for template in question_templates:
            question = template.format(topic)

            if question.lower() not in seen_questions:
                seen_questions[question.lower()] = cleaned_answer
                cleaned_answer = format_answer(question, topic, cleaned_answer)
                response_type = classify_response_type(cleaned_answer)

                if is_valid_entry(question, cleaned_answer):
                    formatted_data.append({
                        "prompt": question,
                        "completion": cleaned_answer,
                        "response_type": response_type,
                        "source_url": source_url
                    })

# Save the optimized dataset
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(formatted_data, file, indent=4, ensure_ascii=False)

logging.info(f"✅ Successfully optimized dataset and saved as '{output_file}'.")




