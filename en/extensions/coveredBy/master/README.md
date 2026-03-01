# Covered By

This extension adds a field to indicate the international legal instruments that the contracting process is covered by.

For example, the Agreement on Government Procurement (GPA) is a treaty that requires members to indicate whether a contracting process is covered by it. The Clean Vehicles Directive is a legal act that provides for member states of the European Union to indicate associated information in procurement notices. The `coveredBy` field should be used to meet such requirements.

To disclose the laws or regulations that govern the contracting process and that grant legal authority to the procuring entity, use the [legalBasis extension](https://github.com/open-contracting-extensions/ocds_legalBasis_extension) instead.

## Guidance

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

If you need to refer to a treaty that is not in the `coveredBy` codelist:

1. If the treaty has a national or subnational scope, pick a relevant [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g "CA" for Canada).
1. If the treaty has a subnational scope, pick a relevant [ISO 3166-2 region code](https://en.wikipedia.org/wiki/ISO_3166-2) (e.g "NT" for [Northern Territories](https://en.wikipedia.org/wiki/ISO_3166-2:CA#Current_codes), a province of Canada).
1. Concatenate the code(s) to the acronym of the treaty, separating each part with a dash (e.g "CA-NT-BIP").
1. Add this code to the `coveredBy` array.
1. Document the new code (see [Extending open codelists](https://standard.open-contracting.org/latest/en/schema/codelists/)).

## Legal context

The [Revised Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) includes: "each notice of intended procurement shall include … l. an indication that the procurement is covered by this Agreement."

The European Union is a [party](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) to the GPA, and as such its [Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Public contracts — setting out clear ground rules) includes: "Part C: Information to be included in contract notices … 29. Indication whether the contract is covered by the GPA."

## Example

The `coveredBy` field is an array of strings, whose values are selected from the `coveredBy.csv` open codelist.

### Tender

```json
{
  "tender": {
    "coveredBy": [
      "GPA"
    ]
  }
}
```

### Lot

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "coveredBy": [
          "EU-CVD"
        ]
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2024-10-08

- Add 'EU-FSR' code to the `coveredBy` codelist.

### 2024-02-07

- Add 'CPTPP' code to the `coveredBy` codelist.

### 2023-03-02

- Add 'EU-CVD' code to the `coveredBy` codelist.
- Add `coveredBy` to the `Lot` object.

### 2020-11-04

- Add guidance on the creation of new codes for the `coveredBy` codelist.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.
