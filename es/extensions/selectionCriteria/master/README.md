# Selection Criteria

Adds an object to describe the criteria to qualify candidates to participate in a contracting process.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-702 (Selection Criteria)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Ejemplos

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

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-07-13

- Add the `appliesTo` field

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_selectionCriteria_extension/pulls?q=is%3Apr+is%3Aclosed).
