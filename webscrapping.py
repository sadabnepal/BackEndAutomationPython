import requests
from bs4 import BeautifulSoup

li = []
data = requests.get("https://www.imdb.com/find?q=Thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
moviesTable = soup.find('table', {'class': 'findList'})
# print(moviesTable.prettify())
rows = moviesTable.findAll('tr')
for row in rows:
    rowData = row.findAll('td')
    subUrl = rowData[1].a['href']
    subData = requests.get("https://www.imdb.com"+subUrl)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    if childSoup.find('div', {'class': 'see-more inline canwrap'}):
        genre = childSoup.findAll('div', {'class': 'see-more inline canwrap'})
        if genre[1].a.text == " Short":
            print(rowData[1].a.text)
            print(genre[1].a.text)
            li.append(rowData[1].a.text)

print("List of short movie:", li)
