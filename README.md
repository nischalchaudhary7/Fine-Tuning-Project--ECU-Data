This project is focused on building a ChatGPT-like application that provides detailed information about East Central University (ECU). The app is designed to respond to user queries regarding various aspects of the university, such as academics, admissions, events, student services, housing, and more. The project aims to simplify access to university-related information by using refined, categorized, and analyzed web data.

Project Objectives
Data Collection: Scrape all publicly available information from the East Central University website and affiliated sources.
Data Refinement: Process, clean, and organize the collected data into meaningful categories for easier accessibility.
Data Analysis and Visualization: Analyze the categorized data to uncover insights, identify gaps, and visualize patterns using charts and graphs.
Build an Intelligent Chat Application: Use the refined dataset to train a domain-specific chatbot capable of answering questions about ECU.
Project Workflow
1. Data Scraping
Utilized Python libraries such as BeautifulSoup and requests to scrape ECU’s website for detailed information.
Extracted over 30,000 links from multiple layers of the website (depth 1, depth 2, and depth 3).
Saved the scraped data in JSON format for further processing.
2. Data Refinement
Processed the raw data to clean up irrelevant links, resolve duplicates, and format the information.
Divided the data into meaningful categories such as:
Academics
Admissions
Events
News
Athletics
Student Services
Housing
Social Media
Emergency Procedures
External Resources
Created rules to automatically categorize uncategorized links using Python.
3. Data Analysis
Analyzed the categorized data to generate insights:
Counted the number of links per category.
Identified uncategorized or miscategorized links for refinement.
Saved the category counts to a CSV file for easy sharing and further use.
4. Data Visualization
Visualized the data using Python libraries like Matplotlib and Pandas.
Created bar charts and pie charts to represent:
The number of links in each category.
The percentage breakdown of categories.
Saved the visualizations as images for documentation and presentations.
Next Steps
With the data refined, analyzed, and visualized, the next phase of the project involves:

Chatbot Development:
Use the refined data to build a domain-specific chatbot capable of answering questions about East Central University.
Implement a fine-tuning process with OpenAI's GPT models for ECU-specific knowledge.
Deployment:
Deploy the chatbot as a web application using frameworks like Flask or Django.
Host the app on a cloud platform for public use.
Interactive Dashboard:
Develop a dashboard for real-time data visualization and chatbot usage metrics.
Continuous Data Updates:
Automate the scraping process to keep the dataset updated with new information.
Technologies Used
Web Scraping: BeautifulSoup, Requests
Data Processing: Python, JSON
Data Visualization: Matplotlib, Pandas
Data Storage: JSON, CSV
Current Status
Completed data scraping, refinement, and categorization.
Successfully visualized the dataset with insights on link distributions and categories.
Ready to begin developing the ChatGPT-like application for querying ECU information.
