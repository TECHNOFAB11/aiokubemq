#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

from aiokubemq.client import KubeMQClient
from aiokubemq.enums import StreamRequestType
from aiokubemq.requests import (
    QueueMessageStream,
    StreamQueueMessagesRequest,
    EventStream,
    Event,
)


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        # stream queue messages

        async def streamer_1():
            yield StreamQueueMessagesRequest(
                channel="queue-channel", typ=StreamRequestType.ReceiveMessage
            )

            while True:
                await asyncio.sleep(1)
                # use an asyncio.Queue here for example to yield more messages to the stream

        stream = await client.send(QueueMessageStream(stream=streamer_1()))

        async for resp in stream:
            print(resp)
            # put your response into the above mentioned asyncio.Queue to send it back
            # eg: StreamQueueMessagesRequest with typ=StreamRequestType.AckMessage to acknowledge
            # or: StreamQueueMessagesRequest with typ=StreamRequestType.RejectMessage to reject, etc.

        # stream events

        async def streamer_2():
            while True:
                yield Event(channel="event-channel", body=b"Hello World")
                await asyncio.sleep(5)

        stream = await client.send(EventStream(stream=streamer_2()))

        async for resp in stream:
            print(resp)


asyncio.run(main())
