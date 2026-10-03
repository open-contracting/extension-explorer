# Procedimiento

Esta extensión agrega un bloque para describir el procedimiento de contratación.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-88, BT-106, BT-1351](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) and [Article 93 and 45(3) of Directive 2014/25/EU](https://eur-lex.europa.eu/eli/dir/2014/25/oj). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "tender": {
    "procedure": {
      "isAccelerated": true,
      "acceleratedRationale": "The medicinal product is of major public health interest particularly from the point of view of therapeutic innovation.",
      "features": "http://www.legislation.gov.uk/uksi/2015/102/pdfs/uksi_20150102_en.pdf"
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_procedure_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/695>.
