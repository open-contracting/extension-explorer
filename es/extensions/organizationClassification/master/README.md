# Clasificación de la organización

Agrega una lista de objetos de clasificación a los detalles de una organización, con el fin de categorizarla.

## Ejemplos

An organization categorized as a social protection business.

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

An organization classified as a women-owned small business by the Small Business Administration in the USA.

```json
{
  "parties": [
    {
      "id": "1",
      "details": {
        "classifications": [
          {
            "id": "WOSB",
            "scheme": "USA-SBA",
            "description": "Woman-Owned Small Business",
            "uri": "https://www.ecfr.gov/current/title-13/chapter-I/part-127/subpart-B"
          }
        ]
      }
    }
  ]
}
```

For a longer example, see the [organization classifications](https://standard.open-contracting.org/latest/en/guidance/map/organization_classifications/#example-2-2-disclosing-data-using-a-local-scheme) guidance in the OCDS documentation.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-05-22

- Add 'eu-buyer-legal-type' code to the `+itemClassificationScheme.csv` codelist patch.

### 2023-08-01

- Add 'eu-buyer-contracting-type' and 'eu-main-activity' codes to the `+itemClassificationScheme.csv` codelist patch.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_organizationClassification_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/711>.
