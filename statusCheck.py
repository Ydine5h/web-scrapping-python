page = requests.get("https://quotes.toscrape.com", verify=False)
print(page.status_code)
