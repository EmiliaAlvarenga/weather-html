#!/usr/bin/env python

import json
import requests
from jinja2 import Template
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

f=open('plantilla1.html','r')
f_weather=open('weather.html','w')
html=''
ciudades=["Almeria","Cadiz","Cordoba","Huelva","Jaen","Malaga","Sevilla"]
temp_min =[]
temp_max = []
vel_viento = []
direccion = []
  
for ciudad in ciudades:
    respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %ciudad})
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
salida=mi_template.render(ciudades=ciudades, temp_minima=temp_min, temp_maxima=temp_max, viento=vel_viento, direccion_viento=direccion)
f_weather.write(salida)
webbrowser.open("weather.html")
