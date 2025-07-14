import schedule
import time
import subprocess

# Define a function to run the datarefining script
def run_datarefining():
    try:
        print("Starting the data refining process...")
        subprocess.run(["python", "datarefining.py"], check=True)
        print("Data refining completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during data refining: {e}")

# Define a function to run the mainrefine script
def run_mainrefine():
    try:
        print("Starting the main refining process...")
        subprocess.run(["python", "mainrefine.py"], check=True)
        print("Main refining completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during main refining: {e}")

# Schedule the data refining script to run daily at 07:00 AM
schedule.every().day.at("07:00").do(run_datarefining)

# Schedule the main refining script to run daily at 08:00 AM
schedule.every().day.at("08:00").do(run_mainrefine)

print("Automated scraper initialized. Waiting for scheduled times...")
while True:
    schedule.run_pending()
    time.sleep(1)
