# Bid opening

Adds an object to describe the date, time, place and other details of the bid opening.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-132, BT-133, BT-134](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Example

```json
{
  "tender": {
    "bidOpening": {
      "date": "2019-10-16T15:00:00+01:00",
      "address": {
        "streetAddress": "Town Hall, St Aldate's",
        "region": "Oxfordshire",
        "locality": "Oxford",
        "postalCode": "OX1 1BX",
        "countryName": "United Kingdom"
      },
      "location": {
        "description": "Central Oxford",
        "geometry": {
          "type": "Point",
          "coordinates": [
            51.751944,
            -1.257778
          ]
        },
        "gazetteer": {
          "scheme": "GEONAMES",
          "identifiers": [
            "2640729"
          ]
        },
        "uri": "http://www.geonames.org/2640729/oxford.html"
      },
      "description": "We recommend that people who wish to attend the opening register on this page: https://wwww.example.org/register"
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_bidOpening_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/749>.
