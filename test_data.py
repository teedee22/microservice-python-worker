import requests
import random
import json

url = "http://127.0.0.1:5000/new"

payload = "{\n    \"message\": \"hello toby\",\n    \"count\": 12\n}"
headers = {
  'Content-Type': 'application/json'
}

for i in range(10):
    number = random.randint(1,5)
    body = {"message": "hello Toby", "count": number}
    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print(str(i) + " response: ", end="")
    print(response.text.encode('utf8'))
