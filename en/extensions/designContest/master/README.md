# Design contest

Adds an object to the tender object to describe a design contest.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-704 (Reward and Jury)](https://github.com/eForms/eForms) and [Title III, Chapter II of Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1585836130257&uri=CELEX:32014L0024#d1e6612-65-1). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Examples

```json
{
  "tender": {
    "designContest": {
      "selectedParticipants": [
        {
          "id": "1",
          "name": "Brigitte Hermon"
        },
        {
          "id": "2",
          "name": "Paolo Travino"
        }
      ],
      "hasPrizes": true,
      "prizes": {
        "description": "The winner(s), as well as each unsuccessful competitor who has provided services which meet the program, will receive, subject to the decision of the contracting authority, a prize of EUR 16,500.00 (VAT free)."
      },
      "rewardsDetails": "The payment is made by administrative mandate within 30 days in accordance with the regulations in force.",
      "followUpContracts": true,
      "bindingJuryDecision": true,
      "juryMembers": [
        {
          "name": "Karla Schaffer"
        },
        {
          "name": "Bulat Kazinsky"
        },
        {
          "name": "Alexandra Martinez"
        },
        {
          "name": "Scott MacDougall"
        }
      ]
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_designContest_extension/pulls?q=is%3Apr+is%3Aclosed).
