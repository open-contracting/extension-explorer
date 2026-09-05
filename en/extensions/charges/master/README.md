# Charges

The charges extension is used to record details of the **total** charges that are estimated or applied to users or government during the operation of a Public Private Partnership contract.

This can be used to provide a breakdown of **government support** to a project, on a period-by-period basis.

The charges extension introduces a `charges` array to the `contracts.implementation` object.

## Example

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Public Private Partnership Agreement",
      "description": "Public-Private Partnership agreement entered into by and between telecoms promoter, together with national fibre infrastructure and the special purpose vehicle Mega Consortium Ltd",
      "implementation": {
        "charges": [
          {
            "id": "2025-user",
            "title": "User charges for calendar year 2025 resulting from 4G, 3G, voice and SMS tariffs",
            "estimatedValue": {
              "amount": 1019100000,
              "currency": "USD"
            },
            "paidBy": "user",
            "period": {
              "startDate": "2025-01-01T00:00:00Z",
              "endDate": "2025-12-31T23:59:59Z"
            }
          },
          {
            "id": "2026-user",
            "title": "User charges for calendar year 2026 resulting from 4G, 3G, voice and SMS tariffs",
            "estimatedValue": {
              "amount": 1129206411.9632988,
              "currency": "USD"
            },
            "paidBy": "user",
            "period": {
              "startDate": "2026-01-01T00:00:00Z",
              "endDate": "2026-12-31T23:59:59Z"
            }
          }
        ]
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Set `"uniqueItems": true` on array fields, and add `"minLength": 1` on required string fields.

### 2018-05-08

- Make `Charge.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
