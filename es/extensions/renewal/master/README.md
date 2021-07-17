# Renewal

Adds fields to the Tender and Lot objects to describe the options for the renewal of contracts.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-57 (Renewal Description)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Guía

If the number of times a contract can be renewed is an exact number and not a range, set `minimumRenewals` and `maximumRenewals` to the same number.

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

### 2021-01-19

- Add the `hasRenewal` and `renewal` fields to the Tender object.

### 2020-10-06

- Add the `minimumRenewals`, `maximumRenewals` and `period` fields to the `Renewal` object.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) in [issue 22](https://github.com/open-contracting-extensions/european-union/issues/22) and in [pull requests](https://github.com/open-contracting-extensions/ocds_renewal_extension/pulls?q=is%3Apr+is%3Aclosed).
