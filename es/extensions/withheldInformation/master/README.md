# Withheld information

Adds a top-level withheld information array to describe items of information whose publication is temporarily or permanently withheld.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-8 (Not Immediately Published)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Ejemplo

```json
{
  "withheldInformation": [
    {
      "id": "cro-bor-law-18d27a53-0109-4f93-9231-6659d931bce0",
      "field": "cro-bor-law",
      "name": "Cross Border Law",
      "rationale": "Publication of this information is delayed because...",
      "rationaleClassifications": [
        {
          "scheme": "eu-non-publication-justification",
          "id": "oth-int",
          "description": "Other public interest",
          "uri": "http://publications.europa.eu/resource/authority/non-publication-justification/oth-int"
        }
      ],
      "availabilityDate": "2024-12-31T09:00:00+01:00"
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
