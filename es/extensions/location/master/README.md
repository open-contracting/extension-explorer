# Datos de ubicación

This extension adds address and location fields to tenders and items, to communicate the location of proposed or executed contract delivery.

La columna `Category`  en la lista de código  `locationGazetteers.csv` indica si el diccionario geográfico tiene identificadores para todo el mundo ('Universal') o solo un subconjunto ('National' o 'Sub-National').

## Ejemplo

A continuación se muestra un ejemplo de un elemento geolocalizado en la sección `tender`:

```json
{
  "tender": {
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
        "deliveryLocations": [
          {
            "geometry": {
              "type": "Point",
              "coordinates": [
                51.751944,
                -1.257778
              ]
            },
            "gazetteer": {
              "scheme": "GEONAMES",
              "identifiers": [
                "2640729"
              ]
            },
            "description": "Central Oxford",
            "uri": "http://www.geonames.org/2640729/oxford.html"
          }
        ],
        "deliveryAddresses": [
          {
            "postalCode": "OX1 1BX",
            "countryName": "United Kingdom",
            "streetAddress": "Town Hall, St Aldate's",
            "region": "Oxfordshire",
            "locality": "Oxford",
            "description": "The old town hall"
          }
        ],
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
}
```

Si la adquisición relacionada con la reconstrucción de una carretera, entonces el elemento también podría especificar geometrías más complejas, tales como:

```json
{
  "tender": {
    "items": [
      {
        "id": "item1",
        "deliveryLocations": [
          {
            "geometry": {
              "type": "LineString",
              "coordinates": [
                [
                  102,
                  0
                ],
                [
                  103,
                  1
                ],
                [
                  104,
                  0
                ],
                [
                  105,
                  1
                ]
              ]
            },
            "gazetteer": {
              "scheme": "OSMW",
              "identifiers": [
                "27895985"
              ]
            },
            "description": "St Aldate's",
            "uri": "http://www.geonames.org/2640729/oxford.html"
          }
        ]
      }
    ]
  }
}
```

Puede tomar el contenido del objeto geométrico, excluyendo la palabra clave `geometry`, y conectarlo a cualquier herramienta de GeoJSON para ver la forma en que se describe.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### No entregado

- Add fields:
  - `Tender.deliveryAddresses`
  - `Tender.deliveryLocations`
  - `Address.description`
- Deprecate the `Item.deliveryAddress` field in favor of the new `Item.deliveryAddresses` field, to support items with multiple delivery addresses
- Deprecate the `Item.deliveryLocation` field in favor of the new `Item.deliveryLocations` field, to support items with multiple delivery locations
- Añadir "format": "uri" a `Location.uri`
- Update field descriptions to allow location objects to be used in other contexts than deliveries

### v1.1.5

- Quitar la información sobre el tipo de las descripciones de los campos
- Revisar las palabras normativas y no-normativas

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
- Add a `geometryType.csv` codelist for `Location.geometry.type`
- Enlista listas de códigos en extension.json
- Agregar pruebas y ordenar el código
