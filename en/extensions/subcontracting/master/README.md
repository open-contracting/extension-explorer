# Subcontracting

Adds an object for information about the parts of the contract that the supplier will subcontract to third parties.

## Guidance

If the percentage of the contract value that is subcontracted is an exact number and not a range, set `minimumPercentage` and `maximumPercentage` to the same number.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-709 (Second Stage), BT-65, BT-64, BT-729](https://github.com/eForms/eForms) and [article 21 of directive 2009/81/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009L0081&from=EN#d1e2623-76-1). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Examples

```json
{
  "tender": {
    "subcontractingTerms": {
      "description": "The successful tenderer is obliged to specify which part or parts of the contract it intends to subcontract beyond the required percentage and to indicate the subcontractors already identified."
    }
  }
}
```

```json
{
  "awards": [
    {
      "id": "1",
      "hasSubcontracting": true,
      "subcontracting": {
        "competitive": true,
        "value": {
          "amount": 28000,
          "currency": "EUR"
        },
        "description": "The painting and electricity tasks are subcontracted."
      }
    }
  ]
}
```

```json
{
  "awards": [
    {
      "id": "1",
      "hasSubcontracting": true,
      "subcontracting": {
        "minimumPercentage": 0.3,
        "maximumPercentage": 0.3,
        "description": "The painting and electricity tasks are subcontracted."
      }
    }
  ]
}
```

```json
{
  "awards": [
    {
      "id": "1",
      "hasSubcontracting": true,
      "subcontracting": {
        "competitiveMinimumPercentage": 0.1,
        "competitiveMaximumPercentage": 0.25,
        "description": "The painting and electricity tasks are subcontracted."
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-10-07

- Rename the `subcontracting` field in the `Tender` object to `subcontractingTerms`.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_subcontracting_extension/pulls?q=is%3Apr+is%3Aclosed). You can also see discussions about this extension in [this issue](https://github.com/open-contracting-extensions/ocds_subcontracting_extension/issues/2).
