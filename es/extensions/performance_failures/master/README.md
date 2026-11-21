# Fallas de desempeño

The [Framework for disclosure in Public Private Partnerships](https://thedocs.worldbank.org/en/doc/773541448296707678-0100022015/original/DisclosureinPPPsFramework.pdf) requires disclosure of instances of performance failures during the the life of a contract, along with the penalties or abatements defined, imposed and paid in relation to each category of performance failures.

## Ejemplo

The performance failures reported for one category during one period:

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "implementation": {
        "performanceFailures": [
          {
            "id": "1",
            "period": {
              "startDate": "2016-01-01T00:00:00Z",
              "endDate": "2016-12-31T23:59:59Z"
            },
            "category": "Daily average journey time exceeds 10 minutes",
            "events": 73,
            "penaltyContracted": "If the daily average journey time exceeds 10 minutes on more than 52 days per calendar year the project company will be subject to a penalty charge equal to (days - 52) * avgToll. Where days is the total number of days where the average journey time exceeded 10 minutes and avgToll is the average daily toll revenue to the project company over the calendar year in which the failures occurred.",
            "penaltyImposed": "A penalty of £3,360,000 was imposed",
            "penaltyPaid": true
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

- Agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `PerformanceFailure.period` no nulo (deshacer el cambio anterior), dado que se refiere al objeto `Period`.

### 2018-05-08

- Make `PerformanceFailure.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-01-29

- Hacer que `PerformanceFailure.period` pueda ser nulo.
