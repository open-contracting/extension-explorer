# Shareholders

Adds company ownership fields to the organization object used in the parties array.

For example, when bidding in Public Private Partnerships, companies can be required to disclose their ownership information. After a contract is signed and during project implementation, the ownership information of the Special Purpose Vehicle (SPV) that is operating the contract might need to be updated.

Since each owner mentioned in the `shareholders` array should have a corresponding entry in the `parties` array, it is possible to use this extension to describe multiple levels of corporate ownership.

## Example

```json
{
  "parties": [
    {
      "id": "MEGA",
      "name": "Mega Consortium",
      "shareholders": [
        {
          "id": "1",
          "shareholder": {
            "id": "AHL",
            "name": "Alpha Holdings Ltd"
          },
          "shareholding": 0.67,
          "votingRights": "additional",
          "votingRightsDetails": "Alpha Holdings Ltd. is entitled to 5 votes per share.",
          "notes": "Alpha Holdings Ltd. must maintain a minimum shareholding of 30% in the project company until 10 years from the date of commissioning have elapsed."
        },
        {
          "id": "2",
          "shareholder": {
            "id": "BET",
            "name": "Beta Investment Company Ltd"
          },
          "shareholding": 0.33,
          "votingRights": "ordinary"
        }
      ]
    },
    {
      "id": "BET",
      "name": "Beta Investment Company Ltd"
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-12-04

- Update and clarify `Shareholder.shareholding` field description.

### 2021-05-24

- Remove `Organization.beneficialOwnership`.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Add `"minLength": 1` on required string fields.
- Make `Organization.beneficialOwnership` non-nullable (undo earlier change).

### 2018-05-08

- Make `Shareholder.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-01-29

- Make `Organization.beneficialOwnership` nullable.
