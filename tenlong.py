import requests
from bs4 import BeautifulSoup

URL = "https://www.tenlong.com.tw/zh_tw/recent_bestselling?range=7"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

output = f"{"排行":<5}{"原價":10}{"特價":10}{"書名":20}\n"

for index, book in enumerate(soup.select("li.single-book"), start=1):
    title = book.select_one(".title a").text[:15]
    price = book.select_one(".pricing")
    orig_price, sell_price = price.text.split()
    output += f"{index:<5}{orig_price:10}{sell_price:10}{title:20}\n"

print(output)
