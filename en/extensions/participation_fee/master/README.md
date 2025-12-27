# Participation fees

This extension adds a participation fees array to the tender object, to disclose any participation fees for the contracting process.

There are sometimes costs involved in accessing bidding documents relating to a contracting process, or in otherwise participating in a contracting process. Potential bidders want to know about such fees. Procurement monitors might also want to ensure that participation fees are within legal parameters (often set as a fixed maximum value, or as a percentage of the total contract value) or to monitor how participation fees are being used.

## Guidance

The `id` field will be required in future versions of the extension.

In some cases, a fee is levied for official copies of procurement documents, with unofficial copies being freely available. Bidders might be required to prove that they have paid for official copies as part of their submission. In such cases, the fee should use the 'submission' code in the `type` field, rather than the 'document' code.

## Examples

A contracting process where fees are applied to access bidding documents and to submit bids:

```json
{
  "tender": {
    "participationFees": [
      {
        "id": "1",
        "type": [
          "document"
        ],
        "value": {
          "currency": "GBP",
          "amount": 8.0
        },
        "description": "Fee payable for both soft and hard copies of documents.",
        "methodOfPayment": [
          "wireTransfer",
          "cheque"
        ],
        "payee": {
          "id": "ORG-0001",
          "name": "Highway Division"
        },
        "paymentAddress": {
          "locality": "Jawali",
          "region": "Himachal Pradesh",
          "countryName": "India"
        }
      },
      {
        "id": "2",
        "type": [
          "submission"
        ],
        "value": {
          "currency": "GBP",
          "amount": 10.0
        },
        "description": "Fee payable within e-procurement system.",
        "methodOfPayment": [
          "wireTransfer"
        ],
        "payee": {
          "id": "ORG-0001",
          "name": "Highway Division"
        }
      }
    ]
  }
}
```

A participation fee of 5% of the award value, payable by the winning bidder:

```json
{
  "tender": {
    "participationFees": [
      {
        "id": "1",
        "type": [
          "win"
        ],
        "relativeValue": {
          "proportion": 0.05,
          "monetaryValue": "award"
        },
        "description": "Fee payable on acceptance of award.",
        "methodOfPayment": [
          "wireTransfer",
          "cheque"
        ]
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### Unreleased

- Make `ParticipationFee.id` required so that participation fees are merged by identifier
- Add fields:
  - `relativeValue`
  - `payee`
  - `paymentAddress`

### v1.1.5

- Add `id` field to example in readme
- Fix description of `ParticipationFee.type` field
- Merge and reconcile field and code descriptions with schema and codelist
- Remove indication of fields as "optional"
- Add `methodOfPayment` codelist from [paymentMethod extension](https://github.com/INAImexico/ocds_paymentMethod_extension/blob/master/codelists/paymentMethod.csv)
- Remove type information from field descriptions
- Review normative and non-normative words

### v1.1.4

- Update `mergeStrategy` property to `wholeListMerge` property
- Update extension.json for Extension Explorer

### v1.1.3

- Disallow `ParticipationFee.type` from having null in its array of strings
- Allow `ParticipationFee.description` to be null
- Add `ParticipationFee.id` field
- Add description to `ParticipationFee`
- Add title and description to `ParticipationFee.value`
- Add a `participationFeeType.csv` codelist for `ParticipationFee.type`
- Add tests and tidy code
