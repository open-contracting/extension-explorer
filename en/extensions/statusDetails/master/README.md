# Status Details

In some cases, it is important to preserve the local name of the status in which the tender, award or contract are. This extension adds the field `statusDetails` to the tender, award and contract objecs, in order to provide the local name of the particular status used.

## Examples

```json
{
  "tender": {
    "id": "tender-1",
    "status": "complete",
    "statusDetails": "Adjudicado"
  },
  "awards": [
    {
      "id": "award-1",
      "status": "active",
      "statusDetails": "Adjudicado"
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "awardID": "award-1",
      "status": "active",
      "statusDetails": "Adjudicado"
    }
  ]
}
```

An example of `contract.statusDetails` reflecting a court order:

```json
{
  "tender": {
    "id": "tender-1",
    "status": "complete"
  },
  "awards": [
    {
      "id": "award-1",
      "status": "active"
    }
  ],
  "contracts": [
    {
      "id": "contract-1",
      "awardID": "award-1",
      "status": "active",
      "statusDetails": "Suspended as a result of a court order."
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2021-01-11

- Add example of `contract.statusDetails` reflecting a court order.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/764>.
