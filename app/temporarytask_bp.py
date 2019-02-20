#-*-coding:utf-8-*-
from flask import Blueprint,request,render_template,redirect
from app.models import Map,Temporary_Ping_Res,Temporary_Curl_Res
from app.of import get_history,get_dashboardnum,get_curlorping_res
import json,time

from app.grpc_push.producer_ping  import run as pingrun
from app.grpc_push.producer_curl  import run as curlrun

temporarytask = Blueprint('temporarytask',__name__)


@temporarytask.route('/temporarytask_ping/',methods=['GET','POST'])
def temporarytask_ping():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('temporarytask_ping.html',endpointlist = maplist)
    else:
        print(request.form.get('serialnum'))
        SERIALNUM=request.form.get('serialnum')
        print(request.form.get('endpoint_select'))
        NODE=request.form.get('endpoint_select')
        print(request.form.get('targeturl'))
        TARGETURL=request.form.get('targeturl')
        print(request.form.get('packagesize'))
        PACKAGESIZE=request.form.get('packagesize')
        print(request.form.get('timeout'))
        TIMEOUT=request.form.get('timeout')
        print(request.form.get('ipversion'))
        SWITCH=request.form.get('ipversion')
        IPVERSION=request.form.get('ipversion')

        MESSAGE="switch:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};ipversion:{5}".format(SWITCH,SERIALNUM,TARGETURL,PACKAGESIZE,TIMEOUT,IPVERSION)
        print(MESSAGE)

        pingrun(NODE,SWITCH,SERIALNUM,TARGETURL,PACKAGESIZE,TIMEOUT,IPVERSION)

        return render_template('temporarytask_ping.html')


@temporarytask.route('/temporarytask_curl/',methods=['GET','POST'])
def temporarytask_curl():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('temporarytask_curl.html',endpointlist = maplist)
    else:
        print(request.form.get('endpoint_select'))
        print(request.getParameter('endpoint_select'))
        print(request.form.get('counter_select'))

        return render_template('temporarytask_curl.html')

@temporarytask.route('/post_temp_pingres/',methods=['GET','POST'])
def post_temp_pingres():
    if request.method == 'GET':
        pass
    else:
        print(request)
        print(request.get_json())
        res = request.get_json()
        Temporary_Ping_Res.ping_serialnum=res['ping_serialnum']
        Temporary_Ping_Res.ping_averagetime=res['ping_averagetime']
        Temporary_Ping_Res.ping_lossrate=res['ping_lossrate']
        Temporary_Ping_Res.ping_maxtime=res['ping_maxtime']
        return 'ok'


@temporarytask.route('/post_temp_curlres/', methods=['GET', 'POST'])
def post_temp_curlres():
    if request.method == 'GET':
        pass
    else:
        print(request)
        print(request.get_json())
        res = request.get_json()
        Temporary_Curl_Res.curl_connect=res['curl_connect']
        Temporary_Curl_Res.curl_httpcode=res['curl_httpcode']
        Temporary_Curl_Res.curl_httpconnect=res['curl_httpconnect']
        Temporary_Curl_Res.curl_nameloopup=res['curl_nameloopup']
        Temporary_Curl_Res.curl_pretransfer=res['curl_pretransfer']
        Temporary_Curl_Res.curl_redirect=res['curl_redirect']
        Temporary_Curl_Res.curl_serialnum=res['curl_serialnum']
        Temporary_Curl_Res.curl_speeddownload=res['curl_speeddownload']
        Temporary_Curl_Res.curl_total=res['curl_total']
        Temporary_Curl_Res.curl_starttransfer=res['curl_starttransfer']
        return 'ok'

