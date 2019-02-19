#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time

import grpc

from push_pb2 import SubmitRequest
from push_pb2_grpc import MessageSyncStub


# raspberry node = channel
NODE = "aaaa"

SWITCH = "PING"

SERIALNUM = "15426365852"

TARGETURL = "www.baidu.com"
PACKAGESIZE = 64
TIMEOUT = 5
IPVERSION = 4

MESSAGE = "switch:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};ipversion:{5}".format(SWITCH,SERIALNUM,TARGETURL,PACKAGESIZE,TIMEOUT,IPVERSION)


def run():
    conn = grpc.insecure_channel("localhost:8081")
    client = MessageSyncStub(channel=conn)
#    for i in range(1, 10000000):
    client.SubmitMessage(SubmitRequest(channel=NODE, message=MESSAGE ))
#        sleep(0.1)


if __name__ == '__main__':
    run()
