# Cuotas de participación

Esta extensión añade una matriz de los costos de participación al objeto de licitación, para revelar cualquier costo de participación en el proceso de contrataciones.

Algunas veces hay costos asociados con el acceso a documentos de licitaciones relacionados al proceso de contratación. Los licitadores potenciales quieren saber sobre esos costos. Los monitores de adquisiciones también deben de asegurar que los costos de participación estén dentro de los parámetros legales (generalmente se establecen con un valor fijo máximo, o como un porcentaje del valor total del contrato) o para monitorear como se usan las tarifas de participación.

## Guía

El campo `id` se va a requerir en las futuras versiones de la extensión.

In some cases, a fee is levied for official copies of procurement documents, with unofficial copies being freely available. Bidders might be required to prove that they have paid for official copies as part of their submission. In such cases, the fee should use the 'submission' code in the `type` field, rather than the 'document' code.

## Ejemplos

A contracting process where fees are applied to access bidding documents and to submit bids:

```json
{
  "tender": {
    "participationFees": [
      {
        "id": "1",
        "type": [
          "document"
        ],
        "value": {
          "currency": "GBP",
          "amount": 8.0
        },
        "description": "Fee payable for both soft and hard copies of documents.",
        "methodOfPayment": [
          "wireTransfer",
          "cheque"
        ],
        "payee": {
          "id": "ORG-0001",
          "name": "Highway Division"
        },
        "paymentAddress": {
          "locality": "Jawali",
          "region": "Himachal Pradesh",
          "countryName": "India"
        }
      },
      {
        "id": "2",
        "type": [
          "submission"
        ],
        "value": {
          "currency": "GBP",
          "amount": 10.0
        },
        "description": "Fee payable within e-procurement system.",
        "methodOfPayment": [
          "wireTransfer"
        ],
        "payee": {
          "id": "ORG-0001",
          "name": "Highway Division"
        }
      }
    ]
  }
}
```

A participation fee of 5% of the award value, payable by the winning bidder:

```json
{
  "tender": {
    "participationFees": [
      {
        "id": "1",
        "type": [
          "win"
        ],
        "relativeValue": {
          "proportion": 0.05,
          "monetaryValue": "award"
        },
        "description": "Fee payable on acceptance of award.",
        "methodOfPayment": [
          "wireTransfer",
          "cheque"
        ]
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### No entregado

- Make `ParticipationFee.id` required so that participation fees are merged by identifier
- Add fields:
  - `relativeValue`
  - `payee`
  - `paymentAddress`

### v1.1.5

- Añadir el campo  `id` al ejemplo en readme
- Corregir la descripción del campo `ParticipationFee.type`
- Combinar y conciliar descripciones de campos y códigos con esquemas y listas de códigos
- Quitar la indicación de campos "opcionales"
- Añadir la lista de código `methodOfPayment`  de la \[extensión paymentMethod\] (https://github.com/INAImexico/ocds_paymentMethod_extension/blob/master/codelists/paymentMethod.csv)
- Quitar la información sobre el tipo de las descripciones de los campos
- Revisar las palabras normativas y no-normativas

### v1.1.4

- Actualizar la propiedad `mergeStrategy` para la propiedad `wholeListMerge`
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que `ParticipationFee.type` tenga null en su conjunto de strings
- Permitir que `ParticipationFee.description` sea null
- Agregar el campo `ParticipationFee.id`
- Agregar descripción a `ParticipationFee`
- Agregar título y descripción a `ParticipationFee.value`
- Add a `participationFeeType.csv` codelist for `ParticipationFee.type`
- Agregar pruebas y ordenar el código
