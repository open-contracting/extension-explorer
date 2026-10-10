# Hitos relacionados con transacción

Esta extensión agrega un campo `relatedImplementationMilestone` a los objetos de la transacción, para que los pagos de un contrato puedan vincularse con un hito de implementación.

This extension must be used with the [Metrics](https://extensions.open-contracting.org/en/extensions/metrics/1.1/) extension.

## Ejemplo

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "implementation": {
        "milestones": [
          {
            "id": "1234",
            "title": "Example milestone",
            "dueDate": "2017-01-01T17:00:00Z",
            "dateMet": "2016-12-28T17:00:00Z",
            "status": "met",
            "dateModified": "2016-12-28T17:00:00Z"
          }
        ],
        "transactions": [
          {
            "id": "ABC-123",
            "source": "http://www.example.com/budget/FY17",
            "date": "2017-01-05T13:00:00Z",
            "value": {
              "amount": 150000,
              "currency": "GBP"
            },
            "payer": {
              "id": "GB-GOV-00000000",
              "name": "Example ministry"
            },
            "payee": {
              "id": "GB-COH-99999999",
              "name": "Example consortium"
            },
            "relatedImplementationMilestone": {
              "id": "1234",
              "title": "Example milestone"
            }
          }
        ]
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
