# Budget Breakdown

OCDS' `planning.budget` object can be used to describe the budget from which funds are drawn. It includes a single `budget.amount` field to capture the total value of the budget for a future contracting process.

This extension provides a way to describe the budget in greater detail, including multi-year budgets or budgets sourced from multiple organizations. In the case of PPPs, budgets may be sourced from the private sector or from multi-lateral development banks.

Disclosing structured data on multi-source budgets allows users to understand how much of the funds for a project come from government or from a specific department, whilst structured data on multi-year budgets allows users to understand the expected spend profile of a contract.

## Guidance

In the core `planning.budget` block, `budget.amount` should be used to capture the total value of the budget for a future contracting process.

Where `budget.budgetBreakdown` is used to express a multi-source budget but the organization details are not known for one or more parts of the budget, for example in a PPP where part of the budget will be provided by the successful private sector bidder, the `sourceParty.name` field should be used to provide a free text explanation of the source of the budget, e.g. "Private sector investment from successful bidder".

## Examples

### Multi-source budgets

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

### Multi-year budgets

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

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-06-07

- Add 'sourceParty' code to the `+partyRole.csv` codelist patch, because the 'funder' code is deprecated in OCDS 1.2.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Set `"uniqueItems": true` on array fields, and add `"minLength": 1` on required string fields.

### 2019-01-30

- Remove obsolete `mergeStrategy` properties

### 2018-05-08

- Make `BudgetBreakdown.id` required and non-nullable to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
