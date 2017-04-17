from bottle import Bottle,route,run,request,template,static_file
import json
import os
import requests
@route('/',method="get")
def eventfull():
    return template ('template.tpl')
@route('/eventfull',method="post")
def eventfull():
    ciudad = request.forms.get('ciudad')
    tipo = request.forms.get('tipo')
    a=open("key_eventfull.txt","r")
    key=a.readline()
    payload={"app_key":key, "location": ciudad, "keywords":tipo}
    r=requests.get("http://api.eventful.com/json/events/search?keywords="+tipo+"&location="+ciudad+"&app_key="+key)
    if r.status_code == 200:
        js=json.loads(r.text)
        titulo=[]
        empezar=[]
        lugar=[]
        for i in js["events"]["event"]:
            titulo.append(i["title"])
            empezar.append(i["start_time"])
            lugar.append(i["venue_name"])
    return template('template2.tpl', titulo=titulo, empezar=empezar, lugar=lugar, ciudad=ciudad, tipo=tipo)

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


run(host='localhost', port=8080, debug=True, reloader=True)