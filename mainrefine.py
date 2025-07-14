import requests
from bs4 import BeautifulSoup
import json
import time

# Set headers to mimic a browser (optional)
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Function to scrape a single URL
def scrape_url(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Extract data (modify based on site structure)
            page_title = soup.title.string.strip() if soup.title else "No Title"
            paragraphs = [p.text.strip() for p in soup.find_all("p")]
            links = [a["href"] for a in soup.find_all("a", href=True)]

            return {
                "url": url,
                "title": page_title,
                "paragraphs": paragraphs,
                "links": links,
            }
        else:
            print(f"Failed to fetch {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

# Recursive scraper
def recursive_scrape(start_urls, depth=2):
    visited = set()
    data = []

    def scrape_recursive(url, current_depth):
        if url in visited or current_depth > depth:
            return
        visited.add(url)

        page_data = scrape_url(url)
        if page_data:
            data.append(page_data)
            # Recursively scrape linked pages
            for link in page_data["links"]:
                if link.startswith("http"):  # Ensure it's an external link
                    scrape_recursive(link, current_depth + 1)

    for url in start_urls:
        scrape_recursive(url, 0)

    return data

# Start scraping from the first page's links
start_urls = [
    "https://www.ecok.edu/directions",
    "https://www.ecok.edu/apply",
    "https://www.ecok.edu/academics/colleges-and-schools/college-health-and-sciences",
    "https://www.facebook.com/ECUTigerUpdate",
    "https://www.ecok.edu/freshman-scholarships",
    "https://www.ecok.edu/news",
    "https://www.ecok.edu/academics/colleges-and-schools/school-graduate-studies",
    "https://www.ecubookstore.com/home",  # Corrected link
    "https://www.ecok.edu/HC",  # Corrected link
    "https://www.ecok.edu/news/ecu-calls-2025-distinguished-award-nominations",
    "https://www.ecok.edu/photo-galleries",
    "https://www.ecok.edu/funding-reports-cares-crrsaa-and-arp-acts",
    "https://www.ecok.edu/alumni",
    "https://www.ecok.edu/academics/colleges-and-schools",
    "https://www.ecok.edu/",
    "https://www.ecok.edu/academics/colleges-and-schools/college-health-and-sciences/school-nursing",
    "https://www.ecok.edu/academics",
    "https://www.ecok.edu/academics/colleges-and-schools/harland-c-stonecipher-school-business",
    "https://www.ecok.edu/event/full-semester-sp25-begins-sp-25-term-begins",
    "https://www.instagram.com/ecutigers/",
    "https://www.ecok.edu/event/kayla-ohlmer-art-exhibit-2",
    "https://www.ecok.edu/academics/find-major-program",
    "https://www.ecok.edu/involvement/student-clubs-organizations",
    "https://www.ecok.edu/take-a-tour",
    "https://twitter.com/ECUTigerUpdates",
    "https://ecok.wufoo.com/forms/qwxcdak1p3foh8/",
    "https://www.ecok.edu/news/ecu-kicks-2025-looking-forward",
    "https://www.ecok.edu/admissions/transfer-student",
    "https://www.ecok.edu/housing",
    "https://www.youtube.com/user/ECUvideos",
    "https://www.ecok.edu/about-east-central-university/campus-map",
    "https://www.ecok.edu/event/kayla-ohlmer-art-exhibit-3",
    "https://www.ecok.edu/event/martin-luther-king-jr-day-1",
    "https://www.ecok.edu/current-students/paying-college/financial-aid/consumer-information",
    "https://www.ecok.edu/academics/colleges-and-schools/college-liberal-arts-and-social-sciences",
    "https://www.ecok.edu/about-east-central-university",
    "https://www.ecok.edu/donate/ways-give/foundation-scholarship-information",
    "https://www.ecok.edu/news/ecus-online-counseling-degree-recognized-college-consensus",
    "https://www.ecok.edu/academics/catalog",
    "http://ecok.erezlife.com/",
    "https://www.ecok.edu/current-students/student-services/centers-programs/academic-success-center",
    "https://www.ecok.edu/involvement/greek-life",
    "https://www.ecok.edu/admissions/freshman-student",
    "https://www.ecok.edu/login",
    "http://instagram.com/ecutigers/",
    "https://www.ecok.edu/admissions/concurrent-student",
    "https://www.ecok.edu/policies-and-handbooks",
    "https://www.ecok.edu/future-students/request-information",
    "https://www.ecok.edu/tiger-parent-family-central",
    "https://www.ecok.edu/calendar",
    "https://www.ecok.edu/donate",
    "https://www.ecok.edu/about-east-central-university/emergency-procedures",
    "https://www.ecok.edu/academics/colleges-and-schools/college-education-and-psychology",
    "https://www.ecok.edu/current-students/student-services/tommy-hewett-md-wellness-center",
    "https://www.ecok.edu/news/ecu-campus-close-holiday-jan-20-classes-begin-jan-21",
    "https://ecutigers.com/",  # Corrected link
    "https://www.ecok.edu/academics/honors-program",
    "https://www.ecok.edu/involvement",
    "https://ecok.libguides.com/home",
    "https://www.ecok.edu/future-students",
    "https://www.ecok.edu/involvement/intramural/",
    "https://www.ecok.edu/academics/colleges-and-schools/college-liberal-arts-and-social-sciences/school-fine-arts",
    "https://www.ecok.edu/directory",
    "https://www.ecok.edu/academics/study-abroadstudy-away",
    "https://online.ecok.edu/",
    "https://www.ecok.edu/admissions",
    "https://www.ecok.edu/current-students/paying-college",
    "https://www.ecok.edu/current-students/student-services/office-testing-and-accessibility-services",
    "https://www.ecok.edu/employment-services/job-opportunities",
    "https://www.ecok.edu/event/martin-luther-king-jr-day-2",
    "https://www.ecok.edu/sitemap",
    "https://www.ecok.edu/calendar/calendar.asp",
    "https://www.ecok.edu/about-east-central-university/hours-operation",
    "https://www.ecok.edu/current-students/paying-college/financial-aid",
    "https://www.ecok.edu/ecu-tiger-esports",
    "https://www.ecok.edu/current-students",
    "https://www.ecok.edu/current-students/student-services/office-international-student-services",
    "https://www.ecok.edu/ecu-tiger-reporting",
    "https://www.ecok.edu/current-students/student-services/centers-programs",
]

# Perform recursive scraping
scraped_data = recursive_scrape(start_urls, depth=2)

# Save to a JSON file
with open("ecu_full_scrape.json", "w") as file:
    json.dump(scraped_data, file, indent=4)

print("Scraping complete. Data saved to 'ecu_full_scrape.json'.")
