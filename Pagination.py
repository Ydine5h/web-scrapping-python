from bs4 import BeautifulSoup
import requests
import csv

file = open("quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["Quote", "Author", "Tags"])

url = "https://quotes.toscrape.com"

while True:

    print(f"Scraping: {url}")

    page = requests.get(url)

    if page.status_code != 200:
        print("Request Failed")
        break

    soup = BeautifulSoup(page.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        quote_text = quote.find("span", class_="text").text

        author = quote.find("small", class_="author").text

        tag_objects = quote.find_all("a", class_="tag")

        tags = []

        for tag in tag_objects:
            tags.append(tag.text)

        writer.writerow([
            quote_text,
            author,
            ",".join(tags)
        ])

    # Find Next button (only once per page)
    next_button = soup.find("li", class_="next")

    if next_button is None:
        print("No more pages")
        break

    # Get next page URL
    next_page = next_button.find("a")["href"]

    # Build complete URL
    url = "https://quotes.toscrape.com" + next_page

file.close()

print("Scraping Completed!")