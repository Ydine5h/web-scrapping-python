'''

CSV- Comma seperated values-Eg Quote,Author->open it in excel looks like table

'''

from bs4 import BeautifulSoup
import requests
import csv
import sys

#Fix UTF-8 printing in window terminal
sys.stdout.reconfigure(encoding="utf-8")

#step 1- send requests to website
url="https://quotes.toscrape.com"
page=requests.get(url)

#step 2: Check whether request succeeded
if page.status_code==200:
    print("Success")
else:
    print("Request failed")
    exit()

#Parse HTML
soup=BeautifulSoup(page.text,"html.parser")
#step 4 Find all quote blocks
quotes=soup.find_all("div",class_="quote")
#print(quotes)
#step 5 Create csv file
file=open("quotes.csv","w",newline="",encoding="utf-8")
#step 6 create CSV writer object
writer=csv.writer(file)
#step 7 Write Header
writer.writerow(["Quote","Author","Tags"])
#step 8 Loop through every quote
for quote in quotes:
    #Extract Quote
    quote_text=quote.find("span",class_="text").text
    #Extract Author
    author=quote.find("small",class_="author").text
    #tags
    tag_objects=quote.find_all("a",class_="tag")
    tags=[]
    for tag in tag_objects:
        tags.append(tag.text)
    #Write one row into CSV
    writer.writerow([
        quote_text,
        author,
        ",".join(tags)
    ])
#step 9: close file
file.close()

print("Scrapping completed Successfully")