# Clasificación de la licitación

Agregar una serie de objetos de clasificación al objeto de licitación para categorizar el procedimiento o la solicitud de orden de compra como un todo.

Se espera que los ítems a ser adquiridos tengan clasificaciones más específicas que el procedimiento en su conjunto.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-261 (Classification)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

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

- Agregar "o solicitud de orden de compra" en la descripción de la extensión.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) y en [pull requests](https://github.com/open-contracting-extensions/ocds_tenderClassification_extension/pulls?q=is%3Apr+is%3Aclosed).
