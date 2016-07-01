import urls
from bs4 import BeautifulSoup
import requests
import json
import re

def switch_dias(dia):
    """
    Funcion que hace de switch
    """
    switcher = {
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT",
        7: "SUN"
    }
    return switcher.get(dia, "MON")

def __obtenerNombreAsig(html):
    contenido = html.find("div", {"id": "contenido_"})
    titulo = contenido.find("h1").getText()
    return titulo.split("-")[1]


def __generarHorarios(regex, tipo, html):
    tabla = html.find(text=re.compile(regex)).findNext('table')
    semanas = tabla.select("tbody tr")
    lista_eventos = []
    rangoSemanas = "0-15" #Valor por defecto
    for rango_semanas in semanas:
        columnas = rango_semanas.find_all('td')
        for i, columna in enumerate(columnas):
            if i == 0:
                rangoSemanas = columna.getText()
            elif columna.getText() != "--":
                evento = {}
                evento["tipoEvento"] = tipo
                evento["diaSemana"] = switch_dias(i)
                evento["rangoSemanas"] = rangoSemanas
                rango_horas = columna.getText().split("-")
                evento["horaInicio"] = rango_horas[0]
                evento["horaFin"] = rango_horas[1]
                lista_eventos.append(evento)
    return lista_eventos

def __obtenerHorarioTeorico(grupo, html):
    """
        Funcion para obtener el horario de las clases teoricas de una asignatura
    """
    regex = "Grupos:." + grupo + ".T"
    return __generarHorarios(regex, "M", html)

def __obtenerHorarioPractico(grupo, html):
    """
        Funcion para obtener el horario de las clases practicas de una asignatura
    """
    regex = "Grupos:." + grupo + ".P"
    return __generarHorarios(regex, "GA", html)


def obtenerHorarioAsignatura(codigoAsig, grupo, campus="GI", codigoGrado="GINFOR20", idioma="es"):
    """
        Si se encuentra la asignatura devuelve un JSON con los datos de la asignatura en formato normalizado
        Si no encuentra los horarios para la asignatura devuelve un mensaje de error.
    """
    try:
        urlAsignatura = urls.__getUrlAsig(campus, codigoGrado, codigoAsig, idioma)
        req = requests.get(urlAsignatura)
        statusCode = req.status_code
        if statusCode == 200:
            html = BeautifulSoup(req.text, "html.parser")
            asignatura = {}
            asignatura["nombreAsignatura"] = __obtenerNombreAsig(html)
            asignatura["codigo"] = codigoAsig
            asignatura["enlaceWebUPV"] = urlAsignatura
            horarioGrupoAsignatura = {}
            horarioGrupoAsignatura["eventos"] = __obtenerHorarioPractico(grupo, html) + __obtenerHorarioTeorico(grupo, html)
            horarioGrupoAsignatura["IDGrupo"] = codigoAsig
            asignatura["horarioGrupoAsignatura"] = horarioGrupoAsignatura
            #print(json.dumps(horarioGrupoAsignatura, indent=4, sort_keys=True))
            return asignatura
        else:
            error = {}
            error["message"] = "Ha ocurrido algun tipo de error"
            return error
    except Exception as e:
        error = {}
        error["message"] = str(e)
        print (str(e))
        return error


obtenerHorarioAsignatura(codigoAsig="26025", grupo="16")
