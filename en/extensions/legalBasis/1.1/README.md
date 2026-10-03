# Legal basis

Adds fields to the tender object to describe the legal basis of the contracting process – that is, the laws and regulations that govern the contracting process and that grant legal authority to the procuring entity.

The `tender.legalBasis` field is a `Classification` object. Example classification schemes are [LEX](<https://en.wikipedia.org/wiki/Lex_(URN)>), [CELEX](https://eur-lex.europa.eu/content/help/faq/intro.html#help8) and [ELI](https://en.wikipedia.org/wiki/European_Legislation_Identifier).

To identify the procedure used, whether by formal name or by legal citation, use the [`tender.procurementMethodDetails`](https://standard.open-contracting.org/latest/en/schema/reference/#release-schema.json,/definitions/Tender,procurementMethodDetails) field.

To indicate whether the contracting process is covered by a treaty, like the Agreement on Government Procurement (GPA), use the [coveredBy](https://extensions.open-contracting.org/en/extensions/coveredBy/) extension. To indicate whether the contracting process is accelerated, involves framework agreements, or has other modalities, [browse the extensions](https://extensions.open-contracting.org/).

## Guidance

If the legal basis is country-specific, it is recommended to prefix the [ISO 3166-1 alpha-2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to the classification scheme: for example, "HN-ONCAE" for the Oficina Normativa de Contratación y Adquisiciones del Estado (ONCAE) in Honduras.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-01 (Procedure Legal Basis), BT-09 (Cross Border Law)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) and [Article 39, paragraph 5 of Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1585836130257&uri=CELEX:32014L0024#d1e4669-65-1). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "tender": {
    "crossBorderLaw": "Italian procurement legislation",
    "legalBasis": {
      "id": "32014L0025",
      "scheme": "CELEX"
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-08-01

- Add 'ELI' code to the `+itemClassificationScheme.csv` codelist patch.

### 2021-01-19

- Add guidance on the choice of the classification scheme for country-specific legal basis.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_contractTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
