import datetime
from icalendar import Event, vRecur
import json

from dateutil.rrule import rruleset,rrulestr

from calendario import util
from calendario import eventcreator as create
from calendario import delete



def __crearEventosHorario(data, inicioCuatrimestre="2016/09/05 MON", inicioCuatrimestreDos="2017/01/23 THU", exclusiones=[]):
    """
        Funcion para generar los eventos que son de tipo horario
        Recibe un json cumpliendo la especificacion
    """
    lista_eventos = []

    for modulo in data:
        semanas = modulo["rangoSemanas"].split("-")
        gapSemanaInicio = ((int(semanas[0]) - 1) * 7) + util.__getPosDiaSemana(modulo["diaSemana"])
        gapSemanaFin = gapSemanaInicio + ((int(semanas[1]) - int(semanas[0]) + len(exclusiones)) * 7 )

        if int(semanas[0]) < 16: #En funcion de la semana toma como referencia el inicio de un cuatrimestre u otro
            diaInicial = inicioCuatrimestre
        else:
            diaInicial = inicioCuatrimestreDos
            gapSemanaInicio -= (15*7)

        inicio = util.__fromOurDateToDatetime(diaInicial, modulo["horaInicio"], gapSemanaInicio)
        fin = util.__fromOurDateToDatetime(diaInicial, modulo["horaFin"], gapSemanaInicio)
        ultimoDia =  util.__fromOurDateToDatetime(diaInicial, modulo["horaFin"], gapSemanaFin)
        evento = create.__crearEventoUnico(inicio, fin, modulo["tipoEvento"])
        evento.add('rrule', {'freq': 'weekly', 'until': ultimoDia})
        lista_eventos.append(evento)
    return lista_eventos

def __crearEventosCalendario(data):
    """
        Funcion para crear los eventos del calendario sin tener en cuenta los dias lectivos
    """
    diasSinClase = create.__crearEventosDiasSinClase(data["diasSinClase"])
    periodosHorarioEspecial = create.__crearEventosHorarioEspecial(data["periodosHorarioEspecial"])
    intercambioDias = create.__crearEventoIntercambio(data["intercambioDias"])
    semanasExcluidas = create.__crearEventosSemanasExcluidas(data["semanasExcluidas"])
    eventos = diasSinClase + periodosHorarioEspecial + intercambioDias + semanasExcluidas
    return eventos

def __crearEventosCalendarioAnual(data):
    """
        Funcion para generar los eventos de tipo calendario,
        eventos de dias completos. Se tienen en cuenta los dias lectivos.
    """
    diasLectivos = []
    dias = util.__eliminarDias(data["diasSemanalesNoLectivos"])
    primerCuatrimestre = create.__crearEventosDiasLectivos(data["inicioCuatrimestreUno"], data["finCuatrimestreUno"], dias)
    segundoCuatrimestre = create.__crearEventosDiasLectivos(data["inicioCuatrimestreDos"], data["finCuatrimestreDos"], dias)
    diasLectivos.append(primerCuatrimestre)
    diasLectivos.append(segundoCuatrimestre)
    diasLectivos = delete.__suprimirFiestas(diasLectivos, data)
    eventos = __crearEventosCalendario(data) + diasLectivos
    return eventos
