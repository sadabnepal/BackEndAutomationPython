import requests
from payload import *
from utilities.configurations import *
from utilities.resources import *

def after_scenario(context, scenario):
    print('---------------------Delete BOOK API---------------------')
    if "library" in scenario.tags:      
        deleteBookUrl = getConfig()['API']['baseURI']+ApiResources.deleteBook
        response = requests.post(deleteBookUrl, json=deleteBookPayload(context.bookID), headers=context.headers)
        print(response.json()['msg'])
        assert response.json()['msg'] == 'book is successfully deleted'