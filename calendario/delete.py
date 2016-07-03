import datetime

from icalendar import Event, vRecur

from calendario import util


def __suprimirDiasSinClase(evento, diasSinClase):
    for dia in diasSinClase:
        time = util.__eventTimeSplit(evento["dtstart"].dt)
        exdate = util.__fromOurDateToDatetime(dia["fecha"], None) + datetime.timedelta(hours=time[0], minutes=time[1])
        evento.add('exdate', exdate)

def __suprimirPeriodosHorarioEspecial(evento, periodoEspecial):
    for periodo in periodoEspecial:
        inicio = util.__fromOurDateToDatetime(periodo["fechaInicio"], None)
        fin = util.__fromOurDateToDatetime(periodo["fechaFin"], None)
        delta = fin - inicio
        time = util.__eventTimeSplit(evento["dtstart"].dt)
        evento.add('exdate', inicio)
        evento.add('exdate', fin)
        for i in range(delta.days + 1):
            evento.add('exdate', inicio + datetime.timedelta(days=i, hours=time[0], minutes=time[1]))

def __suprimirSemanasExcluidas(evento, semanas):
    
    for semana in semanas:
        inicio = util.__fromOurDateToDatetime(semana["primerDiaSemana"], None)
        time = util.__eventTimeSplit(evento["dtstart"].dt)
        for i in range(7):
            evento.add('exdate', inicio + datetime.timedelta(days=i, hours=time[0], minutes=time[1]))


def __suprimirIntercambio(evento, intercambios):
    """
        Funcion para suprimir los eventos de tipo intercambio
    """
    for intercambio in intercambios:
        time = util.__eventTimeSplit(evento["dtstart"].dt)
        exdate = util.__fromOurDateToDatetime(intercambio["diaOriginal"], None) + datetime.timedelta(hours=time[0], minutes=time[1])
        evento.add('exdate', exdate)


def __suprimirFiestas(eventos, data):
    """
        Elimina del evento los dias que hay fiestas
        El algoritmo no es nada eficiente
    """
    for evento in eventos:
        __suprimirDiasSinClase(evento, data["diasSinClase"])
        __suprimirPeriodosHorarioEspecial(evento, data["periodosHorarioEspecial"])
        __suprimirSemanasExcluidas(evento, data["semanasExcluidas"])
        __suprimirIntercambio(evento, data["intercambioDias"])

    return eventos
