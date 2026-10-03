# Cuotas de participación

Esta extensión añade una matriz de los costos de participación al objeto de licitación, para revelar cualquier costo de participación en el proceso de contrataciones.

El campo `id` se va a requerir en las futuras versiones de la extensión.

## Contexto

Algunas veces hay costos asociados con el acceso a documentos de licitaciones relacionados al proceso de contratación. Los licitadores potenciales quieren saber sobre esos costos. Los monitores de adquisiciones también deben de asegurar que los costos de participación estén dentro de los parámetros legales (generalmente se establecen con un valor fijo máximo, o como un porcentaje del valor total del contrato) o para monitorear como se usan las tarifas de participación.

## Ejemplo

El siguiente fragmento de JSON modela un proceso de contratación donde las tarifas son aplicables  al acceso a documentos y para la presentación de ofertas:

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
        ]
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
        ]
      }
    ]
  }
}
```

## Notas de uso

En algunos casos, se puede cobrar una cuota por las "copias oficiales" de los documentos de adquisición (aunque también se pueden obtener copias en línea de forma gratuita) y los licitadores deben probar que han pagado una copia oficial de los documentos como parte de su presentación. En ese caso, las tarifas deben de modelarse como una tarifa de **envío de documentos**, ya que solo se puede enviar los documentos una vez que la tarifa de acceso a los documentos se ha pagado.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

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
- Agregar la lista de códigos de participaciónFeeType.csv para `ParticipationFee.type`
- Agregar pruebas y ordenar el código
