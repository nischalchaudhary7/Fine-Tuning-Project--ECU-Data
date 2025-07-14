"""This code covrerts ecu_full_scrape.json file to better Q/A fomart tinto better NLP format. now """

import json
import re

# Load the scraped ECU website data
input_file = "ecu_full_scrape.json"
output_file = "ecu_qa_dataset.json"

# Load JSON data
with open(input_file, "r", encoding="utf-8") as file:
    scraped_data = json.load(file)

# Expanded Question Templates
question_templates = [
    "What is {}?",
    "Can you explain {}?",
    "Tell me about {}.",
    "Where can I find information about {}?",
    "Who should I contact for {}?",
    "How do I apply for {}?",
    "What are the requirements for {}?",
    "When does {} take place?",
    "How much does {} cost?",
    "Is {} available online?",
    "Where is {} located?",
    "What are the benefits of {}?",
    "What documents do I need for {}?",
    "What are the deadlines for {}?",
    "How does {} work?",
    "What courses are included in {}?",
    "Give me an overview of {}.",
    "How do I enroll in {}?",
    "What is the history of {}?",
    "Are there scholarships for {}?",
    "What financial aid options exist for {}?",
    "What extracurricular activities are available for {}?",
    "How can I join {}?",
    "What career opportunities are available for {} graduates?",
]

# Function to clean and format text
def clean_text(text):
    text = re.sub(r"\s+", " ", text.strip())  # Normalize spaces
    text = text.replace("\n", " ").replace("\r", "")  # Remove new lines
    return text

# Generate Q&A pairs with short, detailed, and list-based answers
qa_pairs = []
for page in scraped_data:
    title = page.get("title", "").strip()
    paragraphs = page.get("paragraphs", [])
    
    if title and paragraphs:
        content = " ".join(paragraphs)
        clean_content = clean_text(content)
        
        for template in question_templates:
            question = template.format(title)

            # Generate different types of responses
            if len(clean_content.split()) < 20:
                answer = clean_content  # Short answer
            elif len(clean_content.split()) < 50:
                answer = clean_content[:300]  # Medium-length response
            else:
                answer = clean_content[:500]  # Detailed response

            # Ensure the response isn't cut mid-sentence
            if len(clean_content) > 500:
                answer = answer.rsplit(".", 1)[0] + "."

            qa_pairs.append({
                "question": question,
                "answer": answer,
                "source_url": page["url"]
            })

# Save Q&A dataset
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(qa_pairs, file, indent=4, ensure_ascii=False)

print(f"✅ NLP Q&A dataset saved as '{output_file}'.")


