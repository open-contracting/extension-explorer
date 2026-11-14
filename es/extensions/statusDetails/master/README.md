# Detalles de estado

En algunos casos, es importante preservar el nombre local del estado en el que se encuentra la licitación, adjudicación o contrato. Esta extensión agrega el campo `statusDetails` a los objetos de licitación, adjudicación y contrato, con el fin de proporcionar el nombre local del estado particular utilizado.

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

Un ejemplo de `contract.statusDetails` reflejando una orden judicial:

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

- Agregar un ejemplo de `contract.statusDetails` reflejando una orden judicial:

Esta extensión se discutió originalmente en <https://github.com/open-contracting/standard/issues/764>.
