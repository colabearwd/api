from .get_auth import get_Apitoken
import requests
import time
import json
from config import name, password, api_addr

Apitoken = get_Apitoken(name, password, api_addr)


def get_endpoint():
    """
    获取到json的所有节点的 节点名和id
    {
        "endpoint": "raspberry-01-li",
        "id": 995
    },
    :return:
    """
    print(Apitoken)
    h = {
        "Apitoken": Apitoken,
        "X-Forwarded-For": "202.120.83.82"
    }

    d = {
        "q": "."
    }

    r = requests.get("%s/graph/endpoint" % (api_addr,), params=d, headers=h)

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return r.text


def get_endpoint_counter(eidlist, metriclist):
    """
    获取到所有eidlist = 178
    所有metriclist = .
    的 counter 名称
    {
        "counter": "agent.alive",
        "endpoint_id": 178,
        "step": 60,
        "type": "GAUGE"
    },
    {
        "counter": "cpu.guest",
        "endpoint_id": 178,
        "step": 60,
        "type": "GAUGE"
    }
    :param eidlist:
    :param metriclist:
    :return:
    """
    print(Apitoken)
    d = {
        "eid": eidlist,
        "metricQuery": metriclist
    }
    h = {
        "Apitoken": Apitoken,
        "X-Forwarded-For": "202.120.83.82"
    }
    r = requests.get("%s/graph/endpoint_counter" % (api_addr,), params=d, headers=h)
    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return r.text


def get_endpoint_number():
    """
    获取所有endpoint的个数
    :return:
    """
    res = get_endpoint()
    return len(json.loads(res))


def get_live_endpoint_number():
    """
    获取活着的节点的个数
    TD 需要更改
    :return:
    """
    print(Apitoken)
    eidlist = []
    res = get_endpoint()
    res = json.loads(res)

    for re in res:
        eidlist.append(re['id'])

    eidlist = ",".join('%s' % id for id in eidlist)

    res = get_endpoint_counter(eidlist, "agent.alive")

    return len(json.loads(res))


def get_pinglist_number():
    """
    获取 ping的个数
    :return:
    """
    r = requests.get("http://202.120.83.82:3456/api/ping")

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return len(json.loads(r.text))


def get_curllist_number():
    """
    获取 curl的个数
    :return:
    """
    r = requests.get("http://202.120.83.82:3456/api/curl")

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return len(json.loads(r.text))
