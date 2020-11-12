import requests
import random
import json
import time

def generate_calls(number):
  for i in range(number):
    endpoint = random.randint(1,2)
    if endpoint == 1:
      url = "http://34.76.117.74:4000/new2"
    else:
      url = "http://34.76.117.74:4000/new"
    number = random.randint(1,100) / 100
    #number = 0.2
    body = {"message": "hello Toby", "count": number, "id": i}
    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print(str(i) + " response: ", end="")
    print(response.text.encode('utf8'))

generate_calls(15)
time.sleep(1)
generate_calls(15)
time.sleep(0.2)
generate_calls(3)
