# Risk allocation

The [framework for disclosure in PPPs](https://thedocs.worldbank.org/en/doc/773541448296707678-0100022015/original/DisclosureinPPPsFramework.pdf) calls for individual risk allocation information.

The risk allocation extension is used to provide structured data on the risk allocations defined in a public private partnership's contract, through a `contracts.riskAllocation` array.

The `riskCategory.csv` codelist is based on the APMG PPP Certification Program. The codelist's Category column indicates the stage or aspect of the contracting process to which the risk category applies.

## Example

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Public Private Partnership Agreement",
      "description": "Public-Private Partnership agreement entered into by and between telecoms promoter, together with national fibre infrastructure and the special purpose vehicle Mega Consortium Ltd",
      "riskAllocation": [
        {
          "id": "1",
          "category": "compliance",
          "description": "Risks deriving from the compliance or lack thereof of regulatory obligations related to the development of the Project",
          "allocation": "privateParty"
        },
        {
          "id": "2",
          "category": "construction",
          "description": "Risks deriving from procurement or lack thereof of the necessary licenses and permits for the Project’s development",
          "allocation": "privateParty"
        },
        {
          "id": "3",
          "category": "construction",
          "description": "Risks arising from the procurement or lack thereof of rights of way required for the Project’s development",
          "allocation": "privateParty"
        }
      ]
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-06-04

- Review normative and non-normative words.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Add `"minLength": 1` on required string fields.

### 2018-05-08

- Make `Risk.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
