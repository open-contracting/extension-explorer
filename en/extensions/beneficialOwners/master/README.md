# Beneficial owners

Adds a beneficial owners array to the organization object to indicate the beneficial owners of an organization.

If beneficial ownership (BO) information is collected via contracting processes, then this extension is appropriate: for example, if tenderers are obligated to disclose their beneficial owners within their bid submission. Similarly, to use this extension, the **laws in your jurisdiction must permit the publication of personal identifiers**.

You can find the complete guidance on publishing personal identifiers in the [Beneficial Ownership Data Standard documentation](https://standard.openownership.org/en/0.3.0/schema/guidance/identifiers.html#shared-identifiers)

On the other hand, if BO information is collected in a central register via other means, then it is recommended to publish that information as a separate dataset. The BO dataset and the OCDS dataset should [identify organizations](https://standard.open-contracting.org/latest/en/schema/identifiers/#organization-ids) in the same way, so that users can cross-reference the datasets. The BO dataset can follow the [Beneficial Ownership Data Standard](https://standard.openownership.org/en/latest/).

## Example

### With nationality

The beneficial owner's nationality is disclosed.

```json
{
  "parties": [
    {
      "id": "AHL",
      "name": "Alpha Holdings Ltd",
      "beneficialOwners": [
        {
          "id": "1",
          "name": "Juan Perez",
          "identifier": {
            "scheme": "PRY-IDCARD",
            "id": "12345"
          },
          "nationalities": [
            "PY"
          ],
          "address": {
            "streetAddress": "Avenida Eusebio Ayala 1347",
            "locality": "Asunción",
            "region": "Gran Asunción",
            "postalCode": "1001",
            "countryName": "Paraguay"
          },
          "email": "jperez@example.com",
          "faxNumber": "+595210000001",
          "telephone": "+595210000000"
        }
      ]
    }
  ]
}
```

### Without nationality

The beneficial owner's nationality is not disclosed because the organization is listed on a regulated market (e.g. a stock exchange) that ensures adequate transparency in line with anti-money laundering legislation.

```json
{
  "parties": [
    {
      "id": "AHL",
      "name": "Alpha Holdings Ltd",
      "beneficialOwners": [
        {
          "id": "1",
          "name": "Juan Perez",
          "identifier": {
            "scheme": "PRY-IDCARD",
            "id": "12345"
          },
          "address": {
            "streetAddress": "Avenida Eusebio Ayala 1347",
            "locality": "Asunción",
            "region": "Gran Asunción",
            "postalCode": "1001",
            "countryName": "Paraguay"
          },
          "email": "jperez@example.com",
          "faxNumber": "+595210000001",
          "telephone": "+595210000000"
        }
      ],
      "details": {
        "listedOnRegulatedMarket": true
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-08-04

- Replace `nationality` string with `nationalities` array.

### 2023-06-07

- Add a `country.csv` codelist for `nationality`.

### 2023-02-27

- Add fields:
  - `Person.address`
  - `Person.email`
  - `Person.faxNumber`
  - `Person.telephone`
  - `Organization.details.listedOnRegulatedMarket`
