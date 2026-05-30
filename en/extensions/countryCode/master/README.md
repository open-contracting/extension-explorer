# Country code

Adds a country code field to the address object.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-514 (Organisation Country Code), BT-5141 (Place Country Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "parties": [
    {
      "id": "GB-LAC-E09000003",
      "name": "London Borough of Barnet",
      "address": {
        "streetAddress": "4, North London Business Park, Oakleigh Rd S",
        "locality": "London",
        "region": "London",
        "postalCode": "N11 1NP",
        "countryName": "United Kingdom",
        "country": "GB"
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

If you need to use a [user-assigned code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#User-assigned_code_elements), [create an issue](https://github.com/open-contracting/standard/issues) to discuss its addition to the codelist.

## Changelog

### 2023-02-07

- Rename `countryCode` to `country` to match OCDS 1.2.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_countryCode/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/524>.
