# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import json

#Url para los asignaturas
urlAsignaturas = 'http://www.ehu.eus/--/web/vicer.grado-innovacion/aurtengo-graduak-campus-ikastegia?p_p_id=upvehuapp_WAR_upvehuappportlet&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=0&p_p_col_count=1&p_p_lifecycle=1&_upvehuapp_WAR_upvehuappportlet_action=redirectAction&reu=/pls/entrada/plew0040.htm_siguiente?p_sesion=&p_cod_idioma=CAS&p_en_portal=N&p_cod_centro=--&p_cod_plan=--&p_anyoAcad=act&p_pestanya=3&p_menu=asig_cursos'

#Monta la url de las asignaturas
def crearUrlAsignatura(idioma, codCentro, codPlan):
    asignaturaURL = urlAsignaturas.split('--')
    return asignaturaURL[0]+idioma+asignaturaURL[1]+codCentro+asignaturaURL[2]+codPlan+asignaturaURL[3]

def obtenerAsignaturas(url):
    soup = BeautifulSoup(urlopen(url))
    asignaturas = soup.findAll('a', {'class':'asig'})
    return asignaturas

def obtenerCursoAsignatura(asignatura):
    return asignatura['href'].split('p_curso=')[1][0:1]

def obtenerNombreAsignatura(asignatura):
    return asignatura.getText()

def obtenerCodigoAsignatura(asignatura):
    return asignatura['href'].split('p_cod_asig=')[1][0:5]

def obtenerEnalceAsignatura(asignatura):
    return 'http://www.ehu.eus/'+asignatura['href']


#Obtener Json de las asignaturas
def crearJsonAsignaturas(idioma, codCentro, codPlan):
    asignaturas = []
    url =  crearUrlAsignatura(idioma, codCentro, codPlan)
    listaAsig = obtenerAsignaturas(url)
    for asig in listaAsig:
        asignatura = {}
        asignatura['nombreAsignatura'] = obtenerNombreAsignatura(asig)
        asignatura['codigo'] = obtenerCodigoAsignatura(asig)
        asignatura['enlaceWebUPV'] = obtenerEnalceAsignatura(asig)
        asignatura['curso'] = obtenerCursoAsignatura(asig)
        asignatura['horarioGrupoAsignatura'] = []
        asignaturas.append(asignatura)
    lista_asignaturas = {}
    lista_asignaturas['asignaturas'] = asignaturas
    return lista_asignaturas

def obtenerAsignaturasGradoInformatica():
    asginaturasGradoInformatica = crearJsonAsignaturas('es','226','GINFOR20')
    return asginaturasGradoInformatica
