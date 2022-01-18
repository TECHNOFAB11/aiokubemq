#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio

import aiokubemq.proto.kubemq_pb2 as proto
from aiokubemq.client import KubeMQClient
from aiokubemq.enums import RequestType
from aiokubemq.requests import RPCRequest, RPCResponse


async def main():
    async with KubeMQClient("test-client", "localhost:50000") as client:
        resp = await client.send(
            RPCRequest(
                channel="rpc-channel", body=b"process dis", typ=RequestType.Query
            )
        )
        print(resp.Body)

        resp = await client.send(
            RPCRequest(
                channel="rpc-channel",
                body=b"send email or something",
                typ=RequestType.Command,
            )
        )
        print(resp.Executed)

        # answer to a previously received RPCRequest:

        request = proto.Response()  # received via subscription for example

        await client.send(
            RPCResponse(
                channel=request.ReplyChannel,
                request_id=request.RequestID,
                body=b"processed stuff",
            )
        )
        # nothing is returned


asyncio.run(main())
