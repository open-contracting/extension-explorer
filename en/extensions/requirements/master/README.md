# Requirements

Adds fields to express the [Core Criterion and Core Evidence Vocabulary (CCCEV)](https://semiceu.github.io/CCCEV/).

CCCEV is designed to support the exchange of information between buyers or procuring entities that define criteria and tenderers that respond to these criteria by means of evidences. Criteria can relate to bids, tenderers, lots or items.

If your data does not closely follow the [Core Criterion and Core Evidence Vocabulary (CCCEV)](https://semiceu.github.io/CCCEV/), consider the [Selection criteria](https://extensions.open-contracting.org/en/extensions/selectionCriteria/master/) extension.

## CCCEV Model

The CCCEV model defines the following concepts:

**Criterion**
A criterion represents a rule or principle used to judge, evaluate or assess bids, tenderers, lots or items. A criterion is satisfied when one or more of its requirement groups is satisfied.

**Requirement Group**
A requirement group is a collection of one or more individual requirements. A requirement group is satisfied when all of it's requirements are satisfied.

**Requirement**
An atomic requirement which can be expressed as either an expected value or a range of accepted values.

**Requirement Response**
A requirements response is an assertion that responds to a specific requirement.

Therefore the CCCEV model can be used to express both **AND** conditions, where a group of requirements must be met to satisfy a criterion, and **OR** conditions, where there are alternative requirements that can satisfy a criterion.

The CCCEV model also defines a number of additional concepts including **formalFrameworks**, used to specify the legal instruments from criteria are derived, **evidence**, used both to specify and provide the evidence required to support a response, and additional properties of *requirements* such as **certificationLevel**. These are not yet implemented in this extension. This extension also does not describe formulae for calculating computed values, nor does it describe whether data should be published openly or not.

## Example

Criteria for an item and a tenderer, with **AND** and **OR** conditions:

```json
{
  "tender": {
    "criteria": [
      {
        "id": "0001",
        "title": "Air intake",
        "description": "The vacuum cleaner air intake must be at least 100W",
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
        "description": "Number of years the tenderer has been trading",
        "relatesToTenderer": true,
        "requirementGroups": [
          {
            "id": "0003-001",
            "description": "Number of years the tenderer has been trading",
            "requirements": [
              {
                "id": "0003-001-01",
                "title": "Years trading",
                "description": "Number of years the tenderer has been trading",
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

Responses to the criteria:

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

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-06-07

- Replace `Criterion.relatesTo` codelist field with `Criterion.relatesToTenderer` boolean field.
- Remove `Award.requirementResponses`.
- Remove `Contract.requirementResponses`.
- Remove `Criterion.source`.
- Remove `RequirementResponse.relatedTenderer`.
- Remove the `relatesTo.csv` codelist.
- Remove the `responseSource.csv` codelist.

### 2023-04-18

- Add `Criterion.relatedLots` field.
- Remove unnecessary instructions from field descriptions.

### 2020-06-04

- Review normative and non-normative words.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/223>.

### 2019-03-20

- Set `"uniqueItems": true` on array fields, and add `"minLength": 1` on required string fields.

### 2018-12-18

- `Requirement.expectedValue` and `RequirementResponse.value` allow boolean values.
