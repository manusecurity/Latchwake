#!/usr/bin/python3
# -*- coding: utf-8 -*-
#SCRIPT QUE COMPRUEBA SI SE DEBE ENCENDER O NO LOS EQUIPOS
import os, sys, latch, syslog, wol, time

while True:   
#CARGAMOS LOS DATOS DE PAREO
    try:
        archivoparear = open( '/usr/local/src/latchwake/parear.data', 'r' )
        linea = list(archivoparear)
        LATCH_APP_ID = (linea[0]).strip()
        LATCH_SECRET = (linea[1]).strip()
        latchuserid = (linea[2]).strip()
        archivoparear.close()  
    except IOError:
        syslog.syslog(syslog.LOG_ERR, "El archivo parear.data no existe o no tiene los permisos adecuados.")
        break
    try:
        latcheo = latch.Latch(LATCH_APP_ID, LATCH_SECRET)    
        response = latcheo.status(latchuserid)    
        if response.get_data()['operations'][LATCH_APP_ID]['status'] == 'on':
            #SI EL SISTEMA LATCH NOS DICE QUE ESTA ESTA EN ON, CARGA EL FICHERO DE LAS MAC-ADDRESS DE LOS EQUIPOS A ENCENDER
            try:
                archivoequipos=open('/usr/local/src/latchwake/equipos.data','r')
                linea=archivoequipos.readline()
                while linea!="":
                    #ENCIENDE LOS EQUIPOS
                    wol.send_magic_packet(linea.strip())
                    linea=archivoequipos.readline()
                    archivoequipos.close()
            except IOError:
                syslog.syslog(syslog.LOG_ERR, "El archivo equipos.data no existe o no tiene los permisos adecuados.")
                break               
        
            else:
                pass
    except:
        syslog.syslog(syslog.LOG_ERR, "No se ha podido conectar con el servidor de Latch.")    
    
    time.sleep(30)
    