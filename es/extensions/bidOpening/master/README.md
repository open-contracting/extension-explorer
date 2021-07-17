# Apertura de ofertas

Agregar un objeto para describir la fecha, hora, lugar y otros detalles de la apertura de ofertas.

## Contexto legal

En la unión Europea, los campos de esta extensión corresponden a \[eForms BT-132, BT-133, BT-134\] (https://github.com/eForms/eForms). Ver [OCDS para la unión Europea](http://standard.open-contracting.org/profiles/eu/master/en/) para lo correspondiente a las Licitaciones Electrónicas Diarias (LED).

## Ejemplo

```json
{
  "tender": {
    "bidOpening": {
      "date": "2019-10-16T15:00:00+01:00",
      "address": {
        "streetAddress": "Town Hall, St Aldate's",
        "region": "Oxfordshire",
        "locality": "Oxford",
        "postalCode": "OX1 1BX",
        "countryName": "United Kingdom"
      },
      "location": {
        "description": "Central Oxford",
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
        "uri": "http://www.geonames.org/2640729/oxford.html"
      },
      "description": "We recommend that people who wish to attend the opening register on this page: https://wwww.example.org/register"
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión fue originalmente discutida como parte del  [OCDS para el perfil de EU](https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_bidOpening_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/749>.
