from flask import Flask, request, jsonify
from flask_cors import CORS
from xml.etree import ElementTree as ET
from models.animals import Perro, Gato, Conejo
from data.data import Data

app = Flask(__name__)
CORS(app)
data = Data()

@app.route('/borrar', methods=['POST'])
def borrar():
  data.animales.clear()
  return jsonify({ 'status': 'Datos borrados' })


@app.route('/cargarXML', methods=['POST'])
def cargar():
  mi_archivo = request.data
  decodificar_xml = mi_archivo.decode('utf-8')
  xml = ET.XML(decodificar_xml)

  for perro in xml.findall('perro'):
    edad = perro.find('edad').text
    raza = perro.find('raza').text

    temp_perro = Perro(edad, raza)
    data.animales.append(temp_perro)
  for gato in xml.findall('gato'):
    edad = gato.find('edad').text
    raza = gato.find('raza').text

    temp_gato = Gato(edad, raza)
    data.animales.append(temp_gato)
  for conejo in xml.findall('conejo'):
    edad = conejo.find('edad').text
    raza = conejo.find('raza').text

    temp_conejo = Conejo(edad, raza)
    data.animales.append(temp_conejo)

  return jsonify({ 'status_code': '200' })

@app.route('/procesarDatos', methods=['GET'])
def procesar():
  root = ET.Element('respuesta')
  contador = 0
  for perro in data.animales:
    if perro.tipo == 'Perro':
      contador += 1

  resultados = ET.SubElement(root, 'resultados')
  perros = ET.SubElement(resultados, 'perros')
  ET.SubElement(perros, 'cantidadTotal').text = str(contador)

  contador = 0
  for gato in data.animales:
    if gato.tipo == 'Gato':
      contador += 1

  gatos = ET.SubElement(resultados, 'gatos')
  ET.SubElement(gatos, 'cantidadTotal').text = str(contador)

  contador = 0
  for conejo in data.animales:
    if conejo.tipo == 'Conejo':
      contador += 1

  conejos = ET.SubElement(resultados, 'conejos')
  ET.SubElement(conejos, 'cantidadTotal').text = str(contador)

  return ET.tostring(root, encoding='utf8', method='xml')

if __name__ == '__main__':
  app.run(host='localhost', port=5000, debug=True)