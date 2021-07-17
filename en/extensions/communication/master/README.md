# Communication

Adds a communication object to the tender to describe the modalities of communication about key events.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-124 and BT-127](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Example

```json
{
  "tender": {
    "communication": {
      "atypicalToolUrl": "https://ecomm-procurement.example.net",
      "futureNoticeDate": "2020-06-17T00:00:00+01:00",
      "documentAvailabilityPeriod": {
        "startDate": "2020-06-15T00:00:00+01:00",
        "endDate": "2020-07-10T00:00:00+01:00"
      }
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2021-01-19

- Add `tender.communication.documentAvailabilityPeriod` field

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_communication_extension/pulls?q=is%3Apr+is%3Aclosed).
