# -*- coding: utf-8 -*-
#ACTIVACION O DESACTIVACION DE SERVICIOS LATCHWAKE 
import os, shutil

#COPIAR ARCHIVO PARA EL SERVICIO AL INICIO DEL SISTEMA
def activaron():
  try:
   shutil.copy("latchwake", "/etc/init.d/latchwake")
   os.system("update-rc.d latchwake defaults >/dev/null 2>&1")
   os.system("/etc/init.d/latchwake start >/dev/null 2>&1")
   input('Operacion realizada, pulse una tecla para continuar.. ')
  except:
   print ('Error, no se ha podido agregar el servicio Latchwake.')
  
def desactivaron():
 #ELIMINAR SERVICIO EN EL INICIO DEL SISTEMA
  try:
   os.system("/etc/init.d/latchwake stop >/dev/null 2>&1")
   os.system("update-rc.d latchwake remove >/dev/null 2>&1")
   input('Operacion  realizada, pulse una tecla para continuar.. ')
  except:
   print ('Error, no se ha podido eliminar el servicio Latchwake.')
                   
def menuservicio():
  os.system('clear')
  print ('\x1b[4mCONFIGURACION Y PAREADO WAKE ON LAN PARA LATCH\x1b[0m\n')
      
  while True:
   opcionMenu = input("Desea activar el servicio en el arranque del sistema? S/N>> ")
  
   if opcionMenu=="S" or opcionMenu=="s":
    activaron()
    break     
   elif opcionMenu=="N" or opcionMenu=="n":
    desactivaron()
    break
   else:
    print("No has pulsado ninguna opcion correcta.")
       