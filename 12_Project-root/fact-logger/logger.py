import requests
import time
import os

# Correct API URL (call the actual API endpoint, not /docs)
FACT_API_URL = "http://fact-generator:8000/fact"  

LOG_DIR = "log"
LOG_FILE = os.path.join(LOG_DIR, "stored_facts.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def fetch_and_store_fact():
    try:
        response = requests.get(FACT_API_URL)
        response.raise_for_status()
        data = response.json()
        fact = data.get("fact", "No fact returned")

        with open(LOG_FILE, "a") as f:
            f.write(fact + "\n")

        print(f"Stored fact: {fact}")

    except Exception as e:
        print(f"Error fetching fact: {e}")
        with open(LOG_FILE, "a") as f:
            f.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    while True:
        fetch_and_store_fact()
        time.sleep(10)  # fetch a new fact every 10 seconds
