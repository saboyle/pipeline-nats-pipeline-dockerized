import asyncio
import json
import random
from nats.aio.client import Client as NATS

async def pub_random(loop):
    nc = NATS()
    await nc.connect("localhost:4222", loop=loop)

    if nc.last_error:
        print("ERROR received from NATS: ", nc.last_error)
    else:
        print('Submitting random requests')
        i = 0
        while True:
            jdata = {"i": i}
            await nc.publish('p1.s0', json.dumps(jdata).encode('utf-8'))
            await asyncio.sleep(random.random())
            i += 1


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(pub_random(event_loop))