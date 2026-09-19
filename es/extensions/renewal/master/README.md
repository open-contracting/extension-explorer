# Renovación

Adds fields to describe the options for the renewal of contracts.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-57 (Renewal Description)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Guía

Si el número de veces que se puede renovar un contrato es un número exacto y no un rango, establecer `minimumRenewals` y `maximumRenewals` al mismo número.

## Ejemplo

```json
{
  "tender": {
    "lots": [
      {
        "id": "lot-1",
        "title": "Architectural services",
        "description": "For architectural services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 200000
        },
        "contractPeriod": {
          "startDate": "2020-10-10T00:00:00Z",
          "endDate": "2021-11-10T00:00:00Z"
        },
        "hasRenewal": false
      },
      {
        "id": "lot-2",
        "title": "Civil engineering services",
        "description": "For civil engineering services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 400000
        },
        "contractPeriod": {
          "startDate": "2020-12-10T00:00:00Z",
          "endDate": "2021-12-10T00:00:00Z"
        },
        "hasRenewal": true,
        "renewal": {
          "description": "The contracting authority reserves the right to extend the term for a period or periods of up to 1 year with a maximum of 2 such extensions on the same terms and conditions, subject to the contracting authority’s obligations at law.",
          "maximumRenewals": 2,
          "period": {
            "durationInDays": 365
          }
        }
      },
      {
        "id": "lot-3",
        "title": "Structural engineering",
        "description": "For structural engineering consultancy delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 600000
        },
        "contractPeriod": {
          "startDate": "2021-02-10T00:00:00Z",
          "endDate": "2022-02-10T00:00:00Z"
        },
        "hasRenewal": true,
        "renewal": {
          "description": "Contracts are due to be renewed one time at the end of the initial term.",
          "minimumRenewals": 3,
          "maximumRenewals": 3,
          "period": {
            "startDate": "2021-02-10T00:00:00Z",
            "endDate": "2024-02-10T00:00:00Z"
          }
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-05-02

- Add fields:
  - `Award.hasRenewal`
  - `Award.renewal`
  - `Contract.hasRenewal`
  - `Contract.renewal`
- Clarify description of `Tender.hasRenewal` and `Lot.hasRenewal`.

### 2021-01-19

- Add fields:
  - `Tender.hasRenewal`
  - `Tender.renewal`

### 2020-10-06

- Add fields:
  - `Renewal.minimumRenewals`
  - `Renewal.maximumRenewals`
  - `Renewal.period`

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) en [issue 22](https://github.com/open-contracting-extensions/european-union/issues/22) y en [pull requests](https://github.com/open-contracting-extensions/ocds_renewal_extension/pulls?q=is%3Apr+is%3Aclosed).
