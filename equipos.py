# -*- coding: utf-8 -*-
import os
 
def introducir():
  try:
    macaddress = input('Ingrese la MAC ADDRESS>>')
    while len(macaddress) == 0:
      macaddress = input('Ingrese la MAC ADDRESS>>')
    archivo = open('equipos.data','a')
    archivo.write(macaddress + '\n')
    archivo.close  
    input('Equipo insertado, pulse una tecla para salir.. ')
  except:
    print ('No se ha podido realizar la operacion')
      
def listar():
  try:
    os.system("more equipos.data")
    input('Pulse una tecla para continuar.. ')
  except:
    print ('No se ha podido listar los equipos')

def borrar():
  try:
    while True:
      opcionMenu = input("Desea borrar los equipos? S/N>> ")
      if opcionMenu=="S" or opcionMenu=="s":
        archivo = open('equipos.data','w')
        archivo.write('')
        archivo.close
        input('Equipos borrados, pulse una tecla para salir.. ')
        break  
      elif opcionMenu=="N" or opcionMenu=="n":
        break
      else: 
        print("No has pulsado ninguna opcion correcta")
  except:
    print ('No se ha podido realizar la operacion')
        
def menuequipos():  
  while True:
    os.system('clear')
    print ('\x1b[4mCONFIGURACION Y PAREADO WAKE ON LAN PARA LATCH\x1b[0m\n')
    print ('ELIJA LA OPCION:')
    print ('1 Introducir Equipos')
    print ('2 Listar equipos')
    print ('3 Borrar lista de equipos')
    print ('4 Salir')
    opcionMenu = input(">> ")
    if opcionMenu=="1":
      introducir()
    elif opcionMenu=="2":
      listar()
    elif opcionMenu=="3":
      borrar() 
    elif opcionMenu=="4":       
      break
    else:
      print("No has pulsado ninguna opcion correcta.")
   
