# Estadística

Adds a top-level statistics array to describe statistics about the contracting process.

This extension must be used with the [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/master/) extension.

## Guía

If you use a codelist for `statistics.measure`, you should explain where the codes are from in your publication policy/user guide.

## Ejemplo

A statistic describing the number of complaints received about the unjustified rejection of abnormally low tenders. The value of `statistics.measure` is taken from the EU's [irregularity type codelist](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/irregularity-type).

```json
{
  "statistics": [
    {
      "id": "1",
      "value": 2,
      "measure": "ab-low",
      "scope": "complaints",
      "notes": "Unjustified rejection of abnormally low tenders"
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
