from geopy.geocoders import Nominatim
import json
import time

# Inicializar el geolocalizador con Nominatim
geolocator = Nominatim(user_agent="mi_aplicacion")

# Leer los códigos postales desde el archivo codigos_postales.json
with open("codigos_postales.json", "r", encoding="utf-8") as file:
    zipcodes = json.load(file)

# Lista para almacenar los resultados
result = []

# Procesar cada código postal
for zipcode in zipcodes:
    if isinstance(zipcode, dict):
        code = zipcode.get("codigo", zipcode)  # Si es un diccionario, toma 'codigo'
    else:
        code = str(zipcode)  # Si es solo un string, conviértelo

    query = f"{code}, Mexico"
    try:
        location = geolocator.geocode(query, country_codes="mx")  # Restringir a México
        if location:
            result.append({
                "codigo_postal": code,
                "latitud": location.latitude,
                "longitud": location.longitude
            })
        else:
            result.append({
                "codigo_postal": code,
                "error": "No encontrado en México"
            })
    except Exception as e:
        result.append({
            "codigo_postal": code,
            "error": str(e)
        })
    time.sleep(1)  # Pausa límites de la API

# Guardar los resultados 
with open("coordinates.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

print("Coordenadas guardadas en coordinates.json")