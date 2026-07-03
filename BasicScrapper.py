import requests
import sys

url="https://quotes.toscrape.com"
sys.stdout.reconfigure(encoding='utf-8')

response=requests.get(url)
print(response.status_code)
print(response.text)
if response.status_code==200:
    print("Success")


#python -> GetRequests ->url -> Html response -> Page
