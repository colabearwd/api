#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import sys
import grpc

from app.grpc_push.push_pb2 import SubmitRequest
from app.grpc_push.push_pb2_grpc import MessageSyncStub


# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])
# print(sys.argv[4])
# print(sys.argv[5])
# print(sys.argv[6])
# print(sys.argv[7])
#
# # raspberry node = channel
# NODE = sys.argv[1]
#
# SWITCH = sys.argv[2]
#
# SERIALNUM = sys.argv[3]
#
# TARGETURL = sys.argv[4]
# PACKAGESIZE = sys.argv[5]
# TIMEOUT = sys.argv[6]
# IPVERSION = sys.argv[7]
#
# #NODE = "rasp_ping"
#
# #SWITCH = "PING"
#
# #SERIALNUM = "15426365852"
#
# #TARGETURL = "www.baidu.com"
# #PACKAGESIZE = 64
# #TIMEOUT = 5
# #IPVERSION = 4
#
#
# MESSAGE = "switch:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};ipversion:{5}".format(SWITCH,SERIALNUM,TARGETURL,PACKAGESIZE,TIMEOUT,IPVERSION)


def run(a, b, c, d, e, f,g):
    NODE = a

    IPVERSION = b

    SERIALNUM = c

    TARGETURL = d
    PACKAGESIZE = e
    TIMEOUT = f
    COUNT = g

    MESSAGE = "ipversion:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};count:{5}".format(IPVERSION,
                                                                                                        SERIALNUM,
                                                                                                        TARGETURL,
                                                                                                        PACKAGESIZE,
                                                                                                        TIMEOUT,
                                                                                                        COUNT
                                                                                                        )
    conn = grpc.insecure_channel("localhost:8081")
    client = MessageSyncStub(channel=conn)
#    for i in range(1, 10000000):
    client.SubmitMessage(SubmitRequest(channel=NODE, message=MESSAGE ))
#        sleep(0.1)



