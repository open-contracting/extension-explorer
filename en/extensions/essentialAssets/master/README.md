# Essential assets

Adds a object to the tender object to describe the assets used for the provision of public services.

## Legal context

In the European Union, this extension's fields correspond to [Article 4, clause 4 of Regulation 1370/2007](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32007R1370). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Examples

```json
{
  "tender": {
    "hasEssentialAssets": true,
    "essentialAssets": {
      "description": "Significant investments have been made by the supplier in the past years and will continue to be so in the future, which will pay for themselves over a period of time well beyond the period of the contract. It includes the purchase of new vehicles, the maintenance of the modernization of the existing fleet and the renovation of the vehicle depots."
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the OCDS for EU profile in [issue #60](https://github.com/open-contracting-extensions/european-union/issues/60) and in [pull requests](https://github.com/open-contracting-extensions/ocds_essentialAssets_extension/pulls?q=is%3Apr+is%3Aclosed).
