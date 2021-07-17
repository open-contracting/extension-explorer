# Risk allocation

The [framework for disclosure in PPPs](http://pubdocs.worldbank.org/en/773541448296707678/Disclosure-in-PPPs-Framework.pdf) calls for individual risk allocation information.

The risk allocation extension is used to provide structured data on the risk allocations defined in a public private partnership's contract.

## Overview

Risk allocations can be represented using an array of `Risk` objects in the `riskAllocation` field of the `contracts` section of an OCDS release.

The risk category can be represented using the `Risk.category` field using values from the `riskCategory.csv` codelist based on the APMG PPP Certification Program. The codelist's Category column indicates the stage or aspect of the contracting process to which the risk category applies.

The party retaining each risk should be represented using the `Risk.allocation` field using values from the `riskAllocation.csv` codelist.

The description of the risk should be provided as free text using the `Risk.description` field.

Additional free text information on the risk can be provided using the `Risk.notes` field.

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

- Make `Risk.id` required to support revision tracking and [list merging](http://standard.open-contracting.org/latest/en/schema/merging/#lists)
