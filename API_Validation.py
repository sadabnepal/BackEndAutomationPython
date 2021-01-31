import requests
import json

response = requests.get(
    "http://216.10.245.166/Library/GetBook.php",
    params={'AuthorName': 'Rahul Shetty2'})

# print(response.text)
# print(type(response.text))
#
# dic_response = json.loads(response.text)
# print(dic_response[0]['isbn'])
# print(type(dic_response))

json_response = response.json()
print(json_response)
print(type(json_response))
print(response.status_code)
assert response.status_code == 200

# print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

for actualBook in json_response:
    if actualBook['aisle'] == '175':
        print(actualBook)
        break;

expectedBook = {'book_name': 'Devops', 'isbn': 'bnid34', 'aisle': '175'}

assert actualBook == expectedBook
