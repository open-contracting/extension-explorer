# Award criteria breakdown

Adds an award criteria array to the lot object, to break down award criteria by price, cost and quality.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-707 (Award Criteria)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

[Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj) [Article 67](https://eur-lex.europa.eu/eli/dir/2014/24/oj#d1e5950-65-1)(5) describes weightings and orders of importance.

## Examples

### Weight

These award criteria are 50% service quality and 50% price.

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "awardCriteria": {
          "criteria": [
            {
              "type": "quality",
              "name": "Service quality",
              "numbers": [
                {
                  "number": 50,
                  "weight": "percentageExact"
                }
              ]
            },
            {
              "type": "price",
              "name": "Price",
              "numbers": [
                {
                  "number": 50,
                  "weight": "percentageExact"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```

### Fixed

The price is fixed at $100,000, such that tenderers compete on quality only.

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "awardCriteria": {
          "criteria": [
            {
              "type": "price",
              "name": "Fixed price",
              "numbers": [
                {
                  "number": 100000,
                  "fixed": "total"
                },
                {
                  "number": 0,
                  "weight": "decimalExact"
                }
              ]
            },
            {
              "type": "quality",
              "name": "Service quality",
              "numbers": [
                {
                  "number": 1,
                  "weight": "decimalExact"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This model was discussed in <https://github.com/eForms/eForms/issues/119>, <https://github.com/eprocurementontology/eprocurementontology/issues/157> and <https://github.com/eprocurementontology/eprocurementontology/issues/203>. This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_awardCriteria_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/443>.
