# Selection Criteria

Adds an object to describe the criteria to qualify candidates to participate in a contracting process.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-702 (Selection Criteria)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Examples

```json
{
  "tender": {
    "selectionCriteria": {
      "criteria": [
        {
          "description": "<Description of the criterion>",
          "minimum": "<Minimum value or level of compliance>",
          "type": "technical",
          "appliesTo": [
            "supplier",
            "subcontractor"
          ]
        },
        {
          "description": "<Description of the criterion>",
          "minimum": "<Minimum value or level of compliance>",
          "type": "economic",
          "appliesTo": [
            "supplier"
          ]
        }
      ]
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-07-13

- Add the `appliesTo` field

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_selectionCriteria_extension/pulls?q=is%3Apr+is%3Aclosed).
