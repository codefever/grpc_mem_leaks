#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
import sys
logging.basicConfig(level = logging.INFO)

import grpc

from service_pb2 import CounterRequest, CounterResponse
from service_pb2_grpc import CounterServiceStub


async def create_stub(addr):
    channel = grpc.aio.insecure_channel(addr, [("grpc.lb_policy_name", "round_robin")])
    return CounterServiceStub(channel)


async def serving(stub, idx):
    while True:
        stream = stub.count(CounterRequest(name="{}".format(idx), max_number=1000))

        try:
            async for response in stream:
                logging.info("[%d] receving: %d", idx, response.number)
        except Exception as e:
            logging.error("[%d] got exception", idx, exc_info=e)
            stream.cancel()
            del stream

            await asyncio.sleep(1)


def main():
    loop = asyncio.new_event_loop()
    stub = loop.run_until_complete(create_stub(sys.argv[1]))

    tasks = [loop.create_task(serving(stub, idx)) for idx in range(100)]
    loop.run_until_complete(asyncio.gather(*tasks))


main()
