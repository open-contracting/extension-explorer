# Amendment rationale classifications

Adds a field to the amendment object to classify its rationale.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-140 (Change Reason Code) and BT-200 (Modification Reason Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Ejemplo

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

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Changelog

### 2025-02-11

- Update the `+itemClassificationScheme.csv` codelist patch:
  - Fix the Title, Description and Source of 'eu-change-corrig-justification'
  - Add 'eu-modification-justification'
