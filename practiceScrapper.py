import sys
from bs4 import BeautifulSoup
import csv
import requests
from urllib.parse import urljoin 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
file=open("books.csv","w",newline="",encoding="utf-8")
writer=csv.writer(file)
# Title
# Price
# Availability
# Rating
# Product_URL
# Image_URL
url="https://books.toscrape.com/"
writer.writerow(["Title","Price","Availability","Rating","Product_URL","Image_url"])

while True:
    print(f"printing:  {url}")

    page=requests.get(url,verify=False)

    if page.status_code!=200:
        print("Request Failed")
        break
    soup=BeautifulSoup(page.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    Rating={
        "One":"1",
        "Two":"2",
        "Three":"3",
        "Four":"4",
        "Five":"5"
        }
        
    for book in books:

        title=book.find("h3").find("a")["title"]

        price=book.find("p",class_="price_color").text

        Availability=book.find("p",class_="instock availability").text.strip()

        rating=Rating[book.find("p",class_="star-rating")["class"][-1]]

        productURL=book.find("h3").find("a")["href"]

        imageURL=book.find("div",class_="image_container").find("img")["src"]

        writer.writerow([
            title,
            price,
            Availability,
            rating,
            productURL,
            imageURL

        ]) 
    next_button=soup.find("li",class_="next")

    if next_button is None:
        print("Print NO more pages")
        break

    next_page=next_button.find("a")["href"]
    url=urljoin(url,next_page)

file.close()

print("Successfully Scrapped")

print("hello git")