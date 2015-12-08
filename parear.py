# -*- coding: utf-8 -*-
#FUNCION PARA EL PAREO CON LATCH

def pair():

 import os, json, latch
     
 appid = input('Ingrese el Applicatrion ID:')
 while len(appid) == 0:
  print('Intente nuevamente...') 
  appid = input('Ingrese el Applicatrion ID:') 
    
 seckey = input('Ingrese Secret Key:')
 while len(seckey) == 0:
  print('Intente nuevamente...')
  seckey = input('Ingrese Secret Key:')
 
 api = latch.Latch(appid,seckey)
 
 pair_code = input('Ingrese el Pairing Code entregado por su celular:')
 while len(pair_code) == 0:
  print('Intente nuevamente...')
  pair_code = input('Ingrese el Pairing Code entregado por su celular:')
  
 response = api.pair(pair_code)
 responseData = str(response.get_data())
 responseData1 = responseData[15:-2]
 responseError = response.get_error()
 
 #ESCRIBIMOS LOS DATOS DEL PAREO EN UN ARCHIVO
 try:
  archivo = open('parear.data','w')
  archivo.write(appid + '\n')
  archivo.write(seckey + '\n')
  archivo.write(responseData1)
  input('Operacion realizada, pulse una tecla para continuar.. ')    
  archivo.close
 except IOError:
  print ('El archivo parear.data no existe o no tiene los permisos adecuados')
 
 if responseError != "" :
  print ('Error:' , responseError)
  input('Pulse una tecla para salir.. ')    
 try:
  salida=json.dumps(responseData)
 except (TypeError, ValueError) as err:
  print ('ERROR:', err)
  