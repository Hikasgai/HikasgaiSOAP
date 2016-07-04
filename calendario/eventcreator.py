import datetime
from icalendar import Event, vRecur
from calendario import util

def __crearEventoUnico(inicio, fin, titulo):
    """
        Funcion para crear eventos con los campos basicos
    """
    evento = Event()
    evento.add('dtstart', inicio)
    if fin is not None:
        evento.add('dtend', fin)
    evento.add('summary', titulo)
    evento.add('description', titulo)
    evento['uid'] = str(inicio).replace(" ", "") + '@hikasgai.com'
    return evento

def __crearEventosDiasSinClase(data):
    """
        Funcion para crear los eventos del calendario que son dias sin clase
    """
    eventos = []
    for dia in data:
        inicio = util.__fromOurDateToDatetime(dia["fecha"], None)
        eventos.append(__crearEventoUnico(inicio, None, dia["motivo"]))
    return eventos

def __crearEventosHorarioEspecial(data):
    """
    Funcion para crear los eventos de horario especial
    """
    eventos = []
    for periodo in data:
        inicio = util.__fromOurDateToDatetime(periodo["fechaInicio"], "00:00")
        fin = util.__fromOurDateToDatetime(periodo["fechaFin"], "23:59")
        eventos.append(__crearEventoUnico(inicio, fin, periodo["motivo"]))
    return eventos

def __crearEventoIntercambio(data):
    """
        Funcion para crear los eventos de tipo intercambio
    """
    eventos = []
    for intercambio in data:
        titulo = "Dia de " + intercambio["diaPorQueSeCambia"]
        inicio = util.__fromOurDateToDatetime(intercambio["diaOriginal"], None)
        eventos.append(__crearEventoUnico(inicio, None, titulo))
    return eventos

def __crearEventosSemanasExcluidas(data):
    """
        Funcion para crear los eventos de las semanas excluidas
    """
    eventos = []
    for semana in data:
        inicio = util.__fromOurDateToDatetime(semana["primerDiaSemana"], None)
        ultimoDia = inicio + datetime.timedelta(days=6)
        evento = __crearEventoUnico(inicio, ultimoDia, semana["motivo"])
        eventos.append(evento)
    return eventos

def __crearEventosDiasLectivos(primerDia, ultimoDia, diasDeClase):
    """
        Funcion para crear los eventos de los dias lectivos
    """
    diaLectivo = Event()
    inicio = util.__fromOurDateToDatetime(primerDia, None)
    ultimoDia = util.__fromOurDateToDatetime(ultimoDia, None)
    diaLectivo.add('dtstart', inicio)
    diaLectivo.add('summary', "Dia lectivo")
    diaLectivo.add('rrule', {'freq': 'daily', 'until': ultimoDia, "byday": diasDeClase})
    return diaLectivo
