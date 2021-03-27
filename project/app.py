from flask import Flask
from flask import jsonify
from flask import Flask,render_template,redirect, url_for, request
import json
import time
import datetime
from module import Process
import time
import os
localtime = time.asctime( time.localtime(time.time()) )

ps=Process()

DIR="data/"


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def success():
    if request.method == 'POST':


        im = request.files['img']  
        im.save(im.filename)

        fn =request.files['xml']
        fn.save(fn.filename)  

        exacttime=time.time()

        localtime = time.asctime( time.localtime(exacttime))

        # magic
        
        data=ps.get_data_xml(ps.read_xml_obj(fn.filename), im.filename,fn.filename,localtime,exacttime)
        # magic


        datatosend={ "imagename" :im.filename,"timestamp":localtime,"data":data}
        os.remove(im.filename)
        os.remove(fn.filename)
        return render_template("index.html",name=datatosend)  


@app.route('/dataDisplay',methods=['GET'])
def dataDisplay():
    return render_template("dataDisplay.html")

@app.route('/dataDisplay',methods=['POST'])
def dataDisplaysuccess():
    error={"msg":"can't find any data"}
    if request.method == 'POST' and request.form["date-start"] and request.form["date-end"]:
        start_date=request.form["date-start"]
        end_date=request.form["date-end"]

        sd_tm=time.mktime(datetime.datetime.strptime(start_date,"%Y-%m-%d").timetuple())
        ed_tm=time.mktime(datetime.datetime.strptime(end_date,"%Y-%m-%d").timetuple())
        result = ps.getDatafromdb(sd_tm,ed_tm)        
        return render_template("dataDisplay.html",somedata=result)
    else:
        return render_template("dataDisplay.html",error=error)

if __name__ == '__main__':
   app.run(host="localhost",port=5000,debug = True)
