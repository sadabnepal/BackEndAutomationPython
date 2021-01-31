import requests
from bs4 import BeautifulSoup

data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = BeautifulSoup(data.content, 'html.parser')
productTable = soup.find('table', {'id': 'product'})
allRows = productTable.findAll('tr')
for allRow in allRows:
    if allRow.find('td'):
        allData = allRow.findAll('td')
        for alltd in allData:
            print(alltd)
