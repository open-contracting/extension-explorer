# Datos de ubicación

Comunicar la ubicación del contrato propuesto o ejecutad es importante para muchos usuarios de los datos de contrataciones.

Esta extensión introduce dos propiedades en el nivel `items` para describir la ubicación:

- `deliveryAddress` - un bloque estándar `Address` que puede usarse para proporcionar una dirección postal donde deben entregarse los servicios.
- `deliveryLocation` - un nuevo bloque que consta de entradas GeoJSON y de diccionario geográfico para describir una gama más amplia de ubicaciones a las que se refiere la partida del contrato.

La columna `Category`  en la lista de código  `locationGazetteers.csv` indica si el diccionario geográfico tiene identificadores para todo el mundo ('Universal') o solo un subconjunto ('National' o 'Sub-National').

## Ejemplo

A continuación se muestra un ejemplo de un elemento geolocalizado:

````json
{
  "items": [
    {
      "id": "item1",
      "description": "Ceremonial Trumpets for Oxford Town Hall",
      "classification": {
        "description": "Trumpets",
        "scheme": "CPV",
        "id": "37312100",
        "uri": "http://purl.org/cpv/2008/code-37312100"
      },
      "deliveryLocation": {
        "geometry": {
          "type": "Point",
          "coordinates": [51.751944, -1.257778]
        },
        "gazetteer": {
          "scheme": "GEONAMES",
          "identifiers": ["2640729"]
        },
        "description": "Central Oxford",
        "uri": "http://www.geonames.org/2640729/oxford.html"
      },
      "deliveryAddress": {
        "postalCode": "OX1 1BX",
        "countryName": "United Kingdom",
        "streetAddress": "Town Hall, St Aldate's",
        "region": "Oxfordshire",
        "locality": "Oxford"
      },
      "unit": {
        "name": "Items",
        "value": {
          "currency": "GBP",
          "amount": 10000
        }
      },
      "quantity": 10
    }
  ]
}
``

If the procurement related to the rebuilding of a road, then the item could also specify more complex geometries such as:

```json
{
"deliveryLocation": {
  "geometry": {
    "type": "LineString",
    "coordinates": [ [ -1.256503402048622, 51.747792026616821 ], [ -1.256477837243949, 51.747500168748303 ], [ -1.256466773131763, 51.747365723021403 ], [ -1.256471969911729, 51.747246699996332 ], [ -1.256481860557471, 51.747182243160943 ], [ -1.256497618535434, 51.747079648666102 ] ]
  },
  "gazetteer": {
    "scheme": "OSMW",
    "identifiers": ["27895985"]
  },
  "description": "St Aldate's",
  "uri": "http://www.geonames.org/2640729/oxford.html"
}
}
````

Puede tomar el contenido del objeto geométrico, excluyendo la palabra clave `geometry`, y conectarlo a cualquier herramienta de GeoJSON para ver la forma en que se describe.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.4

- No permitir que `Location.geometry` y ` Location.gazetteer` sean null (bug se introdujo en v1.1.3)
- Corregir el orden de longitud y latitud en los campos de descripción deben ser iguales a la especificación GeoJSON.
- Describe los valores de elevación o altitud
- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que `Location.geometry.coordinates` tenga null en su matriz de coordenadas
- No permitir que `Location.gazetteer.identifiers` tenga null en su lista de strings
- Corregir el nombre de la lista de código locationGazetteers.csv (era locationGazeteers.csv)
- Permitir que `Location.geometry` y` Location.gazetteer` sean null
- Agregar título y descripción a `Location.gazetteer`
- Agregar descripción a `Item.deliveryLocation`,` Item.deliveryAddress`
- Agregar la lista de código geometryType.csv para `Location.geometry.type`
- Enlista listas de códigos en extension.json
- Agregar pruebas y ordenar el código