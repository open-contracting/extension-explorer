# Participation fees

This extension adds a participation fees array to the tender object, to disclose any participation fees for the contracting process.

The `id` field will be required in future versions of the extension.

## Context

There are sometimes costs involved in accessing bidding documents relating to a contracting process, or in otherwise participating in a contracting process. Potential bidders want to know about such fees. Procurement monitors might also want to ensure that participation fees are within legal parameters (often set as a fixed maximum value, or as a percentage of the total contract value) or to monitor how participation fees are being used.

## Example

The following JSON snippet models a contracting process where fees are applied to access bidding documents and to submit bids:

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
        ]
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
        ]
      }
    ]
  }
}
```

## Usage notes

In some cases, a fee can be levied for 'official copies' of procurement documents (although copies can also be available freely online), and bidders might be required to prove that they have paid for an official copy of the documents as part of their submission. In this case, the fee should be modelled as a **submission** fee, as submission is only possible when this document access fee has been paid.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

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
- Add participationFeeType.csv codelist for `ParticipationFee.type`
- Add tests and tidy code
