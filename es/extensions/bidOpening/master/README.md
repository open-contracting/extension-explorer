# Apertura de ofertas

Adds an object to describe the date, time, place and other details of the public bid opening.

This extension must be used with the [Location](https://extensions.open-contracting.org/en/extensions/location/master/) extension.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-132 (Public Opening Date), BT-133 (Public Opening Place), BT-134 (Public Opening Description)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

### Tender

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

### Lotes

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
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
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-06-07

- Clarify that the extension is for bid openings that are public events.

### 2023-02-13

- Add `Lot.bidOpening` field.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión fue originalmente discutida como parte del  [OCDS para el perfil de EU](https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_bidOpening_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/749>.
