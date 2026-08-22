# Cuotas de participación

## Antecedentes

Hay una serie de casos en los que puede haber costos para acceder a los documentos o participar en un proceso de licitación.

Los licitadores potenciales desearán estar enterados de los costos que un proceso puede implicar.

Los monitores de adquisiciones tal vez deseen asegurarse de que los costos de participación estén dentro de los parámetros legales (a menudo fijados como un máximo fijo, o un porcentaje del valor total del contrato), o para controlar cómo se usan las cuotas de participación.

## Campos de extensión

Esta extensión agrega un campo `participationFees` a la sección ` tender` del OCDS e introduce un nuevo bloque `participationFee`.

El campo `participationFees` es una lista de bloques ` participationFee`.

El bloque `participationFee` consta de tres campos:

- `type` - un valor de la lista de códigos `participationFeeType`, que describe el tipo de costo
- `value` - el importe y la moneda del costo
- `description` - un campo opcional con más información sobre los requisitos del costo de participación. Por ejemplo, a veces un costo de un documento sólo es aplicable a la copia impresa de los documentos.
- `methodOfPayment` - un campo opcional que proporciona información sobre los métodos de pago aceptados para la documentación. Actualmente se trata de una serie de cadenas, pero se podría introducir una lista de códigos abierta en el futuro.

## Listas de códigos de extensión

Esta extensión agrega una lista de códigos **cerrada** `participationFeeType` con los siguientes códigos:

- document - una cuota a pagar por el acceso a los documentos de licitación
- deposit - una cuota reembolsable a pagar por la presentación de ofertas
- submission - una cuota no reembolsable a pagar por la presentación de ofertas
- win - una cuota a pagar por el ganador

## Ejemplo

El siguiente fragmento de JSON modela un proceso de contratación donde las tarifas son aplicables tanto para el acceso a documentos como para la presentación de ofertas:

```json
{
  "tender": {
    "participationFees": [
      {
        "type": "document",
        "value": {
          "currency": "GBP",
          "amount": 8.00
        },
        "description": "Fee payable for both soft and hard copies of documents.",
          "methodOfPayment":["electronic","cheque"]
      },
      {
        "type": ["submission"],
        "value": {
          "currency": "GBP",
          "amount": 10.00
        },
        "description": "Fee payable within e-procurement system.",
        "methodOfPayment":["electronic"]
      }
    ]
  }
}
```

## Notas de uso

En algunos casos, se puede cobrar una cuota por las "copias oficiales" de los documentos de adquisición (aunque también se pueden obtener copias en línea de forma gratuita) y los licitadores deben probar que han pagado una copia oficial de los documentos como parte de su presentación.

En este caso, la cuota debe ser modelada como un cargo de **oferta**, ya que la presentación sólo es posible cuando se ha pagado la cuota de acceso al documento.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

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
