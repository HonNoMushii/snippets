""" This script scrapes JSON data from a webpage using Selenium and BeautifulSoup.
    It continuously polls the page for new data and saves it to a JSON file.
"""

import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
f

# Set up Firefox options and specify binary & GeckoDriver paths
options = Options()
options.headless = False  # Set to False to see the browser
options.binary_location = r"" # Path to your Firefox.exe
service = Service(r"") # Path to your GeckoDriver.exe

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://www.funda.nl/detail/koop/den-haag/appartement-zodiakplein-69/43885981/")
time.sleep(5)  # Wait for the page to load initially

save_path = "scraped_data.json"
collected_data = []
unique_data_set = set()

print("Starting continuous scraping. The browser will remain open until closed manually.")

# Continuous loop that polls the page for new JSON data
while driver.window_handles:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    json_scripts = soup.find_all("script", type="application/ld+json")
    
    for script in json_scripts:
        try:
            data = json.loads(script.string)
            # Create a sorted string representation to compare duplicates
            data_str = json.dumps(data, sort_keys=True)
            if data_str not in unique_data_set:
                unique_data_set.add(data_str)
                collected_data.append(data)
                print("New data found:")
                print(json.dumps(data, indent=2))
        except Exception as e:
            print("Error parsing JSON from a script tag:", e)
    
    # Save the current unique data to a JSON file
    with open(save_path, "w") as json_file:
        json.dump(collected_data, json_file, indent=2)
    
    time.sleep(5)  # Delay between iterations to reduce load
