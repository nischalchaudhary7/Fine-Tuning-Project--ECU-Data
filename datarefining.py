'''In this code I have installed Beautiful Soup which helps to collect data from webite. It has collecetd all the data that
persent in ECU first page. Thre were many hyper links in the ecu first page and it shows there in the terminal if I write python.py'''

import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = "https://www.ecok.edu/"

# Send HTTP request
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to access the website. Status code: {response.status_code}")
    exit()

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract unique links
unique_links = set()
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('/'):
        href = url + href.lstrip('/')
    if href.startswith('http'):
        unique_links.add(href)

# Print links
print(f"Total unique links found: {len(unique_links)}")
for link in unique_links:
    print(link)

# Save links to a text file
with open("ecu_links.txt", "w") as text_file:
    for link in unique_links:
        text_file.write(link + "\n")

# Save links to a JSON file
with open("ecu_links.json", "w") as json_file:
    json.dump(list(unique_links), json_file, indent=4)

print("Links have been saved to 'ecu_links.txt' and 'ecu_links.json'")





'''From this code I am going in second hyper link of the webiste. such as Scholarhsip, Housing, International Students. I am going
to write the code below.'''

'''# Read links from file
with open("ecu_links.txt", "r") as file:
    all_links = [line.strip() for line in file.readlines()]

# Categorize links
categories = {
    "academic_calendar": [link for link in all_links if "calendar" in link],
    "events": [link for link in all_links if "event" in link],
    "scholarships": [link for link in all_links if "scholarship" in link],
    "departments": [link for link in all_links if "departments" in link or "programs" in link],
    "news": [link for link in all_links if "news" in link],
    "student_services": [link for link in all_links if "services" in link],
    "general_info": [link for link in all_links if "about" in link or "map" in link],
    "international_students": [link for link in all_links if "international" in link],
    "housing": [link for link in all_links if "housing" in link],
    "athletics": [link for link in all_links if "athletics" in link or "sports" in link],
    "clubs": [link for link in all_links if "clubs" in link or "organizations" in link]
}

# Print categorized links
for category, links in categories.items():
    print(f"{category}: {len(links)} links")

"""If I want to know what kind of hyper links are there in one section such as of events There were 11 hyper links and to know it 
I wrote this code."""

"""# Print links in the "events" category
print("Event Links:")
for link in categories["events"]:
    print(link)

# Save event links to a separate file
with open("event_links.txt", "w") as file:
    for link in categories["events"]:
        file.write(link + "\n")

print("Event links have been saved to event_links.txt.")

# Print links in the "events" category
print("academic_calendar:")
for link in categories["academic_calendar"]:
    print(link)

# Save event links to a separate file
with open("academic_calendar_links.txt", "w") as file:
    for link in categories["academic_calendar"]:
        file.write(link + "\n")

print("Event links have been saved to academic_calendar_links.txt.")"""

# Print links in the "events" category
print("scholarships:")
for link in categories["scholarships"]:
    print(link)

# Save event links to a separate file
with open("scholasrships_links.txt", "w") as file:
    for link in categories["scholarships"]:
        file.write(link + "\n")

print("Scholarships links have been saved to scholarships_links.txt.")'''






