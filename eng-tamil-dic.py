from flask import Flask,json,Response
import sqlite3
app = Flask(__name__)
@app.route('/dic/<eng>')
def dic(eng):
    con=sqlite3.connect('nofts.sqlite')
    data=con.execute("select ENGW,TAMW from engtam where ENGW='{}'".format(eng))
    list=[]
    for t in data:
        list.append(t)
    data = { "result" : list}
    json_string = json.dumps(data,ensure_ascii = False)
    response = Response(json_string,content_type="application/json; charset=utf-8" )
    return response
app.run()
