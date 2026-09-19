# Techniques

Adds fields to the tender, lot and lot group objects to describe the use of techniques, such as framework agreements, dynamic purchasing systems and electronic auctions. Also, adds a field to the tender object in a framework agreement call-off to indicate if it is competitive or direct.

## Guidance

### Framework agreement's `value` and `period`

The `value` and `period` fields of `FrameworkAgreement` objects should only be used if a data source provides values and periods for both the contract/lot and the framework agreement, like TED XML Schema R2.08. Otherwise:

- If a procurement isn't divided into lots, use the `tender.value` and `tender.contractPeriod` fields.
- If a procurement is divided into lots, use the `value` and `contractPeriod` fields of `Lot` objects.

### Framework agreement's `method`

Here are the possible values for a framework agreement's `method` field, and common synonyms:

- withoutReopeningCompetition: call-offs
- withReopeningCompetition: mini-competitions
- withAndWithoutReopeningCompetition: call-offs and mini-competitions

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-706 (Techniques), BG-157 (Group Framework Maximum Value and BT-271 (Framework Maximum Value)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Examples

### Framework agreement

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasFrameworkAgreement": true,
          "frameworkAgreement": {
            "minimumParticipants": 2,
            "maximumParticipants": 100,
            "method": "withoutReopeningCompetition",
            "periodRationale": "<A good justification>",
            "buyerCategories": "all hospitals in the Tuscany region",
            "value": {
              "amount": 240000,
              "currency": "EUR"
            },
            "period": {
              "durationInDays": 730
            },
            "description": "Call offs are estimated to be organized every 3 months, with an average value of 60,000 euros per contract."
          }
        }
      }
    ]
  }
}
```

### Dynamic purchasing system

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasDynamicPurchasingSystem": true,
          "dynamicPurchasingSystem": {
            "type": "closed",
            "status": "active"
          }
        }
      }
    ]
  }
}
```

### Electronic auction

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasElectronicAuction": true,
          "electronicAuction": {
            "url": "https://example.com/auction/1",
            "description": "<Any relevant details>"
          }
        }
      }
    ]
  }
}
```

### Direct call-off

```json
{
  "tender": {
    "id": "2421-1016-CM20",
    "procuringEntity": {
      "name": "I.MUNICIPALIDAD DE CONCEPCION | DIRECCION DE SALUD MUNICIPAL DE CONCEPCION",
      "id": "CL-MP-3413"
    },
    "competitive": false
  },
  "awards": [
    {
      "id": "42133251",
      "title": "JERINGAS DAS CONCEPCION",
      "description": "2239-16-LR15 Órtesis, Prótesis, Endoprótesis e Insumos de Salud. FINANCIAMIENTO: 215.22.04.005.001 SP 28 SE SOLICITA LA ACEPTACIÓN DE ESTA ORCOM A TRAVÉS DE LA PLATAFORMA MERCADO PUBLICO ANTES DE REALIZAR LA ENTREGA DEL BIEN O SERVICIO",
      "status": "active",
      "date": "2020-06-23T15:40:44Z",
      "value": {
        "amount": 7526475.0,
        "currency": "CLP"
      },
      "suppliers": [
        {
          "name": "Tecnika S.A. | Tecnika S.A.",
          "id": "CL-MP-27291"
        }
      ],
      "items": [
        {
          "id": "111570611",
          "description": "Aparatos de inyección hipodérmica o accesorios(1391678 )JERINGA HIPODERMICA CONTROLADA VENOTEK 10ML LUER LOCK CON AGUJA 21GX1 1/2 100 UNIDADES 1418179",
          "quantity": 500.0,
          "unit": {
            "value": {
              "amount": 4228.0,
              "currency": "CLP"
            }
          }
        }
      ]
    }
  ],
  "relatedProcesses": [
    {
      "id": "1",
      "relationship": [
        "framework"
      ],
      "title": "Órtesis, Prótesis, Endoprótesis e Insumos de Salud",
      "scheme": "ocid",
      "identifier": "ocds-70d2nz-2239-16-LR15"
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-06-07

- Merge the [Competitive](https://github.com/open-contracting-extensions/ocds_competitive_extension) extension.
- Add `LotGroup.techniques` field.

### 2020-10-05

- Add fields:
  - `FrameworkAgreement.minimumParticipants`
  - `FrameworkAgreement.value`
  - `FrameworkAgreement.period`
  - `FrameworkAgreement.description`

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues), in [pull requests](https://github.com/open-contracting-extensions/ocds_techniques_extension/pulls?q=is%3Apr+is%3Aclosed) and in <https://github.com/open-contracting/standard/issues/695>.
