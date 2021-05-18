#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de Jorge Osses.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)
    

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/jorgecv.png"
    cv = {

        "nombre" : "Jorge",
        "apellido" : "Osses",
        "residencia" : "Argentina",
        "telefono" : "+54 11 2721-8440",
        "experiencia" : [{
            "posicion" : "Tecnico",
            "empresa" : "IMPES",
            "desde" : "Febrero de 2017",
            "hasta" : "actualidad",
            "descripcion" : "tecnico con conocimientos en Redes y Servidores de Videovigilancia, aprendiendo desarrollo web con Python/Django"
        }],
        "educación" : {
            "nivel" : "Secundario completo",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["Python", "API's", "Django", "Flask", "Linux", "desarrollo web(HTML,CSS,JS)","BootStrap"],
        "redes" : {
            "website": "https://jorge.osses.ar",
            "github" : "https://github.com/jorge-osses",
            "twitter" : "https://twitter.com/JorgeOsses19",
            "linkedin" : "https://www.linkedin.com/in/jorge-osses-03078899"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)


@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()

    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")

    print("MENSAJE DE CONTACTO: " + str(mensaje))

    return "Gracias por su mensaje."


if __name__ == '__main__':
    app.run()