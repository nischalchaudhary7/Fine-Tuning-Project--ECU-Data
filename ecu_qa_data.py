"""This file converts ecu full scrape.josn file into npl Q/A format into json form"""

#please use ecu_qa_generator.py instead of this code.
import json
import re

# Load the scraped data
input_file = "ecu_full_scrape.json"
output_file = "ecu_qa_dataset.json"

# Load JSON data
with open(input_file, "r", encoding="utf-8") as file:
    scraped_data = json.load(file)

# Define relevant question templates
question_templates = {
    "general": [
        "What is {}?",
        "Tell me about {}.",
        "Can you explain {} in detail?",
        "Give me an overview of {}."
    ],
    "admissions": [
        "How do I apply for {}?",
        "What are the requirements for {}?",
        "What is the deadline for {}?",
        "Who can I contact about {}?"
    ],
    "financial_aid": [
        "What scholarships are available for {}?",
        "How do I apply for scholarships related to {}?",
        "What is the cost of {}?",
        "Are there any financial aid options for {}?"
    ],
    "academics": [
        "What courses are included in {}?",
        "Where can I find information about {}?",
        "Is {} available online?",
        "How does {} work?"
    ],
    "location": [
        "Where is {} located?",
        "How do I get to {}?",
        "What are the directions to {}?"
    ],
    "events": [
        "When is {} scheduled?",
        "What are the details of {}?",
        "How can I participate in {}?"
    ]
}

# Function to clean and format text
def clean_text(text):
    text = re.sub(r"\s+", " ", text.strip())  # Normalize spaces
    text = text.replace("\n", " ").replace("\r", "")  # Remove new lines
    return text

# Generate Q&A pairs
qa_pairs = []
for page in scraped_data:
    title = page.get("title", "").strip()
    paragraphs = page.get("paragraphs", [])
    
    if title and paragraphs:
        content = " ".join(paragraphs)
        clean_content = clean_text(content)
        
        # Categorize based on page title
        if any(keyword in title.lower() for keyword in ["apply", "admissions", "enrollment"]):
            category = "admissions"
        elif any(keyword in title.lower() for keyword in ["scholarship", "tuition", "aid", "financial"]):
            category = "financial_aid"
        elif any(keyword in title.lower() for keyword in ["major", "program", "degree", "course"]):
            category = "academics"
        elif any(keyword in title.lower() for keyword in ["location", "map", "directions"]):
            category = "location"
        elif any(keyword in title.lower() for keyword in ["event", "schedule", "calendar"]):
            category = "events"
        else:
            category = "general"
        
        # Generate questions from the category-specific templates
        for template in question_templates[category]:
            question = template.format(title)
            
            # Extract a meaningful response
            answer = clean_content[:600]  # More content for better accuracy
            if len(clean_content) > 600:
                answer = answer.rsplit(".", 1)[0] + "."  # Avoid cutting mid-sentence

            qa_pairs.append({
                "question": question,
                "answer": answer,
                "category": category,
                "response_type": "detailed" if len(answer) > 300 else "short",
                "source_url": page["url"]
            })

# Save Q&A pairs as JSON
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(qa_pairs, file, indent=4, ensure_ascii=False)

print(f"✅ Q&A dataset saved to '{output_file}'.")





