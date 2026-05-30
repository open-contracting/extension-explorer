# Lotes

A lot is a grouping of items within a contracting process that can be bid on or awarded together. This extension adds the concept of a lot to OCDS.

## Guía

If a contracting process is divided into lots, then you should add each lot to the `tender.lots` array.

If a contracting process is not divided into lots, then you should nonetheless add a single, virtual lot. If a data element can be mapped to either a `tender` field or a `tender.lots` field, you should map it to the `tender.lots` field. In this way, information is accessible at the same location for all contracting processes, regardless of whether the process is actually divided into lots.

## Modelling

La extensión de lotes mantiene la estructura general de una entrega de OCDS, con artículos, documentos e hitos incluidos inmediatamente dentro de los elementos `tender`, `award` y `contract`, pero introduce una lista de lotes en la sección `tender`, y la capacidad de hacer referencia cruzada a un `relatedLot` específico para cada elemento, y una lista de `relatedLots` para documentos, hitos y adjudicaciones

La sección opcional `lotDetails` y `lotGroups` permite que se expresen condiciones más complejas en torno a la adjudicación de lotes, como el valor máximo de un grupo de lotes.

Esto significa que los sistemas que no conocen la 'existencia de lotes' de igual forma pueden entender el valor global de la contratación que se esta llevando a cabo, los acontecimientos clave y las relaciones entre los compradores y los proveedores. Al mismo tiempo, los sistemas que sí conocen de la 'existencia de lotes' pueden hacer uso de la información referenciada para presentar una visión centrada-en-lotes en la información a los usuarios, o para analizar la contratación lote por lote.

## Lote Relacionado

El campo `relatedLot` (singular) está disponible para:

- items

Se puede proporcionar una lista de `relatedLots` (plural) para cada uno de los siguientes:

- documents
- milestones
- awards
- relatedProcesses

En otras extensiones, los siguientes objetos también pueden declararse lotes relacionados:

- bids submitted by tenderers, in the [bid extension](https://github.com/open-contracting-extensions/ocds_bid_extension)
- las fuentes de finanzas  (`Finance`), in the [extensión finanzas](https://github.com/open-contracting-extensions/ocds_finance_extension)

Cuando se usan lotes, **todos** los elementos deben tener un campo `relatedLot`.

Los documentos e hitos pueden tener  una propiedad `relatedLots`. Aquellos sin esta propiedad deben interpretarse como aplicables a la licitación en su conjunto.

Los artículos dentro de una adjudicación deben tener un campo `relatedLot`. Los publicadores pueden también hacer referencia a todos los lotes a los que se relaciona una adjudicación utilizando  `relatedLots`.

## ¿Cómo establecer `tender.status`  si los estados de los lotes son diferentes?

`tender.status` y `tender.lots.status` utilizan la lista de códigos cerada tenderStatus.csv. Esta lista de códigos avanza desde los estados de planeación ('planning', 'planned'), a estado activo 'active', y luego los estados de los resultados completo, cancelado, no exitoso ('complete', 'cancelled', 'unsuccessful').

- Si cualquiera de los estados del lote esta 'activo', entonces  `tender.status` debe ser 'activo', para indicar que algunos lotes están esperando resultados.
- Si todos los estados del lote se encuentran en estado de resultados, entonces `tender.status` describe el resultado agregado:
  - Si al menos uno de los estados del lote esta 'completo', entonces  `tender.status` debe mostrar 'completo', para indicar que hay al menos una adjudicación.
  - Si no es así,  y al menos uno de los estados del lote es 'fallido', el `tender.status` debe ser 'fallido' para indicar que el procedimiento se completo pero no exitosamente.
  - De otra manera, si todos los estados del lote están 'cancelados', entonces  `tender.status` deben de estar 'cancelados', para indicar que el procedimiento se descontinuo en su totalidad.

## Ejemplos

Se emite una licitación para consultoría en el desarrollo de un nuevo edificio público. Esto podría incluir elementos para:

- Diseño arquitectónico
- Servicios de asesoramiento arquitectónico
- Consultoría de ingeniería civil
- Consultoría en ingeniería estructural

Aunque forma parte de la misma oferta, el comprador está dispuesto a adjudicar estos diferentes artículos a diferentes empresas, y así divide la oferta en tres lotes.

```json
{
  "tender": {
    "items": [
      {
        "id": "0001",
        "description": "Architectural advice",
        "classification": {
          "scheme": "CPV",
          "id": "71210000",
          "description": "Advisory architectural services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0002",
        "description": "Architectural design",
        "classification": {
          "scheme": "CPV",
          "id": "71220000",
          "description": "Architectural design services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0003",
        "description": "Civil engineering consultant",
        "classification": {
          "scheme": "CPV",
          "id": "71311000",
          "description": "Civil engineering consultancy services"
        },
        "relatedLot": "lot-2"
      },
      {
        "id": "0004",
        "description": "Structural engineering services",
        "classification": {
          "scheme": "CPV",
          "id": "71312000",
          "description": "Structural engineering consultancy services"
        },
        "relatedLot": "lot-3"
      }
    ],
    "value": {
      "amount": 1200000,
      "currency": "GBP"
    },
    "lots": [
      {
        "id": "lot-1",
        "identifiers": [
          {
            "id": "PROC/2020/0024-ABC-FGHI-1",
            "scheme": "internal"
          }
        ],
        "title": "Architectural services",
        "description": "For architectural services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 200000
        },
        "tenderPeriod": {
          "endDate": "2020-07-30T23:59:59+01:00"
        },
        "submissionMethodDetails": "https://www.acme.com/tender-submission/. All missing tenderer-related documents can be submitted later. Economic operators who ...",
        "submissionTerms": {
          "electronicSubmissionPolicy": "required"
        },
        "enquiryPeriod": {
          "endDate": "2020-07-15T23:59:59+01:00"
        },
        "contractPeriod": {
          "startDate": "2020-10-10T00:00:00Z",
          "endDate": "2021-11-10T00:00:00Z"
        },
        "mainProcurementCategory": "services",
        "additionalProcurementCategories": [
          "consultingServices"
        ],
        "additionalClassifications": [
          {
            "id": "serv-a",
            "scheme": "internal",
            "description": "Services (Architectural)"
          }
        ],
        "milestones": [
          {
            "id": "1",
            "type": "securityClearanceDeadline",
            "dueDate": "2020-10-10T00:00:00Z"
          }
        ]
      },
      {
        "id": "lot-2",
        "identifiers": [
          {
            "id": "PROC/2020/0024-ABC-FGHI-2",
            "scheme": "internal"
          }
        ],
        "title": "Civil engineering services",
        "description": "For civil engineering services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 400000
        },
        "mainProcurementCategory": "services",
        "additionalProcurementCategories": [
          "consultingServices"
        ],
        "tenderPeriod": {
          "endDate": "2020-07-30T23:59:59+01:00"
        },
        "submissionMethodDetails": "https://www.acme.com/tender-submission/. All missing tenderer-related documents can be submitted later. Economic operators who ...",
        "submissionTerms": {
          "electronicSubmissionPolicy": "required"
        },
        "enquiryPeriod": {
          "endDate": "2020-07-15T23:59:59+01:00"
        },
        "contractPeriod": {
          "startDate": "2020-12-10T00:00:00Z",
          "endDate": "2021-12-10T00:00:00Z"
        },
        "additionalClassifications": [
          {
            "id": "serv-ce",
            "scheme": "internal",
            "description": "Services (Civil engineering)"
          }
        ],
        "milestones": [
          {
            "id": "1",
            "type": "securityClearanceDeadline",
            "dueDate": "2020-12-10T00:00:00Z"
          }
        ]
      },
      {
        "id": "lot-3",
        "identifiers": [
          {
            "id": "PROC/2020/0024-ABC-FGHI-3",
            "scheme": "internal"
          }
        ],
        "title": "Structural engineering",
        "description": "For structural engineering consultancy delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 600000
        },
        "tenderPeriod": {
          "endDate": "2020-07-30T23:59:59+01:00"
        },
        "submissionMethodDetails": "https://www.acme.com/tender-submission/. All missing tenderer-related documents can be submitted later. Economic operators who ...",
        "submissionTerms": {
          "electronicSubmissionPolicy": "required"
        },
        "enquiryPeriod": {
          "endDate": "2020-07-15T23:59:59+01:00"
        },
        "contractPeriod": {
          "startDate": "2021-02-10T00:00:00Z",
          "endDate": "2022-02-10T00:00:00Z"
        },
        "mainProcurementCategory": "services",
        "additionalProcurementCategories": [
          "consultingServices"
        ],
        "additionalClassifications": [
          {
            "id": "serv-se",
            "scheme": "internal",
            "description": "Services (Structural engineering)"
          }
        ],
        "milestones": [
          {
            "id": "1",
            "type": "securityClearanceDeadline",
            "dueDate": "2021-02-10T00:00:00Z"
          }
        ]
      }
    ],
    "lotGroups": [
      {
        "id": "lot-group-1",
        "title": "Civil and structural engineering services",
        "description": "Civil and structural engineering services for the development of a new public building",
        "identifiers": [
          {
            "id": "PROC/2020/0024-ABC-FGHI-G1",
            "scheme": "internal"
          }
        ],
        "relatedLots": [
          "lot-2",
          "lot-3"
        ],
        "optionToCombine": true,
        "maximumValue": {
          "currency": "GBP",
          "amount": 1000000
        }
      }
    ],
    "lotDetails": {
      "maximumLotsBidPerSupplier": 4,
      "maximumLotsAwardedPerSupplier": 2,
      "awardCriteriaDetails": "Percentage of people aggregated nationwide contestants undertake to cover, as indicated in their Economic Bids. The evaluation of proposals will be conducted based on the provisions of Article Y of the law on public private partnerships, and the provisions of the tender rules, performing in a first stage an evaluation of the technical bids and subsequently an assessment of the financial offer of the participants."
    },
    "amendments": [
      {
        "id": "1",
        "relatedLots": [
          "lot-1"
        ],
        "description": "Submission deadline extended."
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### No entregado

- Add fields:
  - `Amendment.relatedLots`
  - `Lot.additionalClassifications`
  - `Lot.buyer`
  - `Lot.enquiryPeriod`
  - `Lot.tenderPeriod`
  - `Lot.identifiers`
  - `Lot.mainProcurementCategory`
  - `Lot.additionalProcurementCategories`
  - `Lot.milestones`
  - `Lot.minimumValue`
  - `Lot.submissionMethodDetails`
  - `Lot.submissionTerms`
  - `LotGroup.identifiers`
  - `LotGroup.title`
  - `LotGroup.description`
  - `RelatedProcess.relatedLots`
- Make `Lot.id` and `LotGroup.id` required so that lots and lot groups are merged by identifier
- Move `Bid.relatedLots` to the Bid statistics and details extension
- Move `Finance.relatedLots` to the Finance extension
- Update field descriptions to use a neutral voice
- Add usage guidance

### v1.1.5

- Añadir el campo `tender.lotDetails.awardCriteriaDetails`.
- Añadir el campo `Finance.relatedLots`.
- Añadir el campo  `Lot.contractPeriod`.
- Quitar la información sobre el tipo de las descripciones de los campos
- Revisar las palabras normativas y no-normativas

### v1.1.4

- No permitir que `Tender.lotDetails` sea null (error introducido en la primera versión)
- Move `LotDetails` definition into `Tender.lotDetails` field
- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que los campos `relatedLots` tengan null en sus listas de cadenas
- Agregar enum a `Lot.status`
- Permitir que los campos `relatedLots` sean null
- Agregar título y descripción a `Tender.lotDetails`
- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
