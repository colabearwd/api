#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc
from grpc._channel import _Rendezvous

#from push_pb2 import ConnRequest
#from push_pb2_grpc import MessageSyncStub

import push_pb2
import push_pb2_grpc

from push_pb2 import *
from push_pb2_grpc import *

# ip , get the ip
NODE = "rasp_ping"


def do_script(tempmessage):
    # get the args from the Server 
    
    print(tempmessage.split(';')[0].split(':')[1])
    switch=tempmessage.split(';')[0].split(':')[1]
    print(tempmessage.split(';')[1].split(':')[1])
    serialnum=tempmessage.split(';')[1].split(':')[1]
    print(tempmessage.split(';')[2].split(':')[1])
    targeturl=tempmessage.split(';')[2].split(':')[1]
    print(tempmessage.split(';')[3].split(':')[1])
    packagesize=tempmessage.split(';')[3].split(':')[1]
    print(tempmessage.split(';')[4].split(':')[1])
    timeout=tempmessage.split(';')[4].split(':')[1]
    print(tempmessage.split(';')[5].split(':')[1])
    ipversion=tempmessage.split(';')[5].split(':')[1]

    # put the args into script 

    # put the results to API

    pass 

def run():
    conn = grpc.insecure_channel("localhost:8081")
    client = push_pb2_grpc.MessageSyncStub(channel=conn)

    try:
        response = client.PushMessageStream(ConnRequest(channel=NODE))

        for r in response:
            print(r.message)
	    # tempmessage=r.message
	    
	    do_script(r.message)
    
    except _Rendezvous as e:
        # here we can setup some retry mechanism.
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("StatusCode.UNAVAILABLE")

        if e.code() == grpc.StatusCode.INTERNAL:
            print("StatusCode.INTERNAL")

    except Exception as e:
        print("exception")


if __name__ == '__main__':
    run()
