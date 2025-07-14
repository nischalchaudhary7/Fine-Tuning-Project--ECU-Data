import json
import re

# Load the dataset
input_file = "ecu_finetune_dataset.json"
output_file = "ecu_finetune_dataset_cleaned.json"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        qa_data = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON - {e}")
    exit()

# Define proper question templates
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

# Function to clean text data
def clean_text(text):
    text = re.sub(r"\s+", " ", text.strip())  # Normalize spaces
    text = text.replace("\n", " ").replace("\r", "")  # Remove new lines
    return text

# Function to shorten long responses while preserving key information
def truncate_answer(answer, max_length=250):
    """Truncate long answers but ensure they don't cut off mid-sentence."""
    if len(answer) <= max_length:
        return answer  # Keep short answers as they are
    
    truncated = answer[:max_length].rsplit(".", 1)[0]  # Cut at last full sentence
    return truncated + "." if truncated else answer[:max_length]  # Ensure proper ending

# Remove duplicates and improve structure
seen_questions = set()
formatted_data = []

for entry in qa_data:
    topic = entry.get("prompt", "").strip()
    answer = entry.get("completion", "").strip()
    source_url = entry.get("source_url", "")

    if topic and answer:
        cleaned_answer = clean_text(truncate_answer(answer))  # Shorten responses
        
        for template in question_templates:
            question = template.format(topic)
            
            # Avoid duplicate questions
            if question.lower() not in seen_questions:
                seen_questions.add(question.lower())

                # Define response type
                response_type = "short-answer" if len(cleaned_answer.split()) < 30 else "detailed-answer"

                formatted_data.append({
                    "prompt": question,
                    "completion": cleaned_answer,
                    "response_type": response_type,
                    "source_url": source_url
                })

# Save the optimized dataset
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(formatted_data, file, indent=4, ensure_ascii=False)

print(f"✅ Successfully cleaned dataset and saved as '{output_file}'.")
