#!/usr/bin/env python

import json
import requests
from jinja2 import Template
import os
import webbrowser

#funcion que devuelve la orientacion del viento norte N,nordeste NE,este E, ......
def direccion_vi(cadena):
	if cadena>=337.5 and cadena<=360.0 or cadena>=0 and cadena<22.5:
		return "N"
	if cadena>=22.5 and cadena<=67.5:
		return "NE"
	if cadena>=67.5 and cadena<112.5:
		return "E"
	if cadena>=112.5 and cadena<157.5:
		return "SE"
	if cadena>=157.5 and cadena<202.5:
		return "S"
	if cadena>=202.5 and cadena<247.5:
		return "SE" 
	if cadena>=247.5 and cadena <292.5:
		return "O"
	if cadena>=292.5 and cadena<337.5:
		return "NO"
		
# creacion del diccionario en python 
dicc_ciudad={'1':'Almeria','2':'Cadiz','3':'Cordoba','4':'Granada','5':'Huelva','6':'Jaen','7':'Malaga','8':'Sevilla'}
ciudades=dicc_ciudad.keys() #claves usaremos para buscar un valor especifico en diccionario 
f=open('plantilla1.html','r')
f_weather=open('weather.html','w')
html=''
temp_min =[]
temp_max = []
vel_viento = []
direccion = []
capital=[]
  
for ciudad in ciudades:
	respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %ciudad})
	capital.append(dicc_ciudad[ciudad]) #buscamos en el diccionario el valor de la ciudad evaluada
	datos= respuesta.text
	dicc_api=json.loads(datos)
	viento=float(dicc_api["wind"]["deg"])
	direccion.append(direccion_vi(viento))
	temp_min.append(int(dicc_api["main"]["temp_min"]-272.15))#pasamos la temperatura a grados celsius
	temp_max.append(int(dicc_api["main"]["temp_max"]-273.15))
	vel_viento.append(int(dicc_api["wind"]["speed"]*1.61))#pasamos las millas/hora a kilometro/hora
for linea in f:
  html += linea
mi_template=Template(html)
salida=mi_template.render(ciudades=capital, temp_minima=temp_min, temp_maxima=temp_max, viento=vel_viento, direccion_viento=direccion)
f_weather.write(salida)
webbrowser.open("weather.html")
