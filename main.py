import requests
import os
from bs4 import BeautifulSoup

PAGE_ROOT = "http://books.toscrape.com"
IMAGES_DIR = "images"
BOOK = "li.col-xs-6.col-sm-4.col-md-3.col-lg-3"
TITLE = "article.product_pod h3 a"
PRICE = "article.product_pod div.product_price p.price_color"
IMG = "article.product_pod div.image_container a img"


def download_image(url, counter):
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    content_img = requests.get(url).content
    with open(f"{IMAGES_DIR}/book_0{counter}.png", mode="wb") as file:
        file.write(content_img)


page_content = requests.get(PAGE_ROOT).content

soup = BeautifulSoup(page_content, "html.parser")
books = soup.select(BOOK)

for counter, book in enumerate(books, start=1):
    title = book.select_one(TITLE).attrs["title"]
    price = book.select_one(PRICE).string
    img = book.select_one(IMG).attrs["src"]
    download_image(f"{PAGE_ROOT}/{img}", counter)
