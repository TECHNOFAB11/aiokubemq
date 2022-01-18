#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

from aiokubemq.client import KubeMQClient


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        response = await client.ping()
        print(f"Connected to host '{response.Host}'")


asyncio.run(main())
