Fine-Tuning-Project — ECU Data
AI Chatbot & Intelligent Web Scraping System for East Central University

1. Overview

Fine-Tuning-Project — ECU Data is an end-to-end AI-powered university chatbot system designed to provide accurate, real-time, and context-aware answers about East Central University (ECU).

The system combines:

Large-scale web scraping

Data analysis & visualization

NLP-style Q&A generation

Fuzzy matching

LLM fallback (DeepSeek API)

This project helps students, faculty, and visitors easily access information about:
academics, admissions, scholarships, housing, events, student services, and more.

2. Key Features
Automated Web Scraping

-Scraped 30,000+ ECU webpages

-Recursive, multi-depth crawling

-Extracts titles, paragraphs, and internal links

3. Intelligent Data Structuring

- Categorizes pages into 20+ university domains

- Cleans noisy web content

- Removes duplicates and broken links

4. NLP-Style Q&A Dataset Generation

- Converts raw content into question-answer pairs

- Supports short, medium, and detailed responses

- Optimized for fine-tuning & inference

5. Hybrid Chatbot Architecture

- Local Dataset First (fast + accurate)

- Fuzzy Matching for paraphrased queries

- DeepSeek API fallback for unseen questions

6. Data Analysis & Visualization

- Bar charts & pie charts showing content distribution

- CSV export for further analytics

7. Fully Automated Updates

- Scheduled scraping & refinement

- Keeps dataset fresh and up-to-date

8. Project Architecture
Fine-Tuning-Project--ECU-Data/

├── datarefining.py           # Initial homepage scraping

├── mainrefine.py             # Recursive deep scraping

├── structured.py             # Category-based organization

├── analyze.py                # Data analysis & visualization

├── ecu_qa_generator.py       # Q&A dataset generation (NLP format)

├── ecu_qa_data2.py           # Dataset cleaning & optimization

├── ecu_chatbot.py            # Chatbot logic (local + DeepSeek)

├── automated_scraping.py     # Scheduled automation (daily jobs)

├── requirements.txt          # Python dependencies

├── README.md                 # Documentation

└── .gitignore                # Ignored files

10. Tech Stack

Programming & Libraries, Python 3.9+, BeautifulSoup, Requests, Pandas, Matplotlib, FuzzyWuzzy, JSON, AI & NLP, DeepSeek R1 (via OpenRouter)
Prompt-Response Fine-Tuning, Fuzzy Token Matching, Automation, Schedule, Subprocess, Visualization, Bar Charts, Pie Charts, CSV Export

*How to Run the Project
1. Clone the Repository
git clone https://github.com/nischalchaudhary7/Fine-Tuning-Project--ECU-Data.git
cd Fine-Tuning-Project--ECU-Data

2. Install Dependencies
pip install -r requirements.txt

3. Run Web Scraping Pipeline
python datarefining.py
python mainrefine.py
python structured.py

4. Generate NLP Q&A Dataset
python ecu_qa_generator.py
python ecu_qa_data2.py

5. Launch the Chatbot
python ecu_chatbot.py

6. Sample Chat
You: What scholarships are available for freshmen?

ECU Bot: Using Local Data:
ECU offers a variety of freshman scholarships including academic and need-based awards. Applications are available through the ECU Scholarships Portal.

7. Data Visualization

Generate analytics:

python analyze.py


Outputs

category_counts.png → Bar & Pie Charts

category_counts.csv → Raw statistics

* Large Dataset Notice

Due to GitHub’s 100MB file limit, the cleaned fine-tuning dataset is hosted externally.

Download Dataset (≈360MB):
Add your Google Drive link here

* API Key Setup (DeepSeek)

Open ecu_chatbot.py

Replace:

API_KEY = "your-api-key-here"


Get a free API key from:
https://openrouter.ai

* Automated Scraping

Start scheduled updates:

python automated_scraping.py


Runs Automatically

datarefining.py → 7:00 AM

mainrefine.py → 8:00 AM

Future Enhancements

- Web UI (Flask / React)

- Semantic Search (Embeddings)

- Memory-based Conversations

- Real-time Database Integration

- LangChain / RAG Architecture

License

This project is licensed under the MIT License — free to use, modify, and distribute.

*Acknowledgements

East Central University — for publicly available resources

OpenRouter & DeepSeek — LLM infrastructure

Open-source Python community

