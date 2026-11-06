# Recurrence

This extension adds fields for information on the recurrence of the contracting process.

"Recurrence" means another contracting process for the same goods, services or works is likely to occur. This is not the same as awarding multiple contracts within a [framework agreement](https://standard.open-contracting.org/latest/en/guidance/map/framework_agreements/).

A company might, for example, use this information to decide to invest in the machinery they would need to compete for the potential future contract.

## Legal context

The [Revised Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) includes: "each notice of intended procurement shall include … c. for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement".

The European Union is a [party](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) to the GPA, and as such its [Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Public contracts — setting out clear ground rules) includes: "Part C: Information to be included in contract notices … 27. In the case of recurrent procurement, estimated timing for further notices to be published."

This extension's fields correspond to [eForms BT-94 (Recurrence) and BT-95 (Recurrence Description)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/).

## Example

```json
{
  "tender": {
    "hasRecurrence": true,
    "recurrence": {
      "dates": [
        {
          "startDate": "2020-01-01T00:00:00Z"
        },
        {
          "startDate": "2021-01-01T00:00:00Z"
        }
      ],
      "description": "The duration of this contract and recurrent contracts will not exceed three years."
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

The original draft extension can be found in the [archived trade profile repository](https://github.com/open-contracting-archive/trade/tree/master/draft_extensions/lot_RecurrentProcurement)
