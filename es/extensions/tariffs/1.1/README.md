# Tarifas

## Introducción

Algunos contratos, en particular los contratos de Asociación Público Privada, incluyen acuerdos sobre las tarifas de usuario que se cobrarán por el uso de la infraestructura o los servicios a los que se refiere el contrato.

Por ejemplo, un proyecto de Asociación Pública Privada para construir un puente puede establecer los peajes para coches y otros vehículos para cruzar el mismo.

La extensión de tarifas permite establecer una lista estructurada de estos cargos.

También incluye entradas de lista de códigos adicionales para la lista de códigos documentType para:

- tariffs
- tariffMethod
- tariffReview
- tariffIllustration

## Modelado de tarifas

El modelo de tarifas se basa en la extensión de métricas, permitiendo una lista de elementos tarrif, cada uno con un identificador, título, período, valor, unidades y un conjunto arbitrario de dimensiones.

Por ejemplo, si el peaje para un puente de carretera varía según (a) el tipo de vehículo y (b) la hora del día; una implementación de la extensión de tarifas puede crear nuevos campos para `dimensions.vehicleType` y `dimensions.timeOfDay`, rellenando estos de acuerdo con las listas de códigos locales. En los casos de APP, estas dimensiones adicionales pueden reflejar las utilizadas en las secciones de demanda estimada y otras métricas.

## Ejemplo

El ejemplo siguiente muestra una tabla de tarifas muy sencilla, sin períodos ni unidades, pero con dos dimensiones. Las tarifas que se refieren a un determinado conjunto de fechas podrían tener un bloque `period`. Los que se refieren a una unidad particular (por ejemplo, toneladas) podrían tener esto indicado usando un bloque `unit`.

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "tariffs": [
        {
          "id": "1",
          "title": "Standard Toll",
          "dimensions": {
            "vehicleType": "Class 1",
            "registration": "No registration"
          },
          "value": {
            "amount": 0.0,
            "currency": "GBP"
          }
        },
        {
          "id": "2",
          "title": "Standard Toll",
          "dimensions": {
            "vehicleType": "Class 2",
            "registration": "No registration"
          },
          "value": {
            "amount": 2.0,
            "currency": "GBP"
          }
        },
        {
          "id": "3",
          "title": "Standard Toll",
          "dimensions": {
            "vehicleType": "Class 3",
            "registration": "No registration"
          },
          "value": {
            "amount": 6.0,
            "currency": "GBP"
          }
        },
        {
          "id": "4",
          "title": "Standard Toll",
          "dimensions": {
            "vehicleType": "Class 4",
            "registration": "No registration"
          },
          "value": {
            "amount": 8.0,
            "currency": "GBP"
          }
        }
      ]
    }
  ]
}
```

## Entradas de lista de códigos

Los siguientes tipos de documentos son introducidos por la extensión de tarifa

- tariffs - Para proporcionar tarifas y horarios de precios.
- tariffMethod - Para resumir el método por el cual se fijan las tarifas, y enlazar a la documentación detallada de los métodos para fijar tarifas. Esto puede incluir documentación escrita y hojas de cálculo con los modelos utilizados para calcular las tarifas.
- tariffReview - Para resumir las disposiciones para la revisión y regulación de las tarifas, y enlazar con la documentación detallada que explique cómo se regulan las tarifas. Esto es importante para poder explicarles a los usuarios por qué están pagando lo que están pagando, y el alcance de los cambios en las estructuras de pago.
- tariffIllustration - Para vincular a gráficos e informes sobre el cambio en el tiempo en los precios de las tarifas. Utilice el tipo de material de imagen relevante al vincular a gráficos PNG, JPEG o GIF para permitir que las aplicaciones muestren directamente este contenido.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2021-04-19

- Add Section column to the `+documentType.csv` codelist patch.

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `Tariff.unit` no nulo, como `Item.unit`.
- Hacer `Tariff.dimensions` no nulo (deshacer el cambio anterior).

### 2018-05-08

- Make `Tariff.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-05-01

- Hacer que `Tariff.dimensions` pueda ser nulo.
