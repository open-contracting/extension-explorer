# Design contest

Adds an object to the tender and lot objects to describe a design contest.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-704 (Reward and Jury) and BG-44 (Prize)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) and [Title III, Chapter II of Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1585836130257&uri=CELEX:32014L0024#d1e6612-65-1). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Examples

A contracting process with a single prize.

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
        "description": "The winner(s) will receive a prize of EUR 3,000.00 (VAT free).",
        "details": [
          {
            "id": "1",
            "value": {
              "amount": 3000,
              "currency": "EUR"
            }
          }
        ]
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

### Lot

A lot with multiple prizes.

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
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
            "details": [
              {
                "id": "1",
                "description": "A lump sum indemnity of an amount identical to that paid to unsuccessful competitors will be paid to the winning team in the form of an advance on the project management contract at the end of the competition; this sum being credited to the amount of fees to be collected subsequently under the project management contract.",
                "value": {
                  "amount": 3000,
                  "currency": "EUR"
                }
              },
              {
                "id": "2",
                "description": "The two competitors (candidates admitted to compete) will receive a maximum fixed compensation of 10,000 EUR excluding tax. For the services provided, subject to the admissibility of their services with regard to the rules of the competition and compliance with the program. Compensation is fixed, in accordance with the provisions of article R. 2172-4 of the public procurement code, the buyer, on the proposal of the jury, reserves the right, in the case of a project that he deems incomplete or whose performances do not comply with the competition rules and/or the programme, to totally or partially cancel the indemnity.",
                "value": {
                  "amount": 10000,
                  "currency": "EUR"
                }
              }
            ]
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
            }
          ]
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-03-10

- Add `lots.designContest` object.
- Add `details` array to `DesignContest.prizes` array, to describe the `id`, `description` and `value` of each prize.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_designContest_extension/pulls?q=is%3Apr+is%3Aclosed).
