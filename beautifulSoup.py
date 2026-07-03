# page consists of page.status_code, page.text, page.cookies, page.headers
#website URL-> requests.get(url)->response object(page)->page.text(raw html)->BeautifulSoup(page.text,"html.parser")->Parsed HTML Tree->find(),find_all(),select()
from bs4 import BeautifulSoup
import requests
import sys


url="https://quotes.toscrape.com"
sys.stdout.reconfigure(encoding='utf-8')

page=requests.get(url)
print(page.status_code)
if page.status_code==200:
    print("Success")
else:
    print("Request Failed")
#Parse raw html into a searchable tree structure

test=BeautifulSoup(page.text,"html.parser")

print(type(page))
print(type(page.text))
print(type(test))