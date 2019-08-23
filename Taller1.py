from flask import Flask, jsonify, request
#pip install flask_cors

from flask_cors import CORS

from datetime import datetime

app = Flask(__name__)
CORS(app)

tipo_medicion = { 'sensor':'HC-SR04', 'variable' : 'Distancia' , 'unidades ' : 'cm'} #depende de codigo uy sensor

mediciones = [
    {'fecha ' : ' 2019-08-03 13:12:45', **tipo_medicion, 'valor' : 100},
    {'fecha ' : ' 2019-08-04 4:35:12', **tipo_medicion, 'valor' : 130},
    {'fecha ' : ' 2019-08-07 3:15:42', **tipo_medicion, 'valor' : 450},
    {'fecha ' : ' 2019-08-14 15:47:42', **tipo_medicion, 'valor' : 320},
    {'fecha ' : ' 2019-08-16 21:41:42', **tipo_medicion, 'valor' : 270},
    {'fecha ' : ' 2019-08-19 16:35:55', **tipo_medicion, 'valor' : 70},
    {'fecha ' : ' 2019-08-23 2:55:12', **tipo_medicion, 'valor' : 220}
]

#Traer todas la mediciones
@app.route("/mediciones", methods=['GET'])
def getAll():
    return jsonify(mediciones)

@app.route("/")
def get():
    return "SENSOR ULTRASONICO"

#realizar la media de todas las mediciones
@app.route('/mediciones/media',methods=['GET'])
def getMedia():
    #b = mediciones[0]["valor"]
    #y = len(mediciones)
    c=0

    for dato in mediciones:
        c += dato["valor"]

    return "La media de las mediciones del sensor ultrasonico es : "+str(c/len(mediciones))

#ingresar una nueva medicion
@app.route('/mediciones', methods=['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['fecha'] = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    mediciones.append({**body, **tipo_medicion})
    return jsonify(mediciones)

#puerto y autorun
app.run(port=5000, debug=True)
