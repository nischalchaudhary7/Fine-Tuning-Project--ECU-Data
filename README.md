# Fine-Tuning-Project--ECU-Data



 ECU AI Chatbot \& Web Scraper Project



Welcome to the ECU Chatbot project! This is a fully functional AI chatbot built to help students, faculty, and visitors get accurate, real-time answers about \*\*East Central University (ECU)\*\*. From academic programs and admissions to scholarships, events, housing, and more — this chatbot has you covered.



---



\## What This Project Does



\- \*\*Scrapes\*\* over 30,000+ ECU web pages using Python and BeautifulSoup

\- \*\*Categorizes\*\* content into structured sections like Academics, Admissions, Scholarships, etc.

\- \*\*Generates NLP-style Q\&A pairs\*\* from raw content using smart templates

\- \*\*Runs a chatbot\*\* that:

&nbsp; - Answers questions from a fine-tuned local dataset

&nbsp; - Falls back to \*\*DeepSeek API\*\* if no local match is found

\- \*\*Visualizes data\*\* with charts showing how information is distributed

\- \*\*Automates updates\*\* daily using the `schedule` module



---



\## Project Structure



 Finetuning/

├── datarefining.py # Scrapes homepage links

├── mainrefine.py # Recursive scraping from ECU pages

├── structured.py # Categorizes scraped links

├── analyze.py # Generates bar + pie charts of categories

├── ecu\_qa\_generator.py # Generates Q\&A pairs from scraped content

├── ecu\_qa\_data2.py # Cleans/formats data for fine-tuning

├── ecu\_chatbot.py # Main chatbot logic (local + DeepSeek)

├── automated\_scraping.py # Runs scraping jobs daily at set times

├── requirements.txt # Python dependencies

├── README.md # This file

└── .gitignore # Ignore unneeded files



yaml



---



\## 🔧 How to Run It



\### 1. Clone the Repository



```bash

git clone https://github.com/nischalchaudhary7/Fine-Tuning-Project--ECU-Data.git

cd Fine-Tuning-Project--ECU-Data



2\. Install Required Libraries

pip install -r requirements.txt



3\. Run Web Scraping



python datarefining.py

python mainrefine.py

python structured.py



4\. Generate Q\&A Dataset



python ecu\_qa\_generator.py

python ecu\_qa\_data2.py



5\. Launch the Chatbot



python ecu\_chatbot.py

💬 Sample Chat

plaintext

You: What scholarships are available for freshmen?

ECU Bot: ✅ Using Local Data: ECU offers a variety of freshman scholarships including academic and needs-based options. You can apply through the ECU scholarships portal.

📈 Visual Output

Run:



python analyze.py

Outputs:



category\_counts.png: Bar + Pie charts



category\_counts.csv: Raw numbers per category



Large Dataset

The cleaned fine-tuning dataset was too large for GitHub’s 100MB limit.



 You can download it here:

Download Cleaned Dataset (360MB)



(Replace this with your actual Google Drive link)



API Key Setup

To use the DeepSeek fallback:



Open ecu\_chatbot.py



Replace this line:



API\_KEY = "your-api-key-here"

Sign up for a free key at openrouter.ai



Tech Stack

Python



BeautifulSoup



Requests



Pandas



Matplotlib



FuzzyWuzzy



DeepSeek API (via OpenRouter)



JSON for data storage



Schedule (for automation)



Automation Schedule

Set up automated scraping:



python automated\_scraping.py

Runs datarefining.py daily at 7:00 AM



Runs mainrefine.py daily at 8:00 AM



Future Plans

Host chatbot as a web app (Flask or React.js)



Add a real-time database and search filtering



Fine-tune with more conversational data



Integrate LangChain for advanced memory



License

This project is open source under the MIT License.



🙌 Acknowledgements

Special thanks to East Central University for providing a rich dataset of public-facing resources.

