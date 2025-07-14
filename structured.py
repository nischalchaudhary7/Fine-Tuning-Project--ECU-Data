import json
from collections import defaultdict

# Load the JSON file with links
with open('ecu_full_scrape.json', 'r') as file:
    links = json.load(file)

# Define the updated categories and subcategories
categories = {
    "Academics": [
        "major", "honors", "study-abroad", "online", "colleges", "nursing", "business", 
        "graduate", "phd", "program", "catalog", "policy"
    ],
    "Admissions": [
        "freshman", "transfer", "international", "financial-aid", "scholarship", 
        "apply", "admissions", "tuition", "fees", "teacherspromise"
    ],
    "Events": [
        "academic", "arts", "athletic", "campus-life", "special", "holiday", "event"
    ],
    "News": [
        "news", "announcement", "recognition", "ranking"
    ],
    "Athletics": [
        "sports", "game", "athletic", "team"
    ],
    "Involvement": [
        "clubs", "organizations", "greek", "esports", "centers", "programs", "intramurals", "involvement"
    ],
    "Student Services": [
        "accessibility", "testing", "international-student", "wellness", 
        "services", "support", "self-service"
    ],
    "Housing": [
        "housing", "residence", "tour"
    ],
    "Future Students": [
        "request-information", "tour", "application", "future-students"
    ],
    "Current Students": [
        "paying-for-college", "schedule", "current-students", "class"
    ],
    "Alumni": [
        "alumni", "giving", "distinguished", "donate", "nominations"
    ],
    "Parents and Families": [
        "parent", "family"
    ],
    "Directions and Maps": [
        "directions", "directory", "map", "location", "hours"
    ],
    "Technology and Tools": [
        "adobe", "erezlife", "selfservice", "forms"
    ],
    "Articulation Agreements": [
        "articulation-agreements", "ssc", "occc", "matrix"
    ],
    "External Resources": [
        "nurses", "nsna", "ncsbn", "nln", "nlm", "homecare", "reader", "tests"
    ],
    "Library": ["library"],
    "Emergency Procedures": ["emergency"],
    "Employment Opportunities": ["employment", "jobs"],
    "Photo Galleries": ["photo"],
    "Social Media": ["facebook", "instagram", "twitter", "linkedin"],
    "General Information": [
        "home", "#", "main-content"
    ]
}

# Categorize links
categorized_links = defaultdict(lambda: defaultdict(list))

for link_entry in links:
    # Extract the URL if the link is a dictionary, otherwise use the string directly
    link = link_entry.get("url") if isinstance(link_entry, dict) else link_entry

    if not isinstance(link, str):  # Skip invalid or unexpected entries
        continue

    categorized = False
    for category, subcategories in categories.items():
        if any(keyword in link.lower() for keyword in subcategories):
            categorized_links[category]["Links"].append(link)
            categorized = True
            break
    if not categorized:
        categorized_links["Uncategorized"]["Links"].append(link)

# Count links in each category
category_counts = {
    category: len(subcats.get("Links", []))
    for category, subcats in categorized_links.items()
}

# Save categorized links and counts to a new JSON file
output = {
    "Categorized Links": {category: subcats for category, subcats in categorized_links.items()},
    "Category Counts": category_counts
}

with open('categorized_ecu_links.json', 'w') as file:
    json.dump(output, file, indent=4)

# Print summary
print("Categorized links saved to 'categorized_ecu_links.json'")
print("\nCategory Counts:")
for category, count in category_counts.items():
    print(f"{category}: {count} links")

# Print Uncategorized Links
uncategorized_links = categorized_links.get("Uncategorized", {}).get("Links", [])
if uncategorized_links:
    print("\nUncategorized Links:")
    for link in uncategorized_links:
        print(link)
    print(f"\nTotal Uncategorized Links: {len(uncategorized_links)}")







