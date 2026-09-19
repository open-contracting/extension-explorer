# Términos de Presentación de la Oferta

Agrega un objeto términos de presentación de la oferta a los objetos de la licitación y del lote, para describir cómo, cuándo y dónde los oferentes deberán presentar sus ofertas.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-102 (Submission Terms)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "tender": {
    "submissionTerms": {
      "electronicSubmissionPolicy": "notAllowed",
      "advancedElectronicSignatureRequired": false,
      "electronicCatalogPolicy": "notAllowed",
      "variantPolicy": "notAllowed",
      "multipleBidsAllowed": true,
      "languages": [
        "fr",
        "es"
      ],
      "bidValidityPeriod": {
        "startDate": "2019-09-20T00:00:00Z",
        "endDate": "2019-12-02T23:59:59Z",
        "durationInDays": 74
      },
      "depositsGuarantees": "An on-demand performance bond issued by an entity that the Contracting Entity judges to be acceptable (e.g. a bank or insurance company) and whose value is a percentage of the total contract price.",
      "subcontractingClauses": [
        "subc-oblig"
      ],
      "nonElectronicSubmission": {
        "address": {
          "streetAddress": "Town Hall, St Aldate's",
          "region": "Oxfordshire",
          "locality": "Oxford",
          "postalCode": "OX1 1BX",
          "countryName": "United Kingdom"
        },
        "rationale": "Inclusion of a physical model"
      }
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-01-19

- Rename `electronicCataloguePolicy` to `electronicCatalogPolicy`.

### 2023-10-20

- Add `SubmissionTerms.nonElectronicSubmission` field.
- Remove `SubmissionTerms.nonElectronicSubmissionRationale` field.

### 2023-06-07

- Define "electronic catalog" for the `electronicCatalogPolicy` field.

### 2023-05-22

- Add fields for eForms:
  - `SubmissionTerms.advancedElectronicSignatureRequired`
  - `SubmissionTerms.multipleBidsAllowed`
  - `SubmissionTerms.nonElectronicSubmissionRationale`
  - `SubmissionTerms.subcontractingClauses`

### 2020-09-29

- Rename `requiresGuarantees` to `depositsGuarantees`.
- Cambiar el `type` de `depositsGuarantees` de un boolean a una cadena para que coincida con el tipo del elemento XML correspondiente a TED XML Schema 2.09.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para la Unión Europea\] (https://github.com/open-contracting-extensions/european-union/issues) y en [pull requests](https://github.com/open-contracting-extensions/ocds_submissionTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
