#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time

import grpc

from app.grpc_push.push_pb2 import SubmitRequest
from app.grpc_push.push_pb2_grpc import MessageSyncStub


# raspberry node = channel


def run(a, b, c, d, e):
    NODE = a

    IPVERSION = b

    SERIALNUM = c

    TARGETURL = d

    TIMEOUT = e

    MESSAGE = "ipversion:{0};serialnum:{1};targeturl:{2};timeout:{3}".format(IPVERSION,
                                                                             SERIALNUM,
                                                                             TARGETURL,
                                                                             TIMEOUT
                                                                             )
    conn = grpc.insecure_channel("202.120.83.82:8081")
    client = MessageSyncStub(channel=conn)
#    for i in range(1, 10000000):
    client.SubmitMessage(SubmitRequest(channel=NODE, message=MESSAGE))
#        sleep(0.1)
