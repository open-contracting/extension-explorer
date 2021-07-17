# Tender classification

Adds an array of classification objects to the tender object, in order to categorize the procedure or call-off as a whole.

The items to be procured are expected to have more specific classifications than the procedure as a whole.

## Legal context

En la Unión Europea, los campos de esta extensión corresponden a [eForms BG-261 (Clasificación)](https://github.com/eForms/eForms). Consulte \[OCDS para la Unión Europea\] (http://standard.open-contracting.org/profiles/eu/master/en/) para ver las correspondencias con Tenders Electronic Daily (TED).

## Ejemplo

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

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2021-01-19

- Add "or call-off" in the description of the extension.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_tenderClassification_extension/pulls?q=is%3Apr+is%3Aclosed).
