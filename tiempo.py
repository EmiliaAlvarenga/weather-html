import json
import requests
import jinja2

def direccion_vi(cadena):
    if cadena>=337.5 and cadena<22.5:
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

cadena = """
1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla

"""
print cadena


# creacion del diccionario en python 
dicc_ciudad={'1':'Almeria','2':'Cadiz','3':'Cordoba','4':'Granada','5':'Huelva','6':'Jaen','7':'Malaga','8':'Sevilla'}

#usando la api de weather
id_ciudad=raw_input("De que ciudad quieres saber la temperatura actual? : ")
provincia=dicc_ciudad[id_ciudad]
respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %provincia})
datos= respuesta.text
dicc_api=json.loads(datos)
kelvin=dicc_api["main"]["temp"]
celcius=kelvin-273
temp_minima=dicc_api["main"]["temp_min"]
minima_celcius=temp_minima-273
temp_maxima=dicc_api["main"]["temp_min"]
maxima_celcius=temp_maxima-273
velocidad_viento=dicc_api["wind"]["speed"]
viento=int(dicc_api["wind"]["deg"])
direccion_viento=direccion_vi(viento)
print "La temperatura en %s es de: %.2f"% (provincia,celcius)
print "Temperatura minima prevista: %2.f"%(minima_celcius)
print "Temperatura maxima prevista: %2.f"%(maxima_celcius)
print "Viento: %2.f Km/h Direccion: %s"%(velocidad_viento,direccion_viento) 
