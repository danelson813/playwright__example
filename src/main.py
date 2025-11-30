# playwright__example/src/main.py


import aiohttp
import asyncio
from bs4 import BeautifulSoup
from src.helpers.playwright_ import save_dicts_to_file

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape(urls):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        pages_content = await asyncio.gather(*tasks)
        for content in pages_content:
            soup = BeautifulSoup(content, 'lxml')
            titles = soup.find_all('h2')  # Adjust selector as needed
            prices = soup.find_all('span', class_="jsx-f0e60c587809418b sale-price text-std-gray-600 font-bold")
            for title, price in zip(titles, prices):
                result = {'title': title.get_text(), 'price': float(price.get_text().replace('From $', '').replace('$','').replace(',', ''))}
                results.append(result)

        return results


urls = [f"https://www.guitarcenter.com/Black-Friday-Electric-Guitar-Deals.gc?icid=LP12630&filters=categories.lvl0:Guitars&page={i}#paginationTopAnchor" for i in range(1, 11)]

if __name__ == "__main__":
    list_ = asyncio.run(scrape(urls))
    for item in list_:
        print(item)
    save_dicts_to_file((list_))
