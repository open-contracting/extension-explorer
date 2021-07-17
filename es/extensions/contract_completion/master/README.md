# Finalización de Contratos

El Estándar de Contrataciones Abiertas se puede usar para dar información sobre todas las etapas del proceso de contrataciones, desde la planeación hasta la implementación.

Esta extensión introduce cuatro campos que pueden usarse al final de un proceso de contratación para dar detalles sobre la fecha final y valor del contrato, también se pueden utilizar cuando hay variaciones para dar una justificación de las mismas.

## Campos Adicionales

Los campos que se introducen con esta extensión son:

- **`implementation.endDate`** - La fecha real en la que finalizó la implementación del contrato. Cuando `implementation.endDate` difiera de la anticipada fecha `contracts.period.endDate`, se debe proporcionar una explicación de la variación en `implementation.endDateDetails`.

- **`implementation.endDateDetails`** - Detalles relacionados con endDate. Esto puede ser una justificación para que la fecha de finalización del contrato sea diferente a la del contrato original.

- **`implementation.finalValue`** - El valor total real de todos los pagos de un contrato completado. Si se utilizan `implementation.transactions` para este contrato, este campo debe ser igual a la suma de los campos `transaction.value.amount`. Cuando `finalValue.amount` difiera de `contracts.value.amount`, se debe proporcionar una explicación de la variación en `finalValueDetails`.

- **`implementation.finalValueDetails`** - Detalles relacionados al valor final. Esto puede ser una justificación de que el valor del contrato completado sea diferente al del contrato original.

## Utilizando campos de OCDS existentes en un Registro de Contratos

El OCDS tiene muchos campos que pueden usarse como parte de un Registro de Contratos. Estos están documentados en el  [esquema](http://standard.opencontracting.org/latest/es/schema/reference/). Esta extensión no modifica ninguno de estos campos. De cualquier manera, la siguiente lista se da para la conveniencia de las personas que están considerado el diseño de un registro de contratos.

- **Los detalles del proveedor** deben registrarse dentro de la sección `awards`, enlazada a través de` contract.awardID` (incluso si solo está publicando información en la etapa del contrato, puede proporcionar información en las secciones de licitación y adjudicación)
- **Los documentos del contrato** se pueden vincular en `contracts.documents`
- **Los informes de rendimiento** se pueden proporcionar en `contracts.implementation.documents`
- **Los detalles de los pagos** se pueden proporcionar en `contratos.implementación.transacciones`
- **Los detalles del progreso** se pueden proporcionar usando `contracts.implementation.milestones`.
- **Las enmiendas** se pueden describir usando la matriz `contract.amendments` y con los valores pasados ​​proporcionados usando el [modelo de versiones OCDS como se describe aquí](http://standard.open-contracting.org/latest/es/implementation/amendments/)

### Utilizar hitos para mostrar la finalización de un contrato

Los hitos pueden tener un `status` de 'scheduled', 'met', 'notMet' o 'partiallyMet'. Al dar al menos un hito por contrato, y asegurar que `milestone/status` se actualice cuando `implementation/endDate` se puede indicar que un contrato terminó con la entrega exitosa de todos los hitos y entregables.

## Serializaciones JSON y CSV

En algunos casos, puede ser posible diseñar un registro de contratos simple utilizando el  [flat CSV serialization de OCDS](http://standard.open-contracting.org/latest/en/implementation/serialization/#csv).

## Ejemplo

El siguiente extracto ilustra estas propiedades en uso dentro del bloque `contracts.implementation`. Note la diferencia entre `period` y `value` del contrato (como en se acordó en el contrato o en la versión corregida del contrato), y `finalValue` y `endDate` de la implementación, junto con la explicación proveída de esta variación.

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

La carpeta ejemplo contiene un ejemplo de trabajo completo:

- Un lanzamiento que da detalles sobre un contrato;
- Un lanzamiento que incluye una enmienda al contrato para incrementar el valor total, así como el valor inicial de las transacciones;
- Un lanzamiento que contiene una fecha final confirmada, el valor final y la explicación de variación en ellas

Esto también se suministra en forma de registro y con una serialización plana simplificada. El registro se puede ver con \[OCDS Show\] (https://open-contracting.github.io/ocds-show/) para demostrar cómo el modelo de registros y entregas de OCDS capturan los cambios en el tiempo.

En la serialización de base de datos es posible ver tres tipos de lanzamientos que describen tres momentos clave en el mismo proceso de contratación

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Revisar las palabras normativas y no-normativas

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente en  <https://github.com/open-contracting/standard/issues/703>.
