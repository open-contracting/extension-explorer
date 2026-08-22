# Procedure

This extension adds a block to describe the procurement procedure.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-88, BT-106, BT-1351](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) and [Article 93 and 45(3) of Directive 2014/25/EU](https://eur-lex.europa.eu/eli/dir/2014/25/oj). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

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

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_procedure_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/695>.
