# Organization scale

This extension adds a `scale` field to the `parties.details` object, to indicate the size or scale of an organization, in particular commercial enterprises or economic operators.

This information can be used to calculate procurement statistics, like the share of contracts awarded to micro, small and medium-sized enterprises.

The codes in the `partyScale.csv` codelist do not have precise definitions, and instead defer to local laws and regulations, for example:

- [OECD: Small and Medium-Sized Enterprises (SMEs) definition](https://stats.oecd.org/glossary/detail.asp?ID=3123)
- [European Commission: What is an SME?](https://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition_en)

## Guidance

For small and medium-sized enterprises, if you can distinguish between the two sizes, use the 'small' and 'medium' codes. Otherwise, use the 'sme' code.

For self-employed individuals and sole traders, if you can distinguish them from micro enterprises, use the 'selfEmployed' code. Otherwise, use the 'micro' code.

For enterprises without employees, use the 'micro' code.

## Example

```json
{
  "parties": [
    {
      "id": "GB-COH-1234567844",
      "name": "AnyCorp Cycle Provision",
      "details": {
        "scale": "sme"
      }
    }
  ]
}
```

## Changelog

### 2020-05-20

- Add 'selfEmployed' code to the `partyScale.csv` codelist.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-03-11

- Clarify use of codes.

### 2020-03-10

- Add 'small' and 'medium' codes to the `partyScale.csv` codelist.

### 2018-05-22

- Add Description to 'large' code in the `partyScale.csv` codelist.

### 2018-05-21

- Remove '' (blank) code from the `partyScale.csv` codelist.

### 2018-01-09

- Add a `partyScale.csv` codelist to `Organization.details.scale`.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
