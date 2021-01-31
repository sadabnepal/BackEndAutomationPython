import requests
from utilities.configurations import *
from utilities.resources import *

@given('I pass username and password github auth credentials')
def step_impl(context):
    for row in context.table:
        username = row['username']
        password = row['password']
    context.ses = requests.session()
    context.ses.auth = auth = (getGitUserName(username), getGitPassword(password))
    print('---------------------Git APIs----------------------------')
    context.apiUrl = getConfig()['GITHUB']['baseURI']+ApiResources.githubUserService    


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.ses.get(context.apiUrl)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print("Response Code: ", context.response.status_code)
    assert context.response.status_code == statusCode
    