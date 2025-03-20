# Geocodificación de Códigos Postales

Este repositorio contiene un script en Python que obtiene las coordenadas geográficas (latitud y longitud) a partir de una lista de códigos postales en formato JSON. Utiliza la API de **Nominatim** (OpenStreetMap) para realizar la geocodificación.

---

## Requisitos

Para ejecutar este proyecto, necesitas:

1. **Python 3.x** instalado en tu sistema.
2. Las siguientes bibliotecas de Python:
   - `geopy`
   - `json`
   - `time`

Puedes instalar las dependencias usando el siguiente comando:

```bash
pip install geopy
```

---

## Estructura del Proyecto

El repositorio tiene la siguiente estructura:

```
geocodificacion-codigos-postales/
├── zipcodes_sample.json       # Archivo JSON ejemplo con los códigos postales
├── coordenadas.json           # Archivo JSON de salida con las coordenadas
├── get_coordinates.py         # Script principal de Python
└── README.md                  # Este archivo
```

---

## Uso

### 1. Preparar el archivo de entrada (`codigos_postales.json`)

El archivo `codigos_postales.json` debe contener una lista de objetos JSON con los códigos postales que deseas geocodificar. Ejemplo:

```json
[
    {"codigo": "28001"},
    {"codigo": "08001"},
    {"codigo": "41001"}
]
```

### 2. Ejecutar el script

Ejecuta el script `get_coordinates.py` desde la terminal:

```bash
python get_coordinates.py
```

El script:
1. Cargará los códigos postales desde `codigos_postales.json`.
2. Realizará la geocodificación utilizando Nominatim.
3. Guardará los resultados en `coordenadas.json`.

### 3. Resultados

El archivo `coordenadas.json` contendrá las coordenadas (latitud y longitud) para cada código postal. Ejemplo de salida:

```json
[
    {
        "codigo_postal": "28001",
        "latitud": 40.4225,
        "longitud": -3.68056
    },
    {
        "codigo_postal": "08001",
        "latitud": 41.3825,
        "longitud": 2.17694
    }
]
```

Si un código postal no se encuentra o ocurre un error, se registrará un mensaje de error en el archivo de salida.

---

## Consideraciones

- **Límites de uso**: Nominatim tiene un límite de 1 solicitud por segundo. El script incluye una pausa de 1 segundo entre cada solicitud para cumplir con esta restricción.
- **Atribución**: Si usas Nominatim, debes proporcionar atribución a OpenStreetMap. Más información en [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/).
- **API Key**: Si necesitas mayor volumen de solicitudes, considera usar una API comercial como Google Maps o Here Maps.

---

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
