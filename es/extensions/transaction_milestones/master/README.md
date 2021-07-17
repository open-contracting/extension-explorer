# Transaction related milestones

## Antecedentes

En OCDS  las `transactions` son propiedad del objeto `implementation`.

Algunos contratos vinculan los pagos con un contrato a hitos específicos para la entrega del contrato.

## Campos de extensión

This extension adds a `relatedImplementationMilestone` property to the `Transaction` object.

La propiedad `relatedImplementationMilestone` es un objeto de `MilestoneReference`.

The `MilestoneReference` object is introduced by the [metrics extension](http://extensions.open-contracting.org/en/extensions/metrics/master/).

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
