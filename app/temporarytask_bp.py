#-*-coding:utf-8-*-
from flask import Blueprint,request,render_template,redirect
from app.models import Map
from app.of import get_history,get_dashboardnum,get_curlorping_res
import json,time


temporarytask = Blueprint('temporarytask',__name__)


@temporarytask.route('/temporarytask_ping/',methods=['GET','POST'])
def temporarytask_ping():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('temporarytask_ping.html',endpointlist = maplist)
    else:
        print(request.form.get('endpoint_select'))
        print(request.getParameter('endpoint_select'))
        print(request.form.get('counter_select'))
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