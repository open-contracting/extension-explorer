# Sustainability extension

Adds fields to the tender and lot objects, to provide information related to Sustainable Public Procurement (SPP).

## Motivation

To calculate SPP indicators, a user or an application needs to be able to perform the following tasks, using OCDS data:

- Select the contracting processes or individual lots that relate to SPP.
- Select the contracting processes or individual lots that relate to a specific sustainability goal.
- Determine which strategies are being used to promote a sustainability goal, within a contracting process or lot.
- Determine whether a procured item or a supplier has characteristics related to sustainability.

This extension add the fields needed for the above tasks as structured data.

## Guidance

If you know a contracting process or lot is SPP-related, set `hasSustainability` to `true`.

If you know the sustainability goals pursued through the contracting process or lot, then, for each goal, add an entry in its `sustainability` array, from the `sustainabilityGoal.csv` codelist.  This codelist contains codes for broad goals (like 'environmental') and narrower goals (like 'environmental.wasteReduction'). It is an [open codelist](https://standard.open-contracting.org/latest/en/schema/codelists/), such that you can add new codes if no existing code is appropriate.

If you know the strategies used to pursue the sustainability goal(s), then, for each goal, add an entry in the `strategies` array, from the `sustainabilityStrategy.csv` codelist.

## Examples

### `hasSustainability` only

Public Health Wales adopts SPP in a contracting process to design office space and supply furniture.

```json
{
  "tender": {
    "id": "P427",
    "title": "Design of office space and supply of furniture, reusing existing furniture",
    "hasSustainability": true
  }
}
```

If the contracting process is divided into lots, and it is known which lot(s) relate to SPP, set the lot's `hasSustainability` field:

```json
{
  "tender": {
    "lots": [
      {
        "id": "123",
        "hasSustainability": true
      }
    ]
  }
}
```

### The sustainability goal is known

Public Health Wales intends to reduce waste and CO2 emissions as part of a contracting process to design office space and supply furniture.

```json
{
  "tender": {
    "sustainability": [
      {
        "goal": "environmental.wasteReduction"
      },
      {
        "goal": "environmental.carbonEmissionsReduction"
      }
    ]
  }
}
```

If only the broad goal is known, create a single entry using the broad code:

```json
{
  "tender": {
    "sustainability": [
      {
        "goal": "environmental"
      }
    ]
  }
}
```

If the `sustainabilityGoal.csv` codelist contains no appropriate code, create your own code. To create a narrower code, add a period to an existing code, followed by a camelCase word:

```json
{
  "tender": {
    "sustainability": [
      {
        "goal": "environmental.CFCReduction"
      }
    ]
  }
}
```

If there is a description of the sustainability goal:

```json
{
  "tender": {
    "sustainability": [
      {
        "description": "This procurement procedure is aimed at reducing the environmental impact of Public Health Wales office space and furniture."
      }
    ]
  }
}
```

### The strategies are known

Public Health Wales sets SPP-related technical specifications as part of a contracting process to design office space and supply furniture.

```json
{
  "tender": {
    "sustainability": [
      {
        "goal": "environmental.wasteReduction",
        "strategies": [
          "technicalSpecifications"
        ]
      },
      {
        "goal": "environmental.CO2Reduction",
        "strategies": [
          "technicalSpecifications"
        ]
      }
    ]
  }
}
```

If the goal is unknown or is sustainability in general, omit `goal` and set `strategies` only:

```json
{
  "tender": {
    "sustainability": [
      {
        "strategies": [
          "technicalSpecifications"
        ]
      }
    ]
  }
}
```

## Background

This extension uses the [UNEP definition](https://wedocs.unep.org/bitstream/handle/20.500.11822/37045/SPPWSG.pdf) of SPP:

> A process whereby public sector organizations meet their needs for goods, services, works and utilities in a way that achieves value for money on a whole life basis in terms of generating benefits not only to the organization, but also to society and the economy, whilst minimizing, and if possible, avoiding, damage to the environment.

The `sustainabilityGoal.csv` codelist is based on the goals defined in the [OpenSPP toolkit](https://openspp.super.site/what-is-spp-and-open-spp) and the [EU's strategic procurement codelist](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/strategic-procurement).

The `sustainabilityStrategy.csv` codelist is based on the strategies described in the [OpenSPP toolkit](https://openspp.super.site/implement/set-sustainable-criteria) and the [EU's strategic procurement codelist](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/strategic-procurement).

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/1543>.

## Changelog

### 2023-04-12

- Add `Sustainability.description` field.
- Add codes to the `sustainabilityGoal.csv` codelist:
  - 'economic.innovativePurchase'
  - 'economic.processInnovationPromotion'
  - 'economic.productInnovationPromotion'
  - 'economic.researchDevelopmentActivities'
  - 'environmental.biodiversityProtectionRestoration'
  - 'environmental.circularEconomy'
  - 'environmental.circularEconomy'
  - 'environmental.climateChangeMitigation'
  - 'environmental.pollutionPrevention'
  - 'environmental.waterResourcesProtection'
  - 'social.accessibility'
  - 'social.disadvantagedEmploymentOpportunities'
  - 'social.ethnicEquality'
  - 'social.genderEquality'
  - 'social.humanRightsInSupplyChains'
- Add codes to the `sustainabilityStrategy.csv` codelist:
  - 'euGPPCriteria'
  - 'nationalGPPCriteria'
  - 'otherGPPCriteria'
