import datetime


def __switch_dias(dia):
    """
    Funcion que hace de swicth porque no se les ocurrio hacerlo a los que crearon el lenguaje
     y tengo que estar haciendolo yo aunque ahora no la uso
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

def __getPosDiaSemana(dia):
    """
        Convierte el string en la posicion correspondiente al dia de la semana
    """
    switcher = {
        "MON": 1,
        "TUE": 2,
        "WED": 3,
        "THU": 4,
        "FRI": 5,
        "SAT": 6,
        "SUN": 7
        }
    return switcher.get(dia, 1)

def __eliminarDias(diasExcluidos):
    """
        Funcion para devolver una lista con los dias de la semana excluyendo los que se pasan como parametro
    """
    dias = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    for ex in diasExcluidos:
        if ex in dias:
            dias.remove(ex)
    return dias

def __fromOurDateToDatetime(day, time, mytimedelta=0):
    """
        Convierte el formato normalizado de fecha a datetime
    """
    day_date = day.split(" ")
    date_array = day_date[0].split("/")
    if time is not None:
        time_array = time.split(":")
        newDate = datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2]), int(time_array[0]), int(time_array[1]), 0)
    else:
        newDate = datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2]))
    newDate += datetime.timedelta(days=mytimedelta)
    return newDate

def __eventTimeSplit(time):
    """
        Funcion para convertir del formato date de los eventos a un array de enteros
    """
    starttime = str(time)
    date_split = starttime.split(" ")
    time = date_split[1].split(":")
    for i, item in enumerate(time):
        time[i] = int(item)
    return time
