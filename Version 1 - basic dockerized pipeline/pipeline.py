#!/usr/bin/env python

""" pipeline.py: Example pipeline server (P1).

Note: Requires running NATS server configured on localhost:4222
      i.e. docker run -p 4222:4222 -p 8222:8222 -p 6222:6222 --name gnatsd -ti nats:latest
"""
import asyncio
from nats.aio.client import Client as NATS

test_pauses = [10, 40, 10, 10]  # in milliseconds

def pipeline_p1(loop):
    #####################
    # Connection to NATS
    #####################
    nc = NATS()
    yield from nc.connect("localhost:4222", loop=loop)

    #####################
    # Message Handlers
    #####################
    async def mh_s1(msg):
        await nc.publish("p1.s1", msg.data)

    async def mh_s2(msg):
        await nc.publish("p1.s2", msg.data)

    async def mh_s3(msg):
        await nc.publish("p1.s3", msg.data)

    ######################
    # Pipeline Creation
    ######################
    yield from nc.subscribe("p1.s0", cb=mh_s1)
    yield from nc.subscribe("p1.s1", cb=mh_s2)
    yield from nc.subscribe("p1.s2", cb=mh_s3)


if __name__ == '__main__':
    import logging

    logging.basicConfig(format='%(asctime)s, %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    print("Constructing test pipeline - P1")

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(pipeline_p1(event_loop))

    try:
        print('Run forever')
        event_loop.run_forever()
    finally:
        print('Closing')
