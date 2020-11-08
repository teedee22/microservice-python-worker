import asyncio
import json

from nats.aio.client import Client as NATS

async def get_message(msg):
    payload = json.loads(msg.data)
    print(u'\u2753', end="")
    print(payload)


async def run(event_loop):
    nc = NATS()
    await nc.connect(nats_host, loop=event_loop)
    print("hello")
    await nc.subscribe("foobar", "foobar", get_message)

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