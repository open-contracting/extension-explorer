# Submission terms

Adds a submission terms object to the tender and lot objects, to describe how, when and where the tenderers must submit their bids.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-102 (Submission Terms)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "tender": {
    "submissionTerms": {
      "electronicSubmissionPolicy": "notAllowed",
      "advancedElectronicSignatureRequired": false,
      "electronicCatalogPolicy": "notAllowed",
      "variantPolicy": "notAllowed",
      "multipleBidsAllowed": true,
      "languages": [
        "fr",
        "es"
      ],
      "bidValidityPeriod": {
        "startDate": "2019-09-20T00:00:00Z",
        "endDate": "2019-12-02T23:59:59Z",
        "durationInDays": 74
      },
      "depositsGuarantees": "An on-demand performance bond issued by an entity that the Contracting Entity judges to be acceptable (e.g. a bank or insurance company) and whose value is a percentage of the total contract price.",
      "subcontractingClauses": [
        "subc-oblig"
      ],
      "nonElectronicSubmission": {
        "address": {
          "streetAddress": "Town Hall, St Aldate's",
          "region": "Oxfordshire",
          "locality": "Oxford",
          "postalCode": "OX1 1BX",
          "countryName": "United Kingdom"
        },
        "rationale": "Inclusion of a physical model"
      }
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2024-01-19

- Rename `electronicCataloguePolicy` to `electronicCatalogPolicy`.

### 2023-10-20

- Add `SubmissionTerms.nonElectronicSubmission` field.
- Remove `SubmissionTerms.nonElectronicSubmissionRationale` field.

### 2023-06-07

- Define "electronic catalog" for the `electronicCatalogPolicy` field.

### 2023-05-22

- Add fields for eForms:
  - `SubmissionTerms.advancedElectronicSignatureRequired`
  - `SubmissionTerms.multipleBidsAllowed`
  - `SubmissionTerms.nonElectronicSubmissionRationale`
  - `SubmissionTerms.subcontractingClauses`

### 2020-09-29

- Rename `requiresGuarantees` to `depositsGuarantees`.
- Change the `type` of `depositsGuarantees` from a boolean to a string, to match the type of the corresponding XML element in TED XML Schema 2.09.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_submissionTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
