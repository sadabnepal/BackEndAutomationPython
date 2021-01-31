import requests
from payload import *
from utilities.configurations import *
from utilities.resources import *

print('---------------------ADD BOOK API---------------------')
addBookUrl = getConfig()['API']['baseURI']+ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = "SELECT * FROM Books"
addBook_resp = requests.post(addBookUrl, json=buildPayloadFromDB(query), headers=headers)

print(addBook_resp.json())
assert addBook_resp.status_code == 200
bookID = addBook_resp.json()['ID']
print(bookID)

print('---------------------Delete BOOK API---------------------')
deleteBookUrl = getConfig()['API']['baseURI']+ApiResources.deleteBook
deleteBook_resp = requests.post(deleteBookUrl, json=deleteBookPayload(bookID), headers=headers)

print(deleteBook_resp.json())
assert deleteBook_resp.status_code == 200
assert deleteBook_resp.json()['msg'] == 'book is successfully deleted'
