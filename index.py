from flask import Flask,render_template,jsonify,request
import csv
from datetime import datetime
from io import StringIO
from werkzeug.wrappers import Response

app = Flask(__name__)

informacion = [
    ('tiempo', (30,29,30)),
    ('humedad', (2,4,9)),
    ('temperatura', (30,8,9))] 

@app.route('/')
def  index():
    return render_template('index.html')

@app.route('/',methods=['GET'])
def crearCSV():
    def generate():
        data = StringIO()
        w = csv.writer(data)
        w.writerow(('action', 'timestamp'))
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        for item in informacion:
            w.writerow((
                item[0],
            
            ))
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    response = Response(generate(), mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="informacion.csv")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)