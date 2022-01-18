#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

from aiokubemq.client import KubeMQClient
from aiokubemq.requests import Subscription
from aiokubemq.enums import SubscribeType


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        streamer = await client.send(
            Subscription(typ=SubscribeType.Commands, channel="commands-channel")
        )

        # or

        streamer = await client.send(
            Subscription(typ=SubscribeType.Events, channel="events-channel")
        )

        async for response in streamer:
            print(response)
            # send back RPCResponse for example (when subscribed to commands) → see command_and_query.py


asyncio.run(main())
