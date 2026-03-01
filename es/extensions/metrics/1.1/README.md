# Extensión de Métricas

La extensión de métricas proporciona un bloque de construcción común para reportar información estructurada de rendimiento de los contratos.

Las métricas están estructuradas como un [cubo de datos OLAP](https://en.wikipedia.org/wiki/OLAP_cube) con cada instancia de `Metric` representando una sola **observación**, categorizada por un número de **dimensiones**.

La extensión de métricas se puede usar en:

- The `planning` stage for forecasts for a future contracting process (e.g. forecast demand levels)
- La etapa `tender` para objetivos del proceso de contrataciones (por ejemplo: niveles de disponibilidad objetivo o indicadores clave de rendimiento)
- Las etapas `awards` y `contracts` para los objetivos acordados con el proveedor adjudicado (por ejemplo, niveles de disponibilidad o KPI)
- The `implementation` stage for actual performance information (e.g. actual demand, physical progress, availability or KPIs)

Dónde se usa la extensión métricas para modelar objetivos para un proceso de contratación, el campo `description` puede usarse para indicar si el objetivo es un mínimo o un objetivo recomendando.

## Ejemplo

### Pronósticos

```json
{
  "planning": {
    "forecasts": [
      {
        "id": "annualDemand",
        "title": "Annual Demand",
        "description": "The annual demand",
        "observations": [
          {
            "id": "1",
            "period": {
              "startDate": "2015-01-01T00:00:00Z",
              "endDate": "2015-12-31T23:59:59Z"
            },
            "measure": 10000,
            "dimensions": {
              "vehicleType": "Car"
            }
          },
          {
            "id": "2",
            "period": {
              "startDate": "2015-01-01T00:00:00Z",
              "endDate": "2015-12-31T23:59:59Z"
            },
            "measure": 1000,
            "dimensions": {
              "vehicleType": "Trucks"
            },
            "notes": "Simple note"
          }
        ]
      }
    ]
  }
}
```

### Progreso físico

The physical progress of a highway's construction, by percent completion and kilometres constructed:

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "implementation": {
        "metrics": [
          {
            "id": "completionPercent",
            "title": "Construction progress (percent)",
            "description": "Percent completion of the construction of example highway",
            "observations": [
              {
                "id": "completionPercent-2016-Q1",
                "period": {
                  "startDate": "2016-03-31T23:59:59Z",
                  "endDate": "2016-03-31T23:59:59Z"
                },
                "measure": "25",
                "unit": {
                  "name": "percent",
                  "id": "P1",
                  "scheme": "UNCEFACT"
                }
              }
            ]
          },
          {
            "id": "completionKilometres",
            "title": "Construction progress (kilometres)",
            "description": "Progress of construction of example highway measured in kilometres",
            "observations": [
              {
                "id": "completionKilometres-2016-Q1",
                "period": {
                  "startDate": "2016-03-31T23:59:59Z",
                  "endDate": "2016-03-31T23:59:59Z"
                },
                "measure": "15",
                "unit": {
                  "name": "kilometre",
                  "id": "KMT",
                  "scheme": "UNCEFACT"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `Observation.unit` no nulo, como `Item.unit`.
- Hacer `Observation.dimensions` no nulo (deshacer el cambio anterior).

### 2018-05-08

- Make `Metric.id` and `Observation.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-05-01

- Agregar título y descripción a `Observation.period` y `Observation.value`.
- Hacer que `Observation.dimensions` pueda ser nulo.
