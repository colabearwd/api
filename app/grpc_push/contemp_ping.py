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

# ip , get the ip
# NODE = "995"
nodenamecmd="uname -n"
status, output = commands.getstatusoutput(nodenamecmd)
NODE=output+"_ping"

def do_script(tempmessage):
    # get the args from the Server 
    
    print(tempmessage.split(';')[0].split(':')[1])
    ipversion=tempmessage.split(';')[0].split(':')[1]
    print(tempmessage.split(';')[1].split(':')[1])
    serialnum=tempmessage.split(';')[1].split(':')[1]
    print(tempmessage.split(';')[2].split(':')[1])
    targeturl=tempmessage.split(';')[2].split(':')[1]
    print(tempmessage.split(';')[3].split(':')[1])
    packagesize=tempmessage.split(';')[3].split(':')[1]
    print(tempmessage.split(';')[4].split(':')[1])
    timeout=tempmessage.split(';')[4].split(':')[1]
    print(tempmessage.split(';')[5].split(':')[1])
    count=tempmessage.split(';')[5].split(':')[1]

    # put the args into script 

    # put the results to API
    if ipversion == "4" :
        args_ipversion ="ping"
    else :
        args_ipversion = "ping6"

    cmd = "{0} -s {1} -c {2} -W {3} -q {4} ".format(args_ipversion, packagesize ,count , timeout , targeturl)
    print(cmd)
    status, output = commands.getstatusoutput(cmd)
    print(status)
    print(output)

    if (status == 0):
        temp1 = re.search(r"received, \d+\.?\d{0,3}% packet loss", output)

        temp2 = re.search(r"\d+\.?\d{0,3}\/\d+\.?\d{0,3}\/\d+\.?\d{0,3}\/", output)

        t1 = re.findall(r"\d+\.?\d{0,3}", temp1.group())

        t2 = re.findall(r"\d+\.?\d{0,3}", temp2.group())

        res = []
        res.append(t1[0])
        res.append(t2[2])
        res.append(t2[1])
        res.append(serialnum)
	
	print(res[0])
	print(res[1])
	print(res[2])
	print(res[3])


        push_url = "http://202.120.83.82:3456/temporarytask/post_temp_pingres/"
	
	payload = {'ping_serialnum':res[3],'ping_lossrate':res[0],'ping_maxtime':res[1],'ping_averagetime':res[2]}
	
	print(json.dumps(payload))

	#r = requests.post(push_url, json=json.dumps(payload))
	#r = requests.post(push_url, json=json.loads(payload))
	r = requests.post(push_url, json=payload)
	
	
        return res


def run():
    conn = grpc.insecure_channel("202.120.83.82:8081")
    client = push_pb2_grpc.MessageSyncStub(channel=conn)

    try:
        response = client.PushMessageStream(ConnRequest(channel=NODE))

        for r in response:
            print(r.message)
        # tempmessage=r.message
	    
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

