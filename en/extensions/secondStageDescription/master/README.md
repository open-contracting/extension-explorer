# Second stage description

Adds a second stage object to the tender and lot objects, to describe the second stage of a two-stage procedure. In particular, it adds two fields to describe the limits on the number of candidates to be invited.

## Guidance

If there is an exact limit on the number of candidates, set `minimumCandidates` and `maximumCandidates` to the same number.

If `maximumCandidates` is set, use the selection criteria extension (TBD) to describe how the selection criteria will be used to select candidates to be invited for the second stage.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-709 (Second Stage)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "secondStage": {
          "minimumCandidates": 5,
          "maximumCandidates": 50,
          "successiveReduction": true,
          "noNegotiationNecessary": false,
          "invitationDate": "2019-08-16T10:30:00Z"
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_secondStageDescription_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/695>.
