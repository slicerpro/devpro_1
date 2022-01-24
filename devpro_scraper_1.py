import requests as req
from bs4 import BeautifulSoup as bs

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

response = req.get(url, verify=False)
soup = bs(response.content, "html.parser")
title = soup.find("h1")

print("The headline is " + title.text)
