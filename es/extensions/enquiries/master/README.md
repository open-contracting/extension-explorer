# Consultas

La extensión sobre consultas puede usarse para registrar las preguntas planteadas durante un proceso de contratación y las respuestas proporcionadas.

## Estructura

La extensión agrega una lista de `enquiries` a la licitación, la cual consiste en uno o más objetos de consultas, cada uno con campos para una pregunta y una respuesta.

Ejemplo:

```json
{
  "tender": {
    "enquiries": [
      {
        "id": "Q1",
        "date": "2017-01-22T14:55:00Z",
        "author": {
          "name": "Open Data Services Co-op",
          "id": "GB-COH-09506232"
        },
        "title": "Variations of timeline accepted?",
        "description": "The tender specifies delivery of Item 1 by end of March 2017. Will alternative proposals for the timeline be considered?",
        "dateAnswered": "2017-02-05T09:00:00Z",
        "answer": "There is a hard deadline of 15th April 2017. All proposals must be for delivery of Item 1 by this date.",
        "relatedItem": "1",
        "threadID": "1"
      }
    ]
  }
}
```

Los documentos de soporte con aclaraciones o un documento completo que contenga respuestas a preguntas pueden incluirse en la matriz `tender/documents` con un `documentType` de 'clarifications'.

Si las respuestas a una pregunta sólo están disponibles en los documentos adjuntos, se puede ingresar un valor `answer` como "Consultar la sección N de (nombre del documento) en la sección de documentos" para permitir que los usuarios identifiquen que se ha dado respuesta a esta pregunta.

Cuando un sistema permite un formato de discusión, en el que cada respuesta puede ir seguida de otra pregunta de aclaración, el campo `threadID` puede utilizarse para enlazar varias entradas en la lista `enquiries`.

## Guía

Las implementaciones pueden variar en la cantidad de información de consultas que proporcionan y cuándo se proporciona.

Algunos editores pueden omitir la identidad del autor de la pregunta para proteger la confidencialidad de los solicitantes, o pueden anonimizar esta información (por ejemplo, simplemente poniendo el nombre del autor como "Organización 1" u "Organización 2" para que sea posible ver preguntas de la misma organización , Pero no conocer la identidad de esa organización.)

Los campos `relatedItem` y `relatedLot` están disponibles para su uso cuando se pueden hacer preguntas en relación con un lote o artículo específico.

Cuando sea posible, el enfoque recomendado es:

- Haga una entrega con una etiqueta `tenderUpdate` para cada nueva pregunta o lote de preguntas recibidas, proporcionando una matriz de preguntas con cada una de las preguntas en;
- Haga una entrega con una etiqueta de `tenderUpdate` cuando se proporcionen las respuestas a las preguntas, actualizando la matriz de consultas anteriores para que cada entrada contenga una pregunta y una respuesta;

Este enfoque permitirá a las aplicaciones de terceros vigilar las entregas que proporcionen respuestas a las preguntas y apoyará en el monitoreo de adquisiciones en la revisión de la forma en que se responden las preguntas.

Recomendamos que los publicadores proporcionen respuestas como texto sin formato o con un marcado HTML mínimo (párrafos y saltos de línea) y que las aplicaciones que consumen analicen el texto apropiadamente para darle formato para legibilidad (por ejemplo, reemplazar saltos de línea con saltos de párrafo en HTML).

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### No entregado

- Remove the `+partyRole.csv` codelist patch, whose codes already exist in OCDS 1.1
- Make `Enquiry.id` required so that enquiries are merged by identifier
- Make `Tender.enquiries` non-nullable

### v1.1.5

- Revisar las palabras normativas y no-normativas

### v1.1.4

- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- Usar `OrganizationReference` en lugar de` Organization` para `Enquiry.author`
- Corrige el nombre de la lista de código + partyRole.csv (era + partyRoles.csv)
- Permitir que `Enquiry.date` sea null
- Enlista listas de códigos en extension.json
- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
