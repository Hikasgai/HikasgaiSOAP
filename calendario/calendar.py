import traceback

from icalendar import Calendar

from calendario import events
from calendario import delete as suprimir

def crearCalendario(data):

    cal = Calendar()
    eventos = events.__crearEventosCalendarioAnual(data)
    for evento in eventos:
        cal.add_component(evento)

    cal_content = cal.to_ical()
    with open("cal.ics", 'wb') as f:
        f.write(cal_content)



def crearCalendarioCompleto(data, calendario):
    cal = Calendar()
    #TODO: Gestionar mas de una asignatura, meterlo un for basicamente
    eventos = events.__crearEventosHorario(data, inicioCuatrimestre=calendario["inicioCuatrimestreUno"], inicioCuatrimestreDos=calendario["inicioCuatrimestreDos"], exclusiones=calendario["semanasExcluidas"])
    suprimir.__suprimirFiestas(eventos, calendario)
    eventos += events.__crearEventosCalendario(calendario)
    for evento in eventos:
        cal.add_component(evento)
    cal_content = cal.to_ical()
    with open("cal1.ics", 'wb') as f:
        f.write(cal_content)
    calJSON = {
        "calendario": cal_content
    }
    return calJSON

def crearCalendarioAsignatura(data, fiestas):
    """
        Funcion para crear el horario de una asignatura libre de fiestas y dias especiales
    """
    cal = Calendar()
    eventos = events.__crearEventosHorario(data)
    suprimir.__suprimirFiestas(eventos, fiestas)
    for evento in eventos:
        cal.add_component(evento)
    cal_content = cal.to_ical()
    with open("cal2.ics", 'wb') as f:
        f.write(cal_content)
    calJSON = {
        "calendario": cal_content
    }
    return calJSON

def crearHorario(data):
    try:
        cal = Calendar()
        eventos = events.__crearEventosHorario(data)
        for evento in eventos:
            cal.add_component(evento)
        cal_content = cal.to_ical()
        with open("cal3.ics", 'wb') as f:
            f.write(cal_content)
        calJSON = {
            "calendario": cal_content
        }
        return calJSON

    except Exception as e:
        print(str(e))
        traceback.print_tb(e.__traceback__)
