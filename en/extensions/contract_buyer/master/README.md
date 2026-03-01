# Buyer per award or contract

Adds buyer fields to the award and contract objects to indicate the buyer(s) for an individual award or contract, if different from the buyer(s) involved in the contracting process as a whole.

OCDS indicates the (lead) buyer in a contracting process with the `buyer` field. If a contracting process involves multiple buyers, each buyer can be added to the `parties` array with a 'buyer' role.

However, in some cases, for a given award, a subset of the buyers decide on the supplier and sign the contract. **Only use this extension in such cases.**

## Legal context

In the European Union, this extension's fields correspond to [eForms OPT-300-Contract-Signatory](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Example

### Contracts

Two contracts are issued with a different buyer for each.

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "buyer": {
        "name": "Example Department of Transport",
        "id": "GB-GOV-00000000"
      }
    },
    {
      "id": "2",
      "awardID": "2",
      "buyer": {
        "name": "Example Department of Education",
        "id": "GB-GOV-12345678"
      }
    }
  ]
}
```

### Awards

One award is issued with two buyers.

```json
{
  "awards": [
    {
      "id": "1",
      "buyers": [
        {
          "name": "Example Department of Education",
          "id": "GB-GOV-12345678"
        },
        {
          "name": "Example Department of Transport",
          "id": "GB-GOV-00000000"
        }
      ]
    }
  ]
}
```

## Changelog

### 2023-04-12

- Add `awards.buyers` field.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
