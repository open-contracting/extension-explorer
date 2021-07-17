# Status Details

In some cases, it is important to preserve the local name of the status in which the tender, award or contract are. This extension adds the field `statusDetails` to the tender, award and contract objecs, in order to provide the local name of the particular status used.

## Ejemplos

```json
{
  "tender": {
    "id": "tender-1",
    "status": "complete",
    "statusDetails": "Adjudicado"
  },
  "awards": [
    {
      "id": "award-1",
      "status": "active",
      "statusDetails": "Adjudicado"
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "awardID": "award-1",
      "status": "active",
      "statusDetails": "Adjudicado"
    }
  ]
}
```

An example of `contract.statusDetails` reflecting a court order:

```json
{
  "tender": {
    "id": "tender-1",
    "status": "complete"
  },
  "awards": [
    {
      "id": "award-1",
      "status": "active"
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "awardID": "award-1",
      "status": "active",
      "statusDetails": "Suspended as a result of a court order."
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2021-01-11

- Add example of `contract.statusDetails` reflecting a court order.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/764>.
