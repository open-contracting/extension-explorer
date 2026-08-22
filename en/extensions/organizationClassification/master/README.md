# Organization classification

Adds an array of classification objects to an organization's details, in order to categorize it.

## Examples

An organization categorized as a social protection business.

```json
{
  "parties": [
    {
      "id": "1",
      "details": {
        "classifications": [
          {
            "id": "10",
            "scheme": "TED_CA_ACTIVITY",
            "description": "Social protection"
          }
        ]
      }
    }
  ]
}
```

An organization classified as a women-owned small business by the Small Business Administration in the USA.

```json
{
  "parties": [
    {
      "id": "1",
      "details": {
        "classifications": [
          {
            "id": "WOSB",
            "scheme": "USA-SBA",
            "description": "Woman-Owned Small Business",
            "uri": "https://www.ecfr.gov/current/title-13/chapter-I/part-127/subpart-B"
          }
        ]
      }
    }
  ]
}
```

For a longer example, see the [organization classifications](https://standard.open-contracting.org/latest/en/guidance/map/organization_classifications/#example-2-2-disclosing-data-using-a-local-scheme) guidance in the OCDS documentation.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2024-05-22

- Add 'eu-buyer-legal-type' code to the `+itemClassificationScheme.csv` codelist patch.

### 2023-08-01

- Add 'eu-buyer-contracting-type' and 'eu-main-activity' codes to the `+itemClassificationScheme.csv` codelist patch.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_organizationClassification_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/711>.
