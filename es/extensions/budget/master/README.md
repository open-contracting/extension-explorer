# Desglose del presupuesto

OCDS' `planning.budget` object can be used to describe the budget from which funds are drawn. It includes a single `budget.amount` field to capture the total value of the budget for a future contracting process.

Esta extensión permite describir el presupuesto con mayor detalle, incluidos los presupuestos plurianuales o los presupuestos procedentes de múltiples organizaciones. En el caso de las APP, los presupuestos pueden proceder del sector privado o de bancos de desarrollo multilaterales.

La divulgación de datos estructurados de presupuestos de fuentes múltiples permite a los usuarios entender cuánto de los fondos para un proyecto provienen del gobierno o de un departamento específico, mientras que los datos estructurados sobre presupuestos multi-anuales permiten a los usuarios entender el perfil de gasto esperado de un contrato.

## Guía

In the core `planning.budget` block, `budget.amount` should be used to capture the total value of the budget for a future contracting process.

Cuando se utiliza `budget.budgetBreakdown` para expresar un presupuesto de múltiples fuentes pero los detalles de la organización no se conocen para una o más partes del presupuesto, por ejemplo, en una APP donde el licitador del sector privado proporcionará parte del presupuesto , el campo `sourceParty.name` debe usarse para proporcionar una explicación de texto libre de la fuente del presupuesto, por ejemplo "Inversión del sector privado del licitador ganador".

## Ejemplos

### Presupuestos de múltiples fuentes

A single-year, multi-source budget:

```json
{
  "planning": {
    "budget": {
      "amount": {
        "amount": 300000,
        "currency": "GBP"
      },
      "budgetBreakdown": [
        {
          "id": "1",
          "description": "Budget contribution from the local government",
          "sourceParty": {
            "id": "GB-LAC-E09000003-557",
            "name": "London Borough of Barnet - Transport Services"
          },
          "amount": {
            "amount": 150000,
            "currency": "GBP"
          }
        },
        {
          "id": "2",
          "description": "Budget contribution from the national government",
          "sourceParty": {
            "id": "GB-GOV-23",
            "name": "Department for Transport"
          },
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

A multi-year, single-source budget:

```json
{
  "planning": {
    "budget": {
      "amount": {
        "amount": 70000,
        "currency": "GBP"
      },
      "budgetBreakdown": [
        {
          "id": "1",
          "description": "2021/2022",
          "period": {
            "startDate": "2021-04-01T00:00:00Z",
            "endDate": "2022-03-31T23:59:59Z"
          },
          "amount": {
            "amount": 20000,
            "currency": "GBP"
          }
        },
        {
          "id": "2",
          "description": "2022/2023",
          "period": {
            "startDate": "2022-04-01T00:00:00Z",
            "endDate": "2023-03-31T23:59:59Z"
          },
          "amount": {
            "amount": 50000,
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

### 2023-06-07

- Add 'sourceParty' code to the `+partyRole.csv` codelist patch, because the 'funder' code is deprecated in OCDS 1.2.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2019-01-30

- Eliminar la propiedad obsoleta `mergeStrategy`.

### 2018-05-08

- Make `BudgetBreakdown.id` required and non-nullable to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
