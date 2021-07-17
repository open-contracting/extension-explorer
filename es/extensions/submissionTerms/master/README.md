# Submission terms

Adds a submission terms object to the tender and lot objects, to describe how, when and where the tenderers must submit their bids.

## Guía

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-102 (Submission Terms)](https://github.com/eForms/eForms), although not all the fields have been implemented yet. See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Ejemplo

```json
{
  "tender": {
    "submissionTerms": {
      "electronicSubmissionPolicy": "required",
      "electronicCataloguePolicy": "allowed",
      "variantPolicy": "notAllowed",
      "languages": [
        "fr",
        "es"
      ],
      "bidValidityPeriod": {
        "startDate": "2019-09-20T00:00:00Z",
        "endDate": "2019-12-02T23:59:59Z",
        "durationInDays": 74
      },
      "depositsGuarantees": "An on demand performance bond which value is a percentage of the total contract price issued by an acceptable entity by the Contracting Entity (e.g. bank or insurance company)."
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-09-29

- Rename `requiresGuarantees` to `depositsGuarantees`
- Change the `type` of `depositsGuarantees` from a boolean to a string, to match the type of the corresponding XML element in TED XML Schema 2.09.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_submissionTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
