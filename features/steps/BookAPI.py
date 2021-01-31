import requests
from behave import *
from payload import *
from utilities.configurations import *
from utilities.resources import *

@given("The Book details which needs to be added")
def step_impl(context):
    print('---------------------ADD BOOK API---------------------')
    context.addBookUrl = getConfig()['API']['baseURI']+ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload("mneloasr", "06398")


@when('We execute the AddBook API method')
def step_impl(context):
    context.response = requests.post(context.addBookUrl, json=context.payload, headers=context.headers)


@then('the book is successfully added')
def step_impl(context):
    print(context.response.json()['Msg'])
    context.bookID = context.response.json()['ID']
    assert context.response.json()['Msg'] == "successfully added"

@given('The Book details with {isbn} and {aisle} needs to be added')
def step_impl(context, isbn, aisle):
    context.addBookUrl = getConfig()['API']['baseURI']+ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)
