# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import json

#Url para los grupos
urlGrupos = 'http://www.ehu.eus/--/web/vicer.grado-innovacion/aurtengo-graduak-campus-ikastegia?p_p_id=upvehuapp_WAR_upvehuappportlet&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=0&p_p_col_count=1&p_p_lifecycle=1&_upvehuapp_WAR_upvehuappportlet_action=redirectAction&reu=/pls/entrada/plew0040.htm_asignatura_next?p_sesion=&p_cod_idioma=CAS&p_en_portal=N&p_cod_centro=--&p_cod_plan=--&p_anyoAcad=act&p_pestanya=3&p_menu=principal&p_cod_asig=--&p_ciclo=X&p_curso=--&p_vengo_de=asig_cursos'

#Montar url de los grupos de la asignatura
def crearUrlGrupos(idioma, codCentro, codPlan, codAsig, curso):
    grupoURL = urlGrupos.split('--')
    return grupoURL[0]+idioma+grupoURL[1]+codCentro+grupoURL[2]+codPlan+grupoURL[3]+codAsig+grupoURL[4]+curso+grupoURL[5]

#Obtener el div con los en laces a los grupos
def obtenerDivGrupos(url):
    soup = BeautifulSoup(urlopen(url))
    div = soup.findAll("div", {"id":"enlacesCursos"})
    return div

#Obtener enlaces partiendo del div
def obtenerEnlacesGrupos(div):
    enlaces = div.findAll('a',{'class':'curso'})
    return enlaces


#Obtener nombreGrupo partiendo del enlace
def obtenerNombreGrupo(enlace):
    stringGrupo = enlace.getText()
    nombreGrupo = stringGrupo.split(' ')[0]
    return nombreGrupo

#Obtener boolean para saber si el objeto ya existe
def grupoNoExiste(grupos, grupo):
    for tGrupo in grupos:
        if tGrupo == grupo:
            return False
    return True

#Obtener Json de los grupos
def crearJsonGrupos(idioma, codCentro, codPlan, codAsig, curso):
    grupos = []
    url = crearUrlGrupos(idioma, codCentro, codPlan, codAsig, curso)
    div = obtenerDivGrupos(url)
    enlaces = obtenerEnlacesGrupos(div[0])
    for enlace in enlaces:
        grupo = obtenerNombreGrupo(enlace)
        if grupoNoExiste(grupos, grupo):
            grupos.append(grupo)
    lista_grupos = {}
    lista_grupos['grupos'] = grupos
    return lista_grupos

def obtenerGruposAsignaturaInformatica(codAsig, curso):
    jsonGrupos = crearJsonGrupos('es', '226', 'GINFOR20', codAsig, curso)
    return jsonGrupos
