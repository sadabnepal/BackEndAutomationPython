from utilities.configurations import *


def addBookPayload(isbn, aisle):
    book = {
                "name":"Learn Appium Automation with Java",
                "isbn": isbn,
                "aisle": aisle,
                "author":"MD SADAB SAQIB"
            }
    return book


def deleteBookPayload(bookID):
    return {
                "ID": bookID
            }


def buildPayloadFromDB(query):
    addbody = {}
    tp = getQuery(query)
    addbody['name'] = tp[0]
    addbody['isbn'] = tp[1]
    addbody['aisle'] = tp[2]
    addbody['author'] = tp[3]
    return addbody
