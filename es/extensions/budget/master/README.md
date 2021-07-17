# Desglose del presupuesto

## Antecedentes

La sección `planning` del OCDS puede usarse para describir los antecedentes de un proceso de contratación, que puede incluir detalles del presupuesto del cual se extraen los fondos.

La estructura principal OCDS incluye un solo campo `budget.amount` para capturar el monto total del presupuesto para el proceso de contratación.

## Proporcionar información presupuestaria más detallada

Algunas implementaciones de OCDS requieren información más detallada sobre los presupuestos divulgados, por ejemplo presupuestos plurianuales o presupuestos provenientes de varios departamentos gubernamentales diferentes. En el caso de las APP, los presupuestos pueden provenir del sector privado o de bancos multilaterales de desarrollo.

Esta extensión proporciona una manera de describir los presupuestos multi-anuales y multi-fuente.

La divulgación de datos estructurados de presupuestos de fuentes múltiples permite a los usuarios entender cuánto de los fondos para un proyecto provienen del gobierno o de un departamento específico, mientras que los datos estructurados sobre presupuestos multi-anuales permiten a los usuarios entender el perfil de gasto esperado de un contrato.

## Guía

En el bloque principal de `planning.budget`, se debe utilizar` budget.amount` para capturar el valor total del presupuesto para el proceso de contratación.

Cuando se utiliza `budget.budgetBreakdown` para expresar un presupuesto de múltiples fuentes pero los detalles de la organización no se conocen para una o más partes del presupuesto, por ejemplo, en una APP donde el licitador del sector privado proporcionará parte del presupuesto , el campo `sourceParty.name` debe usarse para proporcionar una explicación de texto libre de la fuente del presupuesto, por ejemplo "Inversión del sector privado del licitador ganador".

## Ejemplos

### Presupuestos de múltiples fuentes

El siguiente fragmento JSON modela un presupuesto multi-fuente de un solo año:

```json
{
  "planning": {
    "budget": {
      "id": "1",
      "description": "Multi-source budget, see budget breakdown for details.",
      "amount": {
        "amount": 300000,
        "currency": "GBP"
      },
      "budgetBreakdown": [
        {
          "sourceParty": {
            "id": "GB-LAC-E09000003-557",
            "name": "London Borough of Barnet - Transport Services"
          },
          "period": {
            "startDate": "2016-01-01T00:00:00Z",
            "endDate": "2016-12-31T23:59:59Z"
          },
          "id": "001",
          "description": "Budget contribution from the local government",
          "amount": {
            "amount": 150000,
            "currency": "GBP"
          }
        },
        {
          "sourceParty": {
            "id": "GB-GOV-23",
            "name": "Department for Transport"
          },
          "period": {
            "startDate": "2016-01-01T00:00:00Z",
            "endDate": "2016-12-31T23:59:59Z"
          },
          "id": "002",
          "description": "Budget contribution from the national government",
          "amount": {
            "amount": 150000,
            "currency": "GBP"
          }
        }
      ]
    }
  },
  "parties": [
    {
      "id": "GB-GOV-23",
      "name": "Department for Transport",
      "roles": [
        "funder"
      ]
    },
    {
      "id": "GB-LAC-E09000003-557",
      "name": "London Borough of Barnet - Transport Services",
      "roles": [
        "funder"
      ]
    }
  ]
}
```

### Presupuestos multi-anuales

El siguiente fragmento JSON modela un presupuesto multi-anual de fuente única:

```json
{
  "planning": {
    "budget": {
      "id": "2",
      "description": "Multi-year budget, see budget breakdown for details.",
      "amount": {
        "amount": 300000,
        "currency": "GBP"
      },
      "budgetBreakdown": [
        {
          "period": {
            "startDate": "2016-01-01T00:00:00Z",
            "endDate": "2016-12-31T00:00:00Z"
          },
          "id": "001",
          "description": "2016 Budget",
          "amount": {
            "amount": 200000,
            "currency": "GBP"
          }
        },
        {
          "period": {
            "startDate": "2017-01-01T00:00:00Z",
            "endDate": "2017-12-31T00:00:00Z"
          },
          "id": "002",
          "description": "2017 Budget",
          "amount": {
            "amount": 100000,
            "currency": "GBP"
          }
        }
      ]
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2019-01-30

- Remover la propiedad obsoleta `mergeStrategy`.

### 2018-05-08

- Hacer obligatorio y no nulo `BudgetBreakdown.id` para permitir el seguimiento de revisiones y [fusión de listas](http://standard.open-contracting.org/latest/es/schema/merging/#lists)
