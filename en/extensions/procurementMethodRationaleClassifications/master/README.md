# Procurement method rationale classifications

Adds an array to the tender object to classify the procurement method rationale.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-136 (Direct Award Justification Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "tender": {
    "procurementMethodRationaleClassifications": [
      {
        "id": "D_NO_TENDERS_REQUESTS",
        "description": "No tenders or no suitable tenders/requests to participate in response to a procedure with prior call for competition",
        "scheme": "TED_PT_AWARD_CONTRACT_WITHOUT_CALL"
      },
      {
        "id": "D_FROM_LIQUIDATOR_CREDITOR",
        "description": "Purchase of supplies or services on particularly advantageous terms from the liquidator in an insolvency procedure, an arrangement with creditors or a similar procedure under national laws and regulations",
        "scheme": "TED_PT_AWARD_CONTRACT_WITHOUT_CALL"
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-04-05

- Add 'eu-direct-award-justification' code to the `+itemClassificationScheme.csv` codelist patch.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_procurementMethodRationaleClassifications_extension/pulls?q=is%3Apr+is%3Aclosed).
