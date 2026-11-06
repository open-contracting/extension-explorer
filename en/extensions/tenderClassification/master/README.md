# Tender classification

Adds an array of classification objects to the tender object, in order to categorize the procedure or call-off as a whole.

The items to be procured are expected to have more specific classifications than the procedure as a whole.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-261 (Classification)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "tender": {
    "classification": {
      "description": "Advertising management services",
      "id": "79341200-8",
      "scheme": "CPV"
    },
    "additionalClassifications": [
      {
        "description": "Advertising campaign services",
        "id": "79341400-0",
        "scheme": "CPV"
      },
      {
        "description": "Customer services",
        "id": "79342300-6",
        "scheme": "CPV"
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2021-01-19

- Add "or call-off" in the description of the extension.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_tenderClassification_extension/pulls?q=is%3Apr+is%3Aclosed).
