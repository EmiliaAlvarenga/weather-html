import json
import requests



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
print "La temperatura en %s es de: %.2f"% (provincia,celcius)
