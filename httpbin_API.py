import requests
from utilities.configurations import *
from utilities.resources import *

print("--------Sending Cookies from cookies param and in session--------")
ss = requests.session()
ss.cookies.update({"name": "john deo"})

httpbinBaseURL = getConfig()['HTTPBIN']['baseURI']
httpbinService = ApiResources.httpCookieService
cookies = {"visitor": "engineer"}
httpbin_res = ss.get(httpbinBaseURL+httpbinService, cookies=cookies)
print(httpbin_res.text)

print("----------Validating Redirection Code----------")
# Status code of 300 series is for redirecting urls
# allow_redirects=False will stop the URL to redirect and hence status code will be of 300 series
response_red = requests.get("http://rahulshettyacademy.com", allow_redirects=False)
# print(response_red.history)
print(response_red.status_code)

print("----------Handling Time delay----------")
httpbin_res = requests.get("http://rahulshettyacademy.com", cookies=cookies, timeout=15)
print(httpbin_res.status_code)
