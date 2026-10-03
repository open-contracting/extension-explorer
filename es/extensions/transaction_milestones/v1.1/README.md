# Transacciones  - Extensión relatedMilestone

## Antecedentes

En OCDS  las `transactions` son propiedad del objeto ` implementation`.

Algunos contratos vinculan los pagos con un contrato a hitos específicos para la entrega del contrato.

## Campos de extensión

Esta extensión agrega una propiedad `relatedImplementationMilestone` al objeto `transaction`.

La propiedad `relatedImplementationMilestone` es un objeto de ` milestoneReference`.

El objeto `milestoneReference` es introducido por la [extensión de métricas](https://github.com/open-contracting/ocds_metrics_extension).

## Ejemplo

```json
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
```
