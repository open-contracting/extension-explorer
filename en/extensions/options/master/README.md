# Options

This extension adds fields to indicate whether options are used and other information about options.

A buyer may have a right – but not an obligation – to additional purchases from a supplier while the contract is valid.

For example, a contract may concern a thousand uniforms, and the buyer may have the option to request an additional hundred uniforms. This might occur if the buyer doesn't yet know whether a planned increase in staff will take place.

## Legal context

The [Revised Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) includes: "each notice of intended procurement shall include … d. a description of any options".

The European Union is a [party](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) to the GPA, and as such its [Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Public contracts — setting out clear ground rules) includes: "Part C: Information to be included in contract notices … 7. … Where appropriate, description of any options."

## Example

```json
{
  "tender": {
    "hasOptions": true,
    "options": {
      "description": "The buyer has the option to buy an additional hundred uniforms.",
      "period": {
        "durationInDays": 180
      }
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2024-05-02

- Add fields:
  - `Award.hasOptions`
  - `Award.options`
  - `Contract.hasOptions`
  - `Contract.options`
- Clarify the description of `Tender.hasOptions` and `Lot.hasOptions`.

### 2020-10-06

- Add `Options.period` field.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_options_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/691>.
