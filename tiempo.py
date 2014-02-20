import json
import requests
from jinja2 import Template

def direccion_vi(cadena):
    if cadena>337.5 and cadena<360.0 or cadena>0 and cadena<22.5:
        return "N"
    if cadena>=22.5 and cadena<67.5:
        return "NE"
    if cadena>=67.5 and cadena<112.5:
        return "E"
    if cadena>=112.5 and cadena<157.5:
        return "SE"
    if cadena>=157.5 and cadena<202.5:
        return "S"
    if cadena>202.5 and cadena<247.5:
        return "SE"    
    if cadena>=247.5 and cadena <292.5:
        return "O"
    if cadena>=292.5 and cadena<337.5:
        return "NO"

capital=["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla"]
for i in capital:
    respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %i})
    datos= respuesta.text
    dicc_api=json.loads(datos)
    kelvin=dicc_api["main"]["temp"]
    celcius=kelvin-273
    temp_minima=dicc_api["main"]["temp_min"]-273
    temp_maxima=dicc_api["main"]["temp_min"]-273
   velocidad_viento=dicc_api["wind"]["speed"]*1.61
    viento=int(dicc_api["wind"]["deg"])
    direccion_viento=direccion_vi(viento)
html=''
f=open('plantilla1.html','r')
for linea in f:
    html += linea
mi_template=Template(html)
salida=mi_template.render(capitalh=capital, temp_minima=temp_minima,temp_maxima=temp_maxima,viento=velocidad_viento,direccion_viento=direccion_viento)
print salida
