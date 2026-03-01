# Código de país

Agregar un campo código de país al objeto de dirección.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-514 (Organisation Country Code), BT-5141 (Place Country Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "parties": [
    {
      "id": "GB-LAC-E09000003",
      "name": "London Borough of Barnet",
      "address": {
        "streetAddress": "4, North London Business Park, Oakleigh Rd S",
        "locality": "London",
        "region": "London",
        "postalCode": "N11 1NP",
        "countryName": "United Kingdom",
        "country": "GB"
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

Si necesita usar un [código asignado por el usuario](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#User-assigned_code_elements), [crear un issue](https://github.com/open-contracting/standard/issues) para discutir su adición a la lista de códigos.

## Registro de cambios

### 2023-02-07

- Rename `countryCode` to `country` to match OCDS 1.2.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_countryCode/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/524>.
