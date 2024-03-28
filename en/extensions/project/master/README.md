# Project

This extension adds a `project` object to the `planning` object.

In OCDS, project information is nested under the [`planning.budget`](https://standard.open-contracting.org/latest/en/schema/reference/#budget) object. However, in some cases, budget management systems and project management systems are separate, and it might be important to separately specify:

- The amount reserved in the budget for a specific contracting process
- The project the contract relates to, and the total value of that project
- Sector classifications
- Additional classifications
- Project locations, with options for gazetteer or point locations

This is particularly important in cases of Public-Private Partnerships and large infrastructure projects, where users might want to track all the contracting processes related to the large-scale project, and to understand the individual contracts in the context of their contracting process and overall project values.

This extension must be used with the [Location](https://extensions.open-contracting.org/en/extensions/location/master/) extension.

## Examples

### Infrastructure project

```json
{
  "planning": {
    "project": {
      "id": "oc4ids-gx3fo2-000002",
      "title": "Construcción de red de drenaje sanitario en diversas calles de la colonia Ruperto Martínez",
      "description": "Construcción de red de drenaje sanitario consistente en excavación de 756 metros cúbicos para alojar la red de drenaje sanitario, suministro y colocación de 712 metros de tubería PVC tipo serie 20 pared solida, construcción de 15 pozos de visita y 30 descargas domiciliarias sencillas en la colonia Ruperto Martinez, en el municipio de Higueras, N.L.",
      "totalValue": {
        "amount": 4010130.1,
        "currency": "MXN"
      },
      "locations": [
        {
          "description": "Col. Ruperto Martínez, Higueras, N.L.",
          "geometry": {
            "type": "Point",
            "coordinates": [
              25.953400063796533,
              -100.01606973176307
            ]
          }
        }
      ]
    }
  }
}
```

### Public-Private Partnership project

```json
{
  "planning": {
    "project": {
      "title": "Example PPP",
      "description": "The Example PPP project will guarantee the installation of a wholesale shared network that allows the provision of telecommunications services by current and future operators.",
      "id": "example_ppp",
      "uri": "http://communications.gov.example/projects/example_ppp",
      "totalValue": {
        "amount": 600000000,
        "currency": "USD"
      },
      "sector": {
        "scheme": "COFOG",
        "description": "Road transportation",
        "id": "04.5.1"
      },
      "locations": [
        {
          "description": "Local Authority Area: Halton Borough Council",
          "gazetteer": {
            "scheme": "GEONAMES",
            "identifiers": [
              "2647601"
            ]
          }
        }
      ]
    }
  }
}
```

## Changelog

### 2021-04-15

- Add infrastructure project example

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-04-16

- Remove guidance related to the `planning.budget` object. See [#701](https://github.com/open-contracting/standard/issues/701).

### 2018-05-03

- Add additional guidance on the use of OCDS fields in the context of this extension

### 2017-12-29

- Remove the repetition of OCDS fields in this extension

### 2017-07-08

- Add multilingual support for `Project.title` fields
- Remove multilingual support for non-existent `Project.source` and `Project.project` fields
- Restore `Budget.project` and `Budget.projectID` fields
- Remove obsolete `mergeStrategy` properties

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
