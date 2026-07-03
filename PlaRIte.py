from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser=p.chromium.launch(headless=False)

    page=browser.new_page()

    page.goto("https://quotes.toscrape.com")

    print(page.title())
    
    browser.close()

    '''
from playwright.sync_api import sync_playwright
import playwright like import requests
--with sync_playwright() as p:
starts playwright PowerON
--browser=p.chromium.launch(headless=False)
lauches chrome and shows browser coz headless is false
--page=browser.new_page()
imagine clicking new tab
--page.goto(url)
exactly like typing www.google.com
--print(page.title())
gets Quotes to scrape
--browser.close()
closes chrome
    '''