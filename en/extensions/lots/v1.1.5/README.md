# Lots

When a single tender is broken down into parts that can be bid upon, and awarded, separately, this is modelled using the **lots extension**.

The lots extension maintains the overall structure of an OCDS release, with items, documents and milestones nested immediately within `tender`, `awards` and `contracts` sections, but it introduces an array of Lots in the `tender` section, and the ability to cross-reference a specific `relatedLot` for each item, and an array of `relatedLots` for documents, milestones and awards.

The `lotDetails` and `lotGroups` sections allow more complex conditions around the award of lots to be expressed, such as the maximum value of a group of lots.

This means that systems which are not 'lot aware' can still understand the overall value of contracting taking place, key events, and relationships between buyers and suppliers. At the same time, 'lot aware' systems can make use of the cross-referenced information to present a lot-centric view on the information to users, or to analyze contracting lot by lot.

## Related Lot

The `relatedLot` (singular) property is available for:

- items

An array of `relatedLots` (plural) can be provided for each of:

- documents
- milestones
- awards

In other extensions, the following objects can also declare related lots:

- bids submitted by tenderers (`Bid`), in the [bid extension](https://github.com/open-contracting-extensions/ocds_bid_extension)
- sources of finance (`Finance`), in the [finance extension](https://github.com/open-contracting-extensions/ocds_finance_extension)

When lots are used, **all** items should have a `relatedLot` field.

Documents and milestones may have a `relatedLots` field. Those without this field ought to be interpreted as applicable to the tender as a whole.

The items within an award should have a `relatedLot` field. Publishers may also reference all the lots an award relates to at the award level using `relatedLots`.

## How to set `tender.status` if lots' statuses differ?

`tender.status` and `Lot.status` use the closed tenderStatus.csv codelist. This codelist progresses from planning statuses ('planning', 'planned'), to 'active' status, and then result statuses ('complete', 'cancelled', 'unsuccessful').

- If any lot's status is 'active', then `tender.status` should be 'active', to indicate that some lots are awaiting results.
- If all lots' status are a result status, then `tender.status` describes the aggregate result:
  - If at least one lot's status is 'complete', then `tender.status` should be 'complete', to indicate that there is at least one award.
  - Otherwise, if at least one lot's status is 'unsuccessful', then `tender.status` should be 'unsuccessful', to indicate that the procedure was completed but unsuccessfully.
  - Otherwise, If all lots' status are 'cancelled', then `tender.status` should be 'cancelled', to indicate that the procedure was discontinued as a whole.

## Example

A tender is issued for consultancy in the development of a new public building. This might include items for:

- Architectural design
- Architectural advisory services
- Civil engineering consultancy
- Structural engineering consultancy

Although part of the same tender, the buyer is willing to award these different items to different firms, and so divides the tender into three lots.

```json
{
  "tender": {
    "items": [
      {
        "id": "0001",
        "description": "Architectural advice",
        "classification": {
          "scheme": "CPV",
          "id": "71210000",
          "description": "Advisory architectural services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0002",
        "description": "Architectural design",
        "classification": {
          "scheme": "CPV",
          "id": "71220000",
          "description": "Architectural design services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0003",
        "description": "Civil engineering consultant",
        "classification": {
          "scheme": "CPV",
          "id": "71311000",
          "description": "Civil engineering consultancy services"
        },
        "relatedLot": "lot-2"
      },
      {
        "id": "0004",
        "description": "Structural engineering services",
        "classification": {
          "scheme": "CPV",
          "id": "71312000",
          "description": "Structural engineering consultancy services"
        },
        "relatedLot": "lot-3"
      }
    ],
    "value": {
      "amount": 1200000,
      "currency": "GBP"
    },
    "lots": [
      {
        "id": "lot-1",
        "title": "Architectural services",
        "description": "For architectural services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 200000
        },
        "contractPeriod": {
          "startDate": "2020-10-10T00:00:00Z",
          "endDate": "2021-11-10T00:00:00Z"
        }
      },
      {
        "id": "lot-2",
        "title": "Civil engineering services",
        "description": "For civil engineering services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 400000
        },
        "contractPeriod": {
          "startDate": "2020-12-10T00:00:00Z",
          "endDate": "2021-12-10T00:00:00Z"
        }
      },
      {
        "id": "lot-3",
        "title": "Structural engineering",
        "description": "For structural engineering consultancy delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 600000
        },
        "contractPeriod": {
          "startDate": "2021-02-10T00:00:00Z",
          "endDate": "2022-02-10T00:00:00Z"
        }
      }
    ],
    "lotGroups": [
      {
        "id": "lot-group-1",
        "relatedLots": [
          "lot-2",
          "lot-3"
        ],
        "optionToCombine": true,
        "maximumValue": {
          "currency": "GBP",
          "amount": 1000000
        }
      }
    ],
    "lotDetails": {
      "maximumLotsBidPerSupplier": 4,
      "maximumLotsAwardedPerSupplier": 2,
      "awardCriteriaDetails": "Percentage of people aggregated nationwide contestants undertake to cover, as indicated in their Economic Bids. The evaluation of proposals will be conducted based on the provisions of Article Y of the law on public private partnerships, and the provisions of the tender rules, performing in a first stage an evaluation of the technical bids and subsequently an assessment of the financial offer of the participants."
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### v1.1.5

- Add `tender.lotDetails.awardCriteriaDetails` field
- Add `Finance.relatedLots` field
- Add `Lot.contractPeriod` field
- Remove type information from field descriptions
- Review normative and non-normative words

### v1.1.4

- Disallow `Tender.lotDetails` from being null (bug introduced in first release)
- `Tender.lotDetails` no longer uses a `$ref` to a `LotDetails` definition
- Remove Sphinx directives from readme
- Update extension.json for Extension Explorer

### v1.1.3

- Disallow `relatedLots` fields from having null in their arrays of strings
- Add enum to `Lot.status`
- Allow `relatedLots` fields to be null
- Add title and description to `Tender.lotDetails`
- Use Apache 2.0 License
- Add tests and tidy code
