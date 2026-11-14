# Statistics

Adds a top-level statistics array to describe statistics about the contracting process.

This extension must be used with the [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/master/) extension.

## Guidance

If you use a codelist for `statistics.measure`, you should explain where the codes are from in your publication policy/user guide.

## Example

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

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
