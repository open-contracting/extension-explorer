# Contract terms

Adds a contract terms object to the tender and lot objects, to describe the terms governing the future contract.

## Guidance

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-711 (Contract Terms)](https://github.com/eForms/eForms), although not all the fields have been implemented yet. See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Example

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
      "socialStandards": "The supplier maintains the social, collective bargaining and labor law obligations according to Union law, national law or collective agreements. 4 paragraph 4a Regulation 13707/2007."
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_contractTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
