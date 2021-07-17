# Requisitos

La ampliación de los requisitos se basa en el modelo de la UE [Vocabulario de Criterios Fundamentales y Evidencia Básica (CCCEV)](https://joinup.ec.europa.eu/node/153001) para comunicar criterios y respuestas.

La extensión está diseñada para permitir que las entidades compradoras o los compradores expresen criterios, relacionados con los artículos adquiridos o sobre los propios licitadores, como datos estructurados.

Los criterios pueden ser respondidos por los licitadores, compradores o entidades compradoras, por ejemplo un comprador puede responder con información sobre un artículo, mientras que una entidad licitadora puede responder con información sobre si un licitador está inhabilitado.

## Modelo CCCEV

El modelo CCCEV define los siguientes conceptos:

**Criterion**
A criterion represents a rule or principle used to judge, evaluate or assess either an item or bidder. A criterion is satisfied when one or more of it's requirement groups are satisfied.

**Requirement Group**
A requirement group is a collection of one or more individual requirements. A requirement group is satisfied when all of it's requirements are satisfied.

**Requirement**
An atomic requirement which can be expressed as either an expected value or a range of accepted values.

**Requirement Response**
A requirements response is an assertion that responds to a specific requirement.

Por lo tanto, el modelo CCCEV puede usarse para expresar las condiciones **AND**, donde un grupo de requisitos debe cumplirse para satisfacer un criterio, así como las condiciones **OR**, donde existen requisitos alternativos que pueden satisfacer un criterio.

## Esquema

La extensión introduce un nuevo bloque para cada uno de los conceptos descritos anteriormente, estos se agregan a las siguientes ubicaciones en el esquema de OCDS:

- *tender.criteria* - una lista de criterios
- *tender.criteria.requirementGroups* - una lista de grupos de requisitos
- *tender.criteria.requirementGroups.requirements* - una lista de requisitos
- *bids.requirementResponses* - una lista de respuestas de requerimientos (Nota: depende de la extensión *bid*)
- *awards.requirementResponses* - una lista de respuestas de requisitos
- *contracts.requirementResponses* - una lista de respuestas a los requisitos

## Ejemplo

A continuación se muestra un ejemplo de requisitos especificados tanto en un artículo como en un licitador que demuestra las condiciones **AND** y **OR**:

```json
{
  "tender": {
    "criteria": [
      {
        "id": "0001",
        "title": "Air intake",
        "description": "The vacuum cleaner air intake must be at least 100W",
        "source": "tenderer",
        "relatesTo": "item",
        "relatedItem": "item1",
        "requirementGroups": [
          {
            "id": "0001-001",
            "description": "The vacuum cleaner air intake must be at least 100W",
            "requirements": [
              {
                "id": "0001-001-01",
                "title": "Air intake",
                "description": "Power of vacuum cleaner air intake in W",
                "dataType": "integer",
                "pattern": "[0-9]*",
                "minValue": 100
              }
            ]
          }
        ]
      },
      {
        "id": "0002",
        "title": "Warranty",
        "description": "The vacuum cleaner must have warranty support options for at least 36 months",
        "source": "tenderer",
        "relatesTo": "item",
        "relatedItem": "item1",
        "requirementGroups": [
          {
            "id": "0002-001",
            "description": "The standard warranty period for the vacuum cleaner must be at least 36 months",
            "requirements": [
              {
                "id": "0002-001-01",
                "title": "Standard warranty period",
                "description": "Length of the vacuum cleaner standard warranty period in months",
                "dataType": "integer",
                "pattern": "[0-9]*",
                "minValue": 36
              }
            ]
          },
          {
            "id": "0002-002",
            "description": "The standard warranty period for the vacuum cleaner must be at least 12 months with an option to extend to 36 months",
            "requirements": [
              {
                "id": "0002-002-01",
                "title": "Standard warranty period",
                "description": "Length of the vacuum cleaner standard warranty period in months",
                "dataType": "integer",
                "pattern": "[0-9]*",
                "minValue": 12
              },
              {
                "id": "0002-002-02",
                "title": "Extended warranty option",
                "description": "There is an extended warranty option for at least 36 months",
                "dataType": "boolean",
                "expectedValue": true
              }
            ]
          }
        ]
      },
      {
        "id": "0003",
        "title": "Years trading",
        "description": "Number of years the bidder has been trading",
        "source": "tenderer",
        "relatesTo": "tenderer",
        "requirementGroups": [
          {
            "id": "0003-001",
            "description": "Number of years the bidder has been trading",
            "requirements": [
              {
                "id": "0003-001-01",
                "title": "Years trading",
                "description": "Number of years the bidder has been trading",
                "dataType": "integer",
                "pattern": "[0-9]*",
                "minValue": 3
              }
            ]
          }
        ]
      }
    ]
  }
}
```

A continuación se muestra un ejemplo de respuestas que cumplen los requisitos anteriores:

```json
{
  "bids": {
    "details": [
      {
        "id": "1",
        "requirementResponses": [
          {
            "id": "air",
            "value": 125,
            "requirement": {
              "id": "0001-001-01"
            }
          },
          {
            "id": "warranty",
            "value": 36,
            "requirement": {
              "id": "0002-001-01"
            }
          },
          {
            "id": "years",
            "value": 10,
            "requirement": {
              "id": "0003-001-01"
            }
          }
        ]
      }
    ]
  }
}
```

## Otras extensiones

El modelo CCCEV también define una serie de conceptos adicionales, incluyendo **formalFrameworks**, utilizado para especificar los instrumentos jurídicos de los que se derivan los criterios, **evidence**, utilizado para especificar y proporcionar la evidencia necesaria para respaldar una respuesta de requisito, y propiedades adicionales de *requirements* como **certificationLevel** que actualmente no están implementadas en esta extensión.

This extension does not describe formulae for calculating computed values, nor does it describe whether data should be published openly or not.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Review normative and non-normative words.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/223>.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2018-12-18

- `Requirement.expectedValue` y `RequirementResponse.value` permiten valores boolean.
