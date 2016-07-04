import json
import re

from ehuData import main as ehu


def bateriaPruebasFHSA():

    print ('probando el metodo obtenerHorarioAsignatura con los parametros ---> codigoAsig=26025,grupo=16 \n')
    jsonHorario = ehu.obtenerHorarioAsignatura(codigoAsig="26025",grupo="16")
    testFSHA(jsonHorario)
    print (str(jsonHorario))
    print ("Fin de prueba")


def testFSHA(horarioAsig):

    resultadoPositivo = False
    comprobarCodigo(horarioAsig["codigo"])
    for horarioGrupo in horarioAsig["horarioGrupoAsignatura"]:
        comprobarIDGrupo(horarioGrupo["IDGrupo"])
        comprobarDiaEnumerado(horarioGrupo["horarioEspecial"])

        for evento in horarioGrupo["eventos"]:
            comprobarTipoEvento(evento["tipoEvento"])
            comprobarDiaEnumerado(evento["diaSemana"])
            comprobarRangoSemanas(evento["rangoSemanas"])
            comprobarHora(evento["horaInicio"])
            comprobarHora(evento["horaFin"])
    '''

    for dia in horarioAsig["dias"]:
        for modulo in dia["modulos"]:
            if comprobarRangoSemanas(modulo["rangoSemanas"]):
                resultadoPositivo = True
                print ("rangoSemanas ok!")
            if comprobarHora(modulo["horaInicio"]) and comprobarHora(modulo["horaFin"]):
                print ("horaFin y horaInicio ok!")
                resultadoPositivo = True
    return resultadoPositivo
'''
def comprobarCodigo(cod):
    if len(cod) == 2:
        print ("Formato codigo OK")
    else:
        print ("Formato codigo no tiene longitud 2 ERROR  valor variable =" + str(cod))

def comprobarIDGrupo(ID):
        if len(ID)  == 5:
            print ("Formato IDGrupo OK")
        else:
            print ("Formato IDGrupo no tiene longitud 5 ERROR valor variable =" + str(ID))

def comprobarRangoSemanas(rangoSemanas):
    print ("Analizando rangoSemanas: " + str(rangoSemanas))
    patron = re.compile("^[0-9]?[0-9]-[0-9]?[0-9]$")
    ok = patron.match(rangoSemanas)
    if not patron.match(rangoSemanas):
        print ("El rango de semanas tiene que ser 1-5  y es: " + rangoSemanas + " ERROR !!")
    else:
        print ("Rango Semanas OK")
    return ok

def comprobarHora(hora):
    print ("Analizando hora" + str(hora))
    patron = re.compile("^\d{2}:\d{2}$")
    ok = patron.match(hora)
    if not ok:
        print ("La hora tiene que ser 12:00 y es : " + hora)
    return ok

def comprobarDiaEnumerado(dia):
    if dia == "MON" or "TUE" or  "WED" or "THU" or "FRI" or "SAT" or "SUN":
        print ("El enumerado de dia OK")
    else:
        print ("El formato de dia ERROR el valor tiene que ser MON, TUE, WED, THU, FRI, SAT, SUN y es" + str(dia))

def comprobarTipoEvento(tipo):
    if tipo == "M" or "S" or "GA" or "GL" or "GO" or "GCL" or "TA" or "TI" or "GCA":
        print ("El formato del tipoEvento OK")
    else:
        print ("El formato tipoEvento es incorrecto ERROR, el valor tiene que ser M,S,GA,GL,GO,GCL,TA,TI,GCA y es" +srt(tipo))
