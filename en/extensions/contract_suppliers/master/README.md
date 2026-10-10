# Contract Suppliers

OCDS is designed around a contracting model in which:

- One or more awards are made naming the selected suppliers;
- One contract is signed for each award made, referring back to the related award;

For this reason, the core `Contract` block does not include information on `suppliers`. These can be located by looking at the related `Award` using the `awardID` cross-reference.

However, there are some contracting processes in which a single award to multiple suppliers, results in multiple contracts, each to a single supplier. In these instances, it is important to specify suppliers at the contract level.

The Contract Suppliers extension introduces a `contracts.suppliers` array for this purpose.

## Example

An award is made to a consortium with multiple suppliers. Then, a contract is signed with each of them separately. When this extension is used, you should fill `contracts.items` and `contracts.value` with the awarded items and value for each supplier.

```json
{
  "awards": [
    {
      "id": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 100000,
        "currency": "GBP"
      },
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 10,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ],
      "suppliers": [
        {
          "id": "GB-COH-1234567844",
          "name": "AnyCorp Cycle Provision"
        },
        {
          "id": "GB-COH-789456123",
          "name": "OtherCorp"
        }
      ]
    }
  ],
  "contracts": [
    {
      "id": "ocds-213czf-000-00001-contract-01",
      "awardID": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 70000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "GB-COH-1234567844",
          "name": "AnyCorp Cycle Provision"
        }
      ],
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 7,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ]
    },
    {
      "id": "ocds-213czf-000-00001-contract-02",
      "awardID": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 30000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "GB-COH-789456123",
          "name": "OtherCorp"
        }
      ],
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 3,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ]
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.
