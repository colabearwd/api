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
import commands
import re
import json
import requests

nodenamecmd = "uname -n"
status, output = commands.getstatusoutput(nodenamecmd)
NODE = output+"_curl"


def do_script(tempmessage):

    print(tempmessage.split(';')[0].split(':')[1])
    ipversion = tempmessage.split(';')[0].split(':')[1]
    print(tempmessage.split(';')[1].split(':')[1])
    serialnum = tempmessage.split(';')[1].split(':')[1]
    print(tempmessage.split(';')[2].split(':')[1])
    targeturl = tempmessage.split(';')[2].split(':')[1]
    print(tempmessage.split(';')[3].split(':')[1])
    timeout = tempmessage.split(';')[3].split(':')[1]

    cmd = "curl -"+ ipversion +" -o /dev/null --connect-timeout "+ timeout +" -s -w %{http_code}:%{http_connect}:%{time_namelookup}:%{time_redirect}:%{time_pretransfer}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} " + targeturl

    print cmd
    status, output = commands.getstatusoutput(cmd)

    res = output.split(":")

    push_url = "http://202.120.83.82:3456/temporarytask/post_temp_curlres/"

    payload = { 'curl_httpcode': res[0], 
                'curl_httpconnect': res[1],
                'curl_nameloopup': res[2], 
                'curl_redirect': res[3],
                'curl_pretransfer': res[4], 
                'curl_connect': res[5],
                'curl_starttransfer': res[6], 
                'curl_total': res[7],
                'curl_speeddownload': res[8],
                'curl_serialnum': serialnum
    }

    print(json.dumps(payload))

    #r = requests.post(push_url, json=json.dumps(payload))
    #r = requests.post(push_url, json=json.loads(payload))
    r = requests.post(push_url, json=payload)

    return 0


def run():
    conn = grpc.insecure_channel("202.120.83.82:8081")
    client = push_pb2_grpc.MessageSyncStub(channel=conn)

    try:
        response = client.PushMessageStream(ConnRequest(channel=NODE))

        for r in response:
            print(r.message)
            res = do_script(r.message)

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
