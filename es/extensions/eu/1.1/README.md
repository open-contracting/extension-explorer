# Unión Europea

Implementa campos y código que son específicos de la legislación europea.

For complete guidance on meeting the disclosure requirements of European law, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/) for the 2019 regulation, or [OCDS for European Union](https://standard.open-contracting.org/profiles/eu/latest/en/) for the 2015 regulation.

## Ejemplo

```json
{
  "parties": [
    {
      "details": {
        "url": "https://www.manchester.ac.uk/",
        "buyerProfile": "https://in-tendhost.co.uk/universityofmanchester/aspx/Home"
      },
      "roles": [
        "leadBuyer",
        "awardingCentralPurchasingBody",
        "evaluationBody",
        "submissionReceiptBody"
      ]
    },
    {
      "name": "Royal Tax Office",
      "id": "08797655",
      "contactPoint": {
        "name": "Crown Commercial Service",
        "email": "info@crowncommercial.gov.uk",
        "url": "https://www.gov.uk/government/publications/procurement-policy-note-0314-promoting-tax-compliance"
      },
      "roles": [
        "informationService"
      ]
    }
  ],
  "bids": {
    "details": [
      {
        "id": "1",
        "foreignSubsidyMeasures": "fsr-stand"
      }
    ]
  },
  "tender": {
    "contractPeriod": {
      "description": "unknown"
    },
    "reviewDetails": "NHS Wales Shared Services Partnership on behalf of Cardiff and Vale University Local Health Board will allow a minimum 10 calendar day standstill period between notifying the award decision and awarding the contract.",
    "valueCalculationMethod": "Income from the sales of tickets over the duration of the contract minus the fees paid to the procuring entity.",
    "items": [
      {
        "id": "item-1",
        "description": "Printer ink cartridges",
        "classification": {
          "scheme": "CPV",
          "id": "45233130.0",
          "description": "Office supplies",
          "uri": "http://cpv.data.ac.uk/code-45233130"
        }
      }
    ],
    "legislativeReferences": [
      {
        "title": "Direct taxation in the EU",
        "url": "https://eur-lex.europa.eu/summary/chapter/2101.html",
        "informationService": {
          "name": "Royal Tax Office",
          "id": "08797655"
        }
      }
    ],
    "lots": [
      {
        "id": "lot-1",
        "awardPeriod": {
          "durationInDays": 30,
          "startDate": "2020-11-06T00:00:00Z",
          "endDate": "2020-12-06T00:00:00Z"
        },
        "contractPeriod": {
          "description": "unknown"
        },
        "additionalClassifications": [
          {
            "id": "oth-serv-contr",
            "scheme": "eu-cvd-contract-type",
            "description": "Other service contract"
          }
        ]
      }
    ],
    "milestones": [
      {
        "id": "1",
        "type": "securityClearanceDeadline",
        "dueDate": "2020-11-19T00:00:00Z"
      }
    ],
    "documents": [
      {
        "id": "Fiscal1",
        "documentType": "legislation"
      }
    ],
    "selectionCriteria": {
      "sources": [
        "epo-notice"
      ]
    },
    "exclusionGrounds": {
      "sources": [
        "epo-notice"
      ]
    }
  },
  "awards": [
    {
      "id": "award-1",
      "valueCalculationMethod": "The awarded value takes into account the growing revenue expected from fees and the value of the equipment provided by the contracting authority.",
      "items": [
        {
          "id": "1",
          "additionalClassifications": [
            {
              "scheme": "eu-vehicle-category",
              "id": "n2-n3",
              "description": "Truck (N2-N3)"
            }
          ]
        }
      ]
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "periodRationale": "The duration of the contract has been extended to anticipate the exceptional snowfall expected in January.",
      "publicPassengerTransportServicesKilometers": 765,
      "awardID": "award-1"
    }
  ],
  "relatedProcesses": [
    {
      "id": "1",
      "identifier": "123e4567-e89b-12d3-a456-426614174000-06",
      "part": "PAR-0001",
      "scheme": "eu-notice-id-ref",
      "relationship": [
        "planning"
      ]
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2025-02-11

- Add 'eu-vehicles' code to the `+itemClassificationScheme.csv` codelist patch.

### 2025-02-04

- Add `RelatedProcess.part` field.
- Update the `+relatedProcessScheme.csv` codelist patch:
  - Add 'eu-notice-id-ref'
  - Add 'eu-ojs-notice-id'
  - Remove 'eu-oj'

### 2024-10-18

- Add `Bid.foreignSubsidyMeasures` field.
- Add a `foreignSubsidyMeasures.csv` codelist for `Bid.foreignSubsidyMeasures`.
- Remove `Item.deliveryAddresses` field (now in Location extension).

### 2024-10-08

- Add fields:
  - `SelectionCriteria.sources`
  - `ExclusionGrounds.sources`
- Add a `sources.csv` codelist for `SelectionCriteria.sources` and `ExclusionGrounds.sources`.

### 2023-08-01

- Add fields:
  - `Organization.eDeliveryGateway`
  - `Lot.hasAccessibilityCriteria`
  - `Lot.noAccessibilityCriteriaRationale`
  - `Lot.reviewDetails`

### 2023-06-30

- Add `Period.description` field.
- Add a `+classificationScheme.csv` codelist patch, with 'eu-vehicle-category' and 'eu-cvd-contract-type' codes.
- Add a `+relatedProcessScheme.csv` codelist patch, with a 'eu-oj' code.
- Add codes:
  - `+documentType.csv`:
    - 'legislation'
  - `+partyRole.csv`:
    - 'procurementServiceProvider'
    - 'eSender'
    - 'leadBuyer'
    - 'leadTenderer'
    - 'evaluationBody'
    - 'submissionReceiptBody'
- Move 'informationService' from the `+partyRole.csv` codelist patch to the Document publisher extension.

### 2022-05-27

- Move `Lot.minimumValue` to the Lots extension.

### 2021-01-19

- Establecer el tipo de objeto de `informationService` a` OrganizationReference`.
- Add 'informationService' code to the `+partyRole.csv` codelist patch.

### 2020-10-06

- Add `Lot.awardPeriod` field.

### 2020-10-05

- Add `Lot.minimumValue` field.

### 2020-07-13

- Add 'securityClearanceDeadline' code to the `+milestoneType.csv` codelist patch.

### 2020-04-29

- Add `Item.deliveryAddresses` field.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [este issue](https://github.com/open-contracting/european-union-support/issues/19) y en [pull requests](https://github.com/open-contracting-extensions/ocds_eu_extension/pulls?q=is%3Apr+is%3Aclosed).
