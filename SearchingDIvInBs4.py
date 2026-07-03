import requests
import sys
from bs4 import BeautifulSoup


url="https://quotes.toscrape.com"
sys.stdout.reconfigure(encoding='utf-8')

response=requests.get(url)
print(type(response))
print(type(response.text))
page=BeautifulSoup(response.text,"html.parser")
print(type(page))
print(type(page.text))
quotes=page.find_all("div",class_="quote") #str same as response.text
'''
quotes=page.find_all("div",class_="quote")
# print(type(quotes)) #ResultSet is container to hold a block of quotes that we have fetched
# len(quotes) #return len coz it behave likes a list
# for quote in quotes:
#     print(quote)
# print(type(quotes[0])) #returns element tag
'''
first=quotes[0]
print(first.prettify())
'''
for quote in quotes:
    quote_tag=quote.find("span")
    author_tag=quote.find("small")
    print(quote_tag.text)
    print(author_tag.text)
    print("--------------")
'''
for quote in quotes:
    quote_text=quote.find("span").text
    author=quote.find("small").text
    tag_objects=quote.find_all("a",class_="tag")
    tags=[]
    for tag in tag_objects:
        tags.append(tag.text)
    print(f"Quote: {quote_text}")
    print(f"Author: {author}")
    print("Tags:",",".join(tags))
    print("-"*60)