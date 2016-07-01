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
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes"
    }
    return switcher.get(dia, "lunes")

def __obtenerNombreAsig(html):
    contenido = html.find("div", {"id": "contenido_"})
    titulo = contenido.find("h1").getText()
    return titulo.split("-")[1]

def __getPosDia(data, dia):
    for i, obj in enumerate(data):
        if obj["diaSemana"] == dia:
            return i
    return -1

def __crearNuevoModulo(rangoSemanas, rango_horas):
    obj = {}
    obj["rangoSemanas"] = rangoSemanas
    obj["horaInicio"] = rango_horas[0]
    obj["horaFin"] = rango_horas[1]
    return obj
def __generarHorarios(diasAsignatura, regex, titulo, html):
    tabla = html.find(text=re.compile(regex)).findNext('table')
    semanas = tabla.select("tbody tr")

    rangoSemanas = "0-15" #Valor por defecto
    for rango_semanas in semanas:
        columnas = rango_semanas.find_all('td')
        i = 0
        for columna in columnas:
            if i == 0:
                rangoSemanas = columna.getText()
            elif columna.getText() != "--":

                diaSemana = switch_dias(i)
                pos = __getPosDia(diasAsignatura, diaSemana)

                if pos != -1: #Aniado un modulo nuevo al dia existente
                    diasAsignatura[pos]["modulos"].append(__crearNuevoModulo(rangoSemanas, columna.getText().split("-")))
                else: #Creo un dia nuevo en el array
                    diaNuevo = {}
                    diaNuevo["diaSemana"] = diaSemana
                    diaNuevo["horarioEspecial"] = False
                    diaNuevo["modulos"] = []
                    diaNuevo["modulos"].append(__crearNuevoModulo(rangoSemanas, columna.getText().split("-")))
                    diasAsignatura.append(diaNuevo)
            i = i+1
    return diasAsignatura

def __obtenerHorarioTeorico(diasAsignatura, grupo, html):
    """
        Funcion para obtener el horario de las clases teoricas de una asignatura
    """
    regex = "Grupos:." + grupo + ".T"
    return __generarHorarios(diasAsignatura, regex, "Clase teorica", html)

def __obtenerHorarioPractico(diasAsignatura, grupo, html):
    """
        Funcion para obtener el horario de las clases practicas de una asignatura
    """
    regex = "Grupos:." + grupo + ".P"
    return __generarHorarios(diasAsignatura, regex, "Clase practica", html)


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

            horario = {}
            dias = __obtenerHorarioTeorico([], grupo, html)
            horario["dias"] = __obtenerHorarioPractico(dias, grupo, html)
            horario["codigo"] = codigoAsig
            print(json.dumps(horario, indent=4, sort_keys=True))
        else:
            error = {}
            error["message"] = "Ha ocurrido algun tipo de error"
            return error
    except Exception, e:
        error = {}
        error["message"] = str(e)
        print str(e)
        return error

def getInicioCuatrimestre():
    return None

def getDiasSemanas():
    """
        Esto deberia hacerse automatico pero no se de donde sacar los datos
        asi que hago la  trampa y los meto a mano.
        Creo que todas las facultades tienen las mismas semanas, al menos en la guia.
        Lo he sacado de aqui: http://www.ehu.eus/documents/1675541/1827566/Calendario+2016-2017.pdf
    """
    #Cada posicion del array corresponde a la semana i+1 y al dia de inicio de las clases
    data = [
        { "anio": "2016","mes": "09","dia": "05" },
        { "anio": "2016","mes": "09","dia": "12" },
        { "anio": "2016","mes": "09","dia": "19" },
        { "anio": "2016","mes": "09","dia": "26" },
        { "anio": "2016","mes": "10","dia": "03" },
        { "anio": "2016","mes": "10","dia": "10" },
        { "anio": "2016","mes": "10","dia": "17" },
        { "anio": "2016","mes": "10","dia": "24" },
        { "anio": "2016","mes": "10","dia": "31" },
        { "anio": "2016","mes": "11","dia": "07" },
        { "anio": "2016","mes": "11","dia": "14" },
        { "anio": "2016","mes": "11","dia": "21" },
        { "anio": "2016","mes": "11","dia": "28" },
        { "anio": "2016","mes": "12","dia": "12" },
        { "anio": "2016","mes": "12","dia": "19" },
        { "anio": "2017","mes": "01","dia": "30" },
        { "anio": "2017","mes": "02","dia": "06" },
        { "anio": "2017","mes": "02","dia": "13" },
        { "anio": "2017","mes": "02","dia": "20" },
        { "anio": "2017","mes": "02","dia": "27" },
        { "anio": "2017","mes": "03","dia": "06" },
        { "anio": "2017","mes": "03","dia": "13" },
        { "anio": "2017","mes": "03","dia": "20" },
        { "anio": "2017","mes": "03","dia": "27" },
        { "anio": "2017","mes": "04","dia": "03" },
        { "anio": "2017","mes": "04","dia": "10" },
        { "anio": "2017","mes": "04","dia": "24" },
        { "anio": "2017","mes": "05","dia": "01" },
        { "anio": "2017","mes": "05","dia": "08" },
        { "anio": "2017","mes": "05","dia": "15" }
    ]
    return data

def getInicioSemana(sem):
    """
        Devuelve el dia de inicio de una semana en concreto
    """
    return getDiasSemanas()[sem-1]

obtenerHorarioAsignatura(codigoAsig="26025", grupo="16")
