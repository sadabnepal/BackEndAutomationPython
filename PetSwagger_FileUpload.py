import requests
from utilities.configurations import *


baseURI = getConfig()['PETSWAGGER']['baseURI']
service = '/pet/9843217/uploadImage'
files = {'file': open('files/write.txt', 'rb')}
resp = requests.post(baseURI+service, files=files)
print(resp.status_code)
print(resp.text)
