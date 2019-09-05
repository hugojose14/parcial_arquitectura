from flask import Flask, render_template, request
import datetime
import time
import sqlite3
from copy import deepcopy
app=Flask(__name__)

class pro():
  _clon="false"
  
  def clone(self):
    self._clon ="true"

    return deepcopy(self)
    
#Ruta principal
@app.route('/')

def inicio():

  return render_template('index.html')

def DatosManuales(time,temperatura,hum):

  hora= time.localtime()

  horaT= time.strftime("%H:%M:%S", hora)

  datos=open("09052019.csv","a+")

  datos.write("\r\n"+horaT+", "+time+", "+ temperatura+ ", "+ hum )

  datos.close()

@app.route('/log', methods=['GET'])
def getValues():

  time = request.args.get('time')

  temperatura = request.args.get('temperatura')

  hum = request.args.get('humedad')

  DatosManuales(time,temperatura,hum)

  return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template("error.html",error="Página no encontrada..."), 404


app.run(debug=True,port=3000)