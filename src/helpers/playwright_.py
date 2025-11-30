# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright

"""
Explanation
    •	Importing Playwright: The sync_api module is used for synchronous operations.	
	•	Launching the Browser: You can choose between Chromium, Firefox, or WebKit.
	•	Opening a Page: The script opens a new page in the browser.	
	•	Navigating: It navigates to "https://example.com".	
	•	Taking a Screenshot: The screenshot is saved as "screenshot.png".	
	•	Printing the Title: Outputs the title of the page to the console.
	•	Closing: Finally, it closes the browser and context.

"""

# synchronous
def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True to run in the background
    # Open a new browser context
    context = browser.new_context()
    # Open a new page
    page = context.new_page()

    # Navigate to a website
    page.goto("https://example.com")

    # Take a screenshot
    page.screenshot(path="screenshot.png")

    # Print the page title
    print("Page Title:", page.title())

    # Close the context and browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

# ***********************************************************************

# synchronous
import requests
from bs4 import BeautifulSoup

base_url = 'https://example.com/page/'
for page in range(1, 11):  # Adjust range for more pages
    response = requests.get(f"{base_url}{page}")
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')  # Adjust selector as needed
    for title in titles:
        print(title.get_text())
# ************************************************************

# asynchronous
import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        pages_content = await asyncio.gather(*tasks)
        for content in pages_content:
            soup = BeautifulSoup(content, 'lxml')
            titles = soup.find_all('h2')  # Adjust selector as needed
            for title in titles:
                print(title)
                return title.get_text()

urls = [f"https://www.guitarcenter.com/Black-Friday-Electric-Guitar-Deals.gc?icid=LP12630&filters=categories.lvl0:Guitars&page={i}#paginationTopAnchor" for i in range(1, 11)]
asyncio.run(scrape(urls))


import csv


# Sample list of dictionaries
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 24, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
]
def save_dicts_to_file(list_):
    # Define the fieldnames (CSV headers) based on the dictionary keys
    fieldnames = ["title", "price"]

    # Specify the output CSV file name
    output_file = "results.csv"

    # Open the CSV file in write mode ('w') with newline='' to prevent extra blank rows
    with open(output_file, "w", newline="") as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write all the dictionary rows
        writer.writerows(list_)

    print(f"Data successfully written to {output_file}")


