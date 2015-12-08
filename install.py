#!/usr/bin/python3
# -*- coding: utf-8 -*-
#MENU PRINCIPAL DEL PROGRAMA DE INSTALACION DE LATCHWAKE 
import os, json, latch, parear, equipos, servicio

def menu():
  os.system('clear')
  print ('\x1b[4mCONFIGURACION Y PAREADO WAKE ON LAN PARA LATCH\x1b[0m\n')
  print ('ELIJA LA OPCION:')
  print ('1 Parear LATCH')
  print ('2 Equipos')
  print ('3 Servicio')
  print ('4 Salir')

while True:
  menu()
  opcionMenu = input(">> ")
  
  if opcionMenu=="1":
   parear.pair()     
  elif opcionMenu=="2":
   equipos.menuequipos()
  elif opcionMenu=="3":
   servicio.menuservicio()
  elif opcionMenu=="4":
   break
  else:
   input("No has pulsado ninguna opcion correcta")
   