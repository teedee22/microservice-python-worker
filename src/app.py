import asyncio
import json
import requests

from nats.aio.client import Client as NATS

async def get_message(msg):
    payload = json.loads(msg.data)
    print(u'\u2753', end="")
    print(payload["count"])
    await asyncio.sleep(payload["count"])
    print(payload)

async def get_message_api(msg):
    url = "http://sleepy-api:5001/new"
    # payload = {}
    # headers = {}
    future = loop.run_in_executor(None, requests.get, url)
    #response = requests.request("GET", url, headers=headers, data = payload)
    response = await future
    print(response.text.encode('utf8'))
    payload = json.loads(msg.data)
    print(payload["id"])


async def run(event_loop):
    nc = NATS()
    await nc.connect(nats_host, loop=event_loop)
    print("hello")
    await nc.subscribe("foobar", "foobar", get_message)
    await nc.subscribe("foobar2", "foobar2", get_message_api)

if __name__=="__main__":
    try:
        nats_host="nats://nats:4222"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(loop))
        loop.run_forever()

    except asyncio.CancelledError:
        pass
    except KeyboardInterrupt:
        print("\nExiting gracefully")