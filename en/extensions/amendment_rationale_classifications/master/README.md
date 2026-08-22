# Amendment rationale classifications

Adds a field to the amendment object to classify its rationale.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-140 (Change Reason Code) and BT-200 (Modification Reason Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Example

```json
{
  "tender": {
    "id": "1",
    "amendments": [
      {
        "rationaleClassifications": [
          {
            "id": "update-add",
            "description": "Information updated",
            "scheme": "eu-change-corrig-justification"
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

### 2025-02-11

- Update the `+itemClassificationScheme.csv` codelist patch:
  - Fix the Title, Description and Source of 'eu-change-corrig-justification'
  - Add 'eu-modification-justification'
