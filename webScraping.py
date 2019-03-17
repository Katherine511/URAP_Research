import requests
import re
import csv
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

page = requests.get("https://en.wikipedia.org/wiki/List_of_companies_of_the_United_States_by_state")
root = "https://en.wikipedia.org"
soup = bs4.BeautifulSoup(page.text, 'html.parser')

listed = soup.find_all(class_ = "div-col columns column-width")
companyLinks, companyNames = [], []
for each in listed:
    companyLinks += each.find_all("a")
    for each in companyLinks:
        companyNames.append(each.text)
        
# Getting hyperlinks      
hyperlinked = soup.find_all(class_ = "hatnote navigation-not-searchable")
hyperlink = []
for link in hyperlinked:
    hyperlink.append(link.find('a')['href'])

# Getting a list of company names from hyperlink 
for link in hyperlink:
    page = requests.get(root + link)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    for each in soup.find_all(class_ = "mw-parser-output"):
        companyLinks += each.find_all("a")
        for each in companylinks:
            companyNames.append(each.text)

# Data cleaning for a list of company names 
clean = []
for name in companyNames:
    clean.append(name.replace(" ", "_"))
clean_names = pd.DataFrame(clean)
clean = clean_names.drop_duplicates()
np.savetxt(r'clean.txt', clean[[0]], '%s')




