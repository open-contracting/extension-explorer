# Criterios de selección

Agregar un objeto para describir los criterios para calificar a los candidatos a participar en un proceso de contratación.

This extension must be used with the [Award criteria breakdown](https://extensions.open-contracting.org/en/extensions/awardCriteria/master/) extension.

If your data closely follows the [Core Criterion and Core Evidence Vocabulary (CCCEV)](https://semiceu.github.io/CCCEV/), consider the [Requirements](https://extensions.open-contracting.org/en/extensions/requirements/master/) extension.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-702 (Selection Criteria) and BG-72 (Selection Criteria Second Stage Invite Number)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplos

### Tender

Potential suppliers and subcontractors must demonstrate a minimum of 10 years experience on similar projects.

```json
{
  "tender": {
    "selectionCriteria": {
      "criteria": [
        {
          "description": "Minimum number of years of experience on similar projects",
          "minimum": "10",
          "type": "technical",
          "subType": "slc-abil-ref-services",
          "appliesTo": [
            "supplier",
            "subcontractor"
          ]
        }
      ]
    }
  }
}
```

### Lot

A tender with a single lot where the selection criterion only applies for selecting candidates to be invited to the second stage of the procedure. The candidates will be selected only if the rate of their turnover over the value of the contract is at least 2. The procuring entity will use annual accounts from the previous two financial years to verify the candidates' turnover.

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "selectionCriteria": {
          "criteria": [
            {
              "description": "Turnover over contract value rate",
              "type": "economic",
              "forReduction": true,
              "numbers": [
                {
                  "number": 2,
                  "threshold": "minimumScore"
                }
              ],
              "verificationMethod": "Annual accounts from previous 2 financial years."
            }
          ]
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-10-10

- Add `subType` field to the `SelectionCriterion` object.

### 2024-01-25

- Add `verificationMethod` field to the `SelectionCriterion` object.

### 2023-04-05

- Add `forReduction` and `numbers` fields to the `SelectionCriterion` object. The `numbers` field reuses the `CriterionNumber` definition from the [Award criteria breakdown](https://extensions.open-contracting.org/en/extensions/awardCriteria/master/) extension.

### 2020-07-13

- Add `appliesTo` field.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) y en [pull requests](https://github.com/open-contracting-extensions/ocds_selectionCriteria_extension/pulls?q=is%3Apr+is%3Aclosed).
