# Location Data

This extension adds address and location fields to tenders and items, to communicate the location of proposed or executed contract delivery.

The `locationGazetteers.csv` codelist's `Category` column indicates whether the gazetteer has identifiers for the whole world ('Universal') or only some subset ('National' or 'Sub-National').

## Example

Below is an example of a geolocated item in the `tender` section:

```json
{
  "tender": {
    "items": [
      {
        "id": "item1",
        "description": "Ceremonial Trumpets for Oxford Town Hall",
        "classification": {
          "description": "Trumpets",
          "scheme": "CPV",
          "id": "37312100",
          "uri": "http://purl.org/cpv/2008/code-37312100"
        },
        "deliveryLocations": [
          {
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
            "description": "Central Oxford",
            "uri": "http://www.geonames.org/2640729/oxford.html"
          }
        ],
        "deliveryAddresses": [
          {
            "postalCode": "OX1 1BX",
            "countryName": "United Kingdom",
            "streetAddress": "Town Hall, St Aldate's",
            "region": "Oxfordshire",
            "locality": "Oxford",
            "description": "The old town hall"
          }
        ],
        "unit": {
          "name": "Items",
          "value": {
            "currency": "GBP",
            "amount": 10000
          }
        },
        "quantity": 10
      }
    ]
  }
}
```

If the procurement related to the rebuilding of a road, then the item could also specify more complex geometries such as:

```json
{
  "tender": {
    "items": [
      {
        "id": "item1",
        "deliveryLocations": [
          {
            "geometry": {
              "type": "LineString",
              "coordinates": [
                [
                  102,
                  0
                ],
                [
                  103,
                  1
                ],
                [
                  104,
                  0
                ],
                [
                  105,
                  1
                ]
              ]
            },
            "gazetteer": {
              "scheme": "OSMW",
              "identifiers": [
                "27895985"
              ]
            },
            "description": "St Aldate's",
            "uri": "http://www.geonames.org/2640729/oxford.html"
          }
        ]
      }
    ]
  }
}
```

You can take the contents of the geometry object, excluding the `geometry` keyword, and plug this into any GeoJSON tool to see the shape that is described.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### Unreleased

- Add fields:
  - `Tender.deliveryAddresses`
  - `Tender.deliveryLocations`
  - `Address.description`
- Deprecate the `Item.deliveryAddress` field in favor of the new `Item.deliveryAddresses` field, to support items with multiple delivery addresses
- Deprecate the `Item.deliveryLocation` field in favor of the new `Item.deliveryLocations` field, to support items with multiple delivery locations
- Add "format": "uri" to `Location.uri`
- Update field descriptions to allow location objects to be used in other contexts than deliveries

### v1.1.5

- Remove type information from field descriptions
- Review normative and non-normative words

### v1.1.4

- Disallow `Location.geometry` and `Location.gazetteer` from being null (bug introduced in v1.1.3)
- Correct the order of longitude and latitude in field descriptions to match the GeoJSON specification
- Describe elevation or altitude values
- Remove Sphinx directives from readme
- Update extension.json for Extension Explorer

### v1.1.3

- Disallow `Location.geometry.coordinates` from having null in its array of coordinates
- Disallow `Location.gazetteer.identifiers` from having null in its array of strings
- Correct name of locationGazetteers.csv codelist (was locationGazeteers.csv)
- Allow `Location.geometry` and `Location.gazetteer` to be null
- Add title and description to `Location.gazetteer`
- Add description to `Item.deliveryLocation`, `Item.deliveryAddress`
- Add a `geometryType.csv` codelist for `Location.geometry.type`
- List codelists in extension.json
- Add tests and tidy code
