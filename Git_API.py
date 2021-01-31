import requests
from utilities.configurations import *
from utilities.resources import *

# Authentication
ses = requests.session()
ses.auth = auth = (getConfig()['GITHUB']['username'], getConfig()['GITHUB']['password'])

print('---------------------Git APIs----------------------------')
apiUrl = getConfig()['GITHUB']['baseURI']+ApiResources.githubUserService
response = ses.get(apiUrl)
assert response.status_code == 200
gitresponse = response.json()
print(response.status_code)