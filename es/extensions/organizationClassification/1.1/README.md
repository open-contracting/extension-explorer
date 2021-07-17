# Organization classification

Adds an array of Classification objects to Organization.details in order to categorize organizations.

## Legal context

En la Unión Europea, los campos de esta extensión corresponden a [eForms BT-10 (Actividad de la Autoridad)](https://github.com/eForms/eForms). Consulte \[OCDS para la Unión Europea\] (http://standard.open-contracting.org/profiles/eu/master/en/) para ver las correspondencias con Tenders Electronic Daily (TED).

## Ejemplos

```json
{
  "parties": [
    {
      "id": "1",
      "details": {
        "classifications": [
          {
            "id": "10",
            "scheme": "TED_CA_ACTIVITY",
            "description": "Social protection"
          }
        ]
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_organizationClassification_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/711>.
