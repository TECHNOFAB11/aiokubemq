#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

from aiokubemq.client import KubeMQClient
from aiokubemq.requests import Event


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        result = await client.send(
            Event(channel="event-channel", body=b"Hello World", event_id="some_id")
        )
        print("Sent →", result.Sent)


asyncio.run(main())
