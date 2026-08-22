# Contract terms

Adds a contract terms object to the tender and lot objects, to describe the terms governing the future contract.

## Guidance

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-711 (Contract Terms), BT-801 (Non Disclosure Agreement), BT-802 (Non Disclosure Agreement Description), OPT-071 (Quality Target Code) and OPT-072 (Quality Target Description)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

### Tender

```json
{
  "tender": {
    "contractTerms": {
      "hasElectronicPayment": true,
      "hasElectronicOrdering": false,
      "electronicInvoicingPolicy": "required",
      "reservedExecution": true,
      "performanceTerms": "A set of KPIs will be developed for this contract and the successful tenderer will be measured against these for the duration of the contract. Please refer to briefing document for further details.",
      "financialTerms": "In the event that a work referred to in § 2.6 of the Agreement is created as part of the implementation of the Subject Matter of the Agreement, the Contractor shall indicate on the invoice what proportion of the remuneration for implementation.",
      "tendererLegalForm": "Contractors may jointly apply for the contract.",
      "hasExclusiveRights": false,
      "operatorRevenueShare": 0.25,
      "socialStandards": "The supplier maintains the social, collective bargaining and labor law obligations according to Union law, national law or collective agreements. 4 paragraph 4a Regulation 13707/2007.",
      "hasNonDisclosureAgreement": true,
      "nonDisclosureAgreement": "A non-disclosure agreement is required in order to...",
      "customerServices": [
        {
          "type": "clean",
          "name": "Cleanliness of rolling stock and station facilities",
          "description": "Rolling stock and station facilities must be kept at a minimum standard of cleanliness."
        }
      ]
    }
  }
}
```

### Lot

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "contractTerms": {
          "hasElectronicPayment": true,
          "hasElectronicOrdering": false,
          "electronicInvoicingPolicy": "required",
          "reservedExecution": true,
          "performanceTerms": "A set of KPIs will be developed for this contract and the successful tenderer will be measured against these for the duration of the contract. Please refer to briefing document for further details.",
          "financialTerms": "In the event that a work referred to in § 2.6 of the Agreement is created as part of the implementation of the Subject Matter of the Agreement, the Contractor shall indicate on the invoice what proportion of the remuneration for implementation.",
          "tendererLegalForm": "Contractors may jointly apply for the contract.",
          "hasExclusiveRights": false,
          "operatorRevenueShare": 0.25,
          "socialStandards": "The supplier maintains the social, collective bargaining and labor law obligations according to Union law, national law or collective agreements. 4 paragraph 4a Regulation 13707/2007.",
          "hasNonDisclosureAgreement": true,
          "nonDisclosureAgreement": "A non-disclosure agreement is required in order to...",
          "customerServices": [
            {
              "type": "clean",
              "name": "Cleanliness of rolling stock and station facilities",
              "description": "Rolling stock and station facilities must be kept at a minimum standard of cleanliness."
            }
          ]
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-12-04

- Update and clarify `operatorRevenueShare` field description.

### 2023-03-10

- Add `hasNonDisclosureAgreement`, `nonDisclosureAgreement` and `customerServices` fields.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_contractTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
