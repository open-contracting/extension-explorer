# Contract level buyer information

## Background

The core OCDS schema provides space for a single `buyer` to be described for each contracting process. The buyer is defined as the organizations whose funds are directly used for the purchase of the goods, works or services described in the contract.

However, some forms of contracting process, such as framework agreements, may result in multiple contracts, with each contract signed by a different buyer.

This extension provides a way to provide `buyer` information on a per contract basis.

## Extension fields

This extension adds a `buyer` property to the `contracts` section of OCDS.

`contracts.buyer` is an `OrganizationReference` consisting of the following fields:

- `name` - The name of the party being referenced. This must match the name of an entry in the `parties` section.
- `id` - The id of the party being referenced. This must match the id of an entry in the `parties` section.

## Dependencies

This extension is only valid from OCDS Version 1.1, as it makes use of the updated organization reference approach.

## Example

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

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
