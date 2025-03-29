import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Set up Firefox options and specify binary & GeckoDriver paths
options = Options()
options.headless = False  # Set to False to see the browser
options.binary_location =
service = Service()

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://www.funda.nl/detail/koop/den-haag/appartement-zodiakplein-69/43885981/")
time.sleep(5)  # Wait for the page to load initially

save_path = "scraped_data.json"
collected_data = []
unique_data_set = set()

print("Starting continuous scraping. The browser will remain open until closed manually.")

while driver.window_handles:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    # Create a dictionary to hold all data extracted in this iteration.
    scraped_item = {}

    # 1. Extract JSON-LD data from <script> tags
    json_scripts = soup.find_all("script", type="application/ld+json")
    json_ld_list = []
    for script in json_scripts:
        try:
            data = json.loads(script.string)
            json_ld_list.append(data)
        except Exception as e:
            print("Error parsing JSON from a script tag:", e)
    if json_ld_list:
        scraped_item['json_ld'] = json_ld_list

    # 2. Extract the description text from the designated div
    description_div = soup.find("div", class_="listing-description-text")
    if description_div:
        description = description_div.get_text(strip=True)
        scraped_item['description'] = description
        # Debug: Print the length of the description and write it to a file.
        print("Description length:", len(description))
        with open("description.txt", "w", encoding="utf-8") as f:
            f.write(description)

    # 3. Extract inline JSON data (e.g. __NUXT_DATA__)
    nuxt_data_script = soup.find("script", id="__NUXT_DATA__")
    if nuxt_data_script:
        try:
            nuxt_data = json.loads(nuxt_data_script.string)
            scraped_item['nuxt_data'] = nuxt_data
        except Exception as e:
            print("Error parsing __NUXT_DATA__:", e)

    # Only add this iteration's data if there's any new content.
    if scraped_item:
        # Use a sorted JSON string representation to check for uniqueness.
        item_str = json.dumps(scraped_item, sort_keys=True)
        if item_str not in unique_data_set:
            unique_data_set.add(item_str)
            collected_data.append(scraped_item)
            print("New data found:")
            # Print the entire JSON object (may be truncated in some consoles)
            print(json.dumps(scraped_item, indent=2))

    # Save the current unique data to a JSON file
    with open(save_path, "w", encoding="utf-8") as json_file:
        json.dump(collected_data, json_file, indent=2)
    
    time.sleep(5)  # Delay between iterations to reduce load
