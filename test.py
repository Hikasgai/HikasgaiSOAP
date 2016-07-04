import json

from ehuData import main
from calendario import calendar
from testMetodos import test_fhsa
#test_fhsa.bateriaPruebasFHSA()

print(json.dumps(main.obtenerHorarioAsignatura(codigoAsig="26025", grupo="16"), indent=4, sort_keys=True))

dataCalendar = {
            "cursoAcademico": "2016-2017",
            "inicioCuatrimestreUno": "2016/09/05",
            "inicioCuatrimestreDos": "2017/01/25",
            "finCuatrimestreUno": "2016/12/23",
            "finCuatrimestreDos": "2017/05/19",
            "diasSemanalesNoLectivos": ["SA", "SU"],
            "diasSinClase": [{
                "motivo": "FiestaNacional",
                "fecha": "2016/09/21"
            }, {
                "motivo": "NoPresencial",
                "fecha": "2016/11/22"
            }],
            "periodosHorarioEspecial": [{
                "fechaInicio": "2016/10/15",
                "fechaFin": "2016/10/23",
                "motivo": "FinDeTrabajos"
            },
            {
                "fechaInicio": "2016/12/01",
                "fechaFin": "2016/12/10",
                "motivo": "Examenes"
            }],
            "semanasExcluidas": [{
                "primerDiaSemana": "2016/10/02",
                "motivo":"Pascua"
            }],
            "intercambioDias": [{
                "diaOriginal": "2016/11/04",
                "diaPorQueSeCambia": "Martes"
            }]
        }

data =  [
    {
        "diaSemana": "THU",
        "horaFin": "17:00",
        "horaInicio": "15:40",
        "rangoSemanas": "16-30",
        "tipoEvento": "GA"
    },
    {
        "diaSemana": "MON",
        "horaFin": "19:15",
        "horaInicio": "17:15",
        "rangoSemanas": "1-15",
        "tipoEvento": "M"
    },
    {
        "diaSemana": "THU",
        "horaFin": "15:40",
        "horaInicio": "15:00",
        "rangoSemanas": "1-15",
        "tipoEvento": "M"
    }
]

calendar.crearCalendarioCompleto(data, dataCalendar)
calendar.crearCalendarioAsignatura(data, dataCalendar)
calendar.crearCalendario(dataCalendar)
calendar.crearHorario(data)
