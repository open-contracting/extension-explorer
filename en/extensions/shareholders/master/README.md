# Shareholder details

The shareholder extension can be used to provide details of the owners of parties involved in a contracting process.

For example, in Public Private Partnerships processes, companies are often required to disclose information on their ownership structures when bidding, and when the contract is awarded, information on the ownership of a Special Purpose Vehicle (SPV) operating the contract may need to be kept up to date during project implementation.

Because each owner mentioned in the shareholders array should also gain an entry in the `parties` array, it is possible to use this extension to build up information on corporate ownership networks involved in a contracting process.

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

### 2021-05-24

- Remove `Organization.beneficialOwnership`.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Add `"minLength": 1` on required string fields.
- Make `Organization.beneficialOwnership` non-nullable (undo earlier change).

### 2018-05-08

- Make `Shareholder.id` required to support revision tracking and [list merging](http://standard.open-contracting.org/latest/en/schema/merging/#lists)

### 2018-01-29

- Make `Organization.beneficialOwnership` nullable.
