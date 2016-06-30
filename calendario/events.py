import datetime
from icalendar import Event, vRecur
import json
from datetime import datetime
from dateutil.rrule import rruleset,rrulestr

def __switch_dias(dia):
    """
    Funcion que hace de swicth porque no se les ocurrio hacerlo a los que crearon el lenguaje
     y tengo que estar haciendolo yo aunque ahora no la uso
    """
    switcher = {
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes"
    }
    return switcher.get(dia, "lunes", titulo)

def __eliminarDias(diasExcluidos):
    """
        Funcion para devolver una lista con los dias de la semana excluyendo los que se pasan como parametro
    """
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    for ex in diasExcluidos:
        dias = filter(lambda a: a != ex, dias)
    return dias

def __crearEventosHorario(data):
    """
        Funcion para generar los eventos que son de tipo horario
        Recibe un json cumpliendo la especificacion
    """
    lista_eventos = []
    for dia in data["horario"]["dias"]:
        for modulo in dia["modulo"]:
            evento = Event()
            horaInicio = ""#De donde saco el dia?
            horaFin = ""#Idem
            ultimoDia = ""#Necesito los datos para calcular el ultimo dia
            event.add('summary', data["codigo"])
            event.add('rrule', {'freq': 'weekly', 'duration': ultimoDia})
            event['uid'] = str(horainicio) + '@hikasgai.com'
            lista_eventos.append(evento)
    return lista_eventos


def __crearEventoUnico(inicio, fin, titulo):
    evento = Event()
    evento.add('dtstart', inicio)
    evento.add('dtend', fin)
    evento.add('summary', titulo)
    return evento


def __crearEventosDiasSinClase(data):
    eventos = []
    for dia in data:
        eventos.append(__crearEventoUnico(inicio, fin, dia["motivo"]))
    return eventos

def __crearEventosHorarioEspecial(data):
    eventos = []
    for periodo in data:
        eventos.append(__crearEventoUnico(inicio, fin, periodo["motivo"]))
    return eventos

def __crearEventoIntercambio(data):
    eventos = []
    for intercambio in data:
        titulo = "Dia de " + intercambio["diaPorQueSeCambia"]
        eventos.append(__crearEventoUnico(inicio, fin, titulo))

def __crearEventosDiasLectivos(data):

    diaLectivo = Event()
    inicio = data["inicioCuatrimestreUno"]
    fin = data["finCuatrimestreUno"]
    evento.add('dtstart', inicio)
    evento.add('dtend', fin)
    evento.add('summary', titulo)
def __crearEventosCalendario(data):
    """
        Funcion para generar los eventos de tipo calendario,
        eventos de dias completos.
    """
    eventos = []
    eventos.append(__crearEventosDiasSinClase(data["diasSinClase"]))
    eventos.append(__crearEventosHorarioEspecial(data["periodosHorarioEspecial"]))
    eventos.append(__crearEventoIntercambio(data["intercambioDias"]))
    return eventos
