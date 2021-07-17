# Procedure

This extension adds a block to describe the procurement procedure.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-88, BT-106, BT-1351](https://github.com/eForms/eForms) and [Article 93 and 45(3) of Directive 2014/25/EU](https://eur-lex.europa.eu/eli/dir/2014/25/oj). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

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

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_procedure_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/695>.
