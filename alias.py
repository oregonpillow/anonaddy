from uuid import uuid
import requests
import json

bearer = 'Bearer ' + uuid
description = input('Description: ')

http_codes = {
"201":"---Success!---",
"400":"Bad Request -- Your request sucks",
"401":"Unauthenticated -- Your API key is wrong",
"403":"Forbidden -- You do not have permission to access the requested resource",
"404":"Not Found -- The specified resource could not be found",
"405":"Method Not Allowed -- You tried to access an endpoint with an invalid method",
"422":"Validation Error -- The given data was invalid",
"429":"Too Many Requests -- You're sending too many requests or have reached your limit for new aliases",
"500":"Internal Server Error -- We had a problem with our server. Try again later",
"503":"Service Unavailable -- We're temporarially offline for maintanance. Please try again later",
}


url = 'https://app.anonaddy.com/api/v1/aliases'
payload = {
    "domain": "anonaddy.me",
    "description": description,
    "format": "uuid"
}

headers = {
  'Content-Type': 'application/json',
  'X-Requested-With': 'XMLHttpRequest',
  'Authorization': bearer
}

response = requests.request('POST', url, headers=headers, json=payload)
status_code = str(response.status_code)
print(http_codes[status_code])
print(response.json()['data']['email'])

