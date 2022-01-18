#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

from aiokubemq.client import KubeMQClient
from aiokubemq.requests import (
    QueueMessageBatch,
    QueueMessage,
    AckAllQueueMessages,
    ReceiveQueueMessages,
)


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        # send single message
        resp = await client.send(
            QueueMessage(channel="queue-channel", body=b"Hello World")
        )
        print(resp)

        # send batch
        resp = await client.send(
            QueueMessageBatch(
                messages=[
                    QueueMessage(channel="queue-channel", body=b"some data"),
                    QueueMessage(channel="queue-channel", body=b"other data"),
                ]
            )
        )
        print(resp)

        # acknowledge all messages in queue
        resp = await client.send(
            AckAllQueueMessages(channel="queue-channel", wait_time=10)
        )
        print(resp)

        # receive 2 messages with timeout of 10s
        resp = await client.send(
            ReceiveQueueMessages(channel="queue-channel", wait_time=10, max_messages=2)
        )
        print(resp)


asyncio.run(main())
