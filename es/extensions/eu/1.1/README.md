# European Union

Implements fields and codes that are specific to European law.

For complete guidance on meeting the disclosure requirements of European law, see [OCDS for European Union](https://standard.open-contracting.org/profiles/eu/master/en/).

## Guía

If items have at most one delivery address, use the [Location](https://extensions.open-contracting.org/en/extensions/location/) extension instead ([see discussion](https://github.com/open-contracting/ocds-extensions/issues/115)).

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-99 (Review Deadline Description), BT-163 (Concession Value Description), BT-109 (Framework Duration Justification), BT-505 (Organisation Internet Address), BT-508 (Buyer Profile URL) and BG-708 (Place of Performance)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Ejemplo

```json
{
  "parties": [
    {
      "details": {
        "url": "https://www.manchester.ac.uk/",
        "buyerProfile": "https://in-tendhost.co.uk/universityofmanchester/aspx/Home"
      }
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
  "tender": {
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
        },
        "deliveryAddresses": [
          {
            "streetAddress": "4, North London Business Park, Oakleigh Rd S",
            "locality": "London",
            "region": "London",
            "postalCode": "N11 1NP",
            "countryName": "United Kingdom"
          }
        ]
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
        "minimumValue": {
          "amount": 12000,
          "currency": "EUR"
        },
        "awardPeriod": {
          "durationInDays": 30,
          "startDate": "2020-11-06T00:00:00Z",
          "endDate": "2020-12-06T00:00:00Z"
        }
      }
    ],
    "milestones": [
      {
        "id": "1",
        "type": "securityClearanceDeadline",
        "dueDate": "2020-11-19T00:00:00Z"
      }
    ]
  },
  "awards": [
    {
      "id": "award-1",
      "valueCalculationMethod": "The awarded value takes into account the growing revenue expected from fees and the value of the equipment provided by the contracting authority."
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "periodRationale": "The duration of the contract has been extended to anticipate the exceptional snowfall expected in January.",
      "publicPassengerTransportServicesKilometers": 765,
      "awardID": "award-1"
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2021-01-19

- Set the object type of `informationService` to `OrganizationReference`.
- Add 'informationService' code to `+partyRole.csv` codelist.

### 2020-10-06

- Add the `awardPeriod` field to the `Lot` object.

### 2020-10-05

- Add the `minimumValue` field to the `Lot` object.

### 2020-07-13

- Add the 'securityClearanceDeadline' code to the `+milestoneType.csv` codelist.

### 2020-04-29

- Add the `deliveryAddresses` field to the `Item` object.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [this issue](https://github.com/open-contracting/european-union-support/issues/19) and in [pull requests](https://github.com/open-contracting-extensions/ocds_eu_extension/pulls?q=is%3Apr+is%3Aclosed).
