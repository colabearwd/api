#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time

import grpc

from app.grpc_push.push_pb2 import SubmitRequest
from app.grpc_push.push_pb2_grpc import MessageSyncStub


# raspberry node = channel



def run(a, b, c, d, e, f, g,):
    NODE = a

    SWITCH = b

    SERIALNUM = c

    TARGETURL = d
    PACKAGESIZE = e
    TIMEOUT = f
    IPVERSION = g

    MESSAGE = "switch:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};ipversion:{5}".format(SWITCH,
                                                                                                        SERIALNUM,
                                                                                                        TARGETURL,
                                                                                                        PACKAGESIZE,
                                                                                                        TIMEOUT,
                                                                                                        IPVERSION)
    conn = grpc.insecure_channel("localhost:8081")
    client = MessageSyncStub(channel=conn)
#    for i in range(1, 10000000):
    client.SubmitMessage(SubmitRequest(channel=NODE, message=MESSAGE ))
#        sleep(0.1)



