# Finalización de los contratos

El Estándar de Datos de Contrataciones Abiertas se puede usar para dar información sobre todas las etapas del proceso de contrataciones, desde la planeación hasta la implementación.

Esta extensión introduce cuatro campos que pueden usarse al final de un proceso de contratación para dar detalles sobre la fecha final y valor del contrato, también se pueden utilizar cuando hay variaciones para dar una justificación de las mismas.

## Utilizar campos OCDS existentes dentro de un registro de contratos

OCDS contains many existing fields that can be used as part of a Contracts Register. These are documented in the [schema reference](https://standard.open-contracting.org/latest/en/schema/reference/). This extension does not modify any of these fields. However, the following list is provided for convenience of those considering the design of a contracts register:

- **Los detalles del proveedor** deben registrarse dentro de la sección  `awards`, enlazada a través de` contract.awardID` (incluso si solo está publicando información en la etapa del contrato, puede proporcionar información en las secciones de licitación y adjudicación).
- **Documentos del contrato** se puede enlazar en `contracts.documents`.
- **Reportes de desempeño** se pueden proporcionar en `contracts.implementation.documents`.
- **Detalles de los pagos** se pueden proporcionar en `contracts.implementation.transactions`.
- **Los detalles del progreso** se pueden proporcionar usando `contracts.implementation.milestones`.
- **Amendments** can be described using the `contracts.amendments` array, and with past values provided using the OCDS releases model [as described here](https://standard.open-contracting.org/latest/en/implementation/amendments/).

### Utilizar hitos para mostrar la finalización de un contrato

Los hitos pueden tener un `status` de 'scheduled', 'met', 'notMet' o 'partiallyMet'. Al dar al menos un hito por contrato, y asegurar que `milestone/status` se actualice cuando `implementation/endDate` se puede indicar que un contrato terminó con la entrega exitosa de todos los hitos y entregables.

## Ejemplo

Observe la diferencia entre `period` y `value` del contrato (según lo acordado en el contrato, o en el contrato modificado o enmendado), y el `finalValue` y  `endDate`,  de la implementación, junto con la explicación de esta diferencia.

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Contract to build new cycle lanes in the centre of town.",
      "period": {
        "startDate": "2010-07-01T00:00:00Z",
        "endDate": "2012-01-01T23:59:00Z",
        "maxExtentDate": "2012-01-31T23:59:00Z"
      },
      "value": {
        "amount": 11500000,
        "currency": "GBP"
      },
      "implementation": {
        "endDate": "2012-02-01T00:00:00Z",
        "endDateDetails": "Project was completed one day beyond the extended deadline.",
        "finalValue": {
          "amount": 11800000,
          "currency": "GBP"
        },
        "finalValueDetails": "The final payment to the supplier included a compensation payment triggered by the local authority failure to provide work permits on schedule."
      }
    }
  ]
}
```

El directorio de [ejemplos](https://github.com/open-contracting-extensions/ocds_contract_completion_extension/tree/master/examples) contiene un completo ejemplo práctico con:

- Un lanzamiento que da detalles sobre un contrato;
- Un lanzamiento que incluye una enmienda al contrato para incrementar el valor total, así como el valor inicial de las transacciones;
- Un lanzamiento que contiene una fecha final confirmada, el valor final y la explicación de variación en ellas

Esto también se proporciona como registro OCDS y como archivo Excel.

En el archivo Excel, es posible ver tres entregas que describen los tres momentos clave del mismo proceso de contratación.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Revisar las palabras normativas y no-normativas

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente en  <https://github.com/open-contracting/standard/issues/703>.
