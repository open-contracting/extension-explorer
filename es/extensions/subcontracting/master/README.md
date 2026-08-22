# Subcontratación

Adds objects for information about the terms governing subcontracting and the parts of the contract that tenderers and suppliers will subcontract to third parties.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#usage) on whether to use `tender.lots` fields or `tender` fields.

Si el porcentaje del valor del contrato que se subcontrata es un número exacto y no un rango, establecer `minimumPercentage` y `maximumPercentage` al mismo número.

## Contexto legal

In the European Union, this extension's fields correspond to [article 21 of directive 2009/81/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009L0081&from=EN#d1e2623-76-1) and the [eForms business terms](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) in BG-180 (Subcontracting) and BG-711 (Contract Terms).

For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

TED XML schema R2.0.9 models the minimum and maximum percentages of the contract value that the contractor needs to subcontract as part of each award for *F15: Voluntary ex ante transparency notice*. eForms XML models these as part of each lot. As such, different fields ought to be used when implementing each profile.

## Ejemplos

### Tender and awards

Information about the terms governing subcontracting is disclosed at the tender and award stages, and information about the parts of the contract that the supplier will subcontract is disclosed at the award stage.

```json
{
  "tender": {
    "subcontractingTerms": {
      "description": "The successful tenderer is obliged to specify which part or parts of the contract it intends to subcontract beyond the required percentage and to indicate the subcontractors already identified."
    }
  },
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
        "minimumPercentage": 0.3,
        "maximumPercentage": 0.3,
        "competitiveMinimumPercentage": 0.1,
        "competitiveMaximumPercentage": 0.25,
        "description": "The painting and electricity tasks are subcontracted."
      }
    }
  ]
}
```

### Lots and bids

Information about the terms governing subcontracting is disclosed per lot at the tender stage, and information about the parts of the contract that the tenderer will subcontract is disclosed at the bid stage.

```json
{
  "parties": [
    {
      "id": "ORG-0005",
      "roles": [
        "tenderer"
      ]
    },
    {
      "id": "ORG-0012",
      "roles": [
        "subcontractor"
      ]
    }
  ],
  "tender": {
    "lots": [
      {
        "id": "1",
        "subcontractingTerms": {
          "description": "The contractor must subcontract a minimum percentage of the contract using the procedure set out in Title III of Directive 2009/81/EC.",
          "competitiveMinimumPercentage": 0.255,
          "competitiveMaximumPercentage": 0.455
        }
      }
    ]
  },
  "bids": {
    "details": [
      {
        "id": "1",
        "hasSubcontracting": true,
        "subcontracting": {
          "description": "The subcontracting will be...",
          "value": {
            "amount": 9999999.99,
            "currency": "EUR"
          },
          "minimumPercentage": 0.3,
          "maximumPercentage": 0.3,
          "subcontracts": [
            {
              "id": "1",
              "subcontractor": {
                "id": "ORG-0012",
                "name": "Company ABC"
              },
              "mainContractors": [
                {
                  "id": "ORG-0005",
                  "name": "Tendering Company Ltd"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-12-04

- Update field descriptions:
  - `SubcontractingTerms.competitiveMaximumPercentage`
  - `SubcontractingTerms.competitiveMinimumPercentage`
  - `Subcontracting.competitiveMaximumPercentage`
  - `Subcontracting.competitiveMinimumPercentage`
  - `Subcontracting.maximumPercentage`
  - `Subcontracting.minimumPercentage`

### 2023-05-22

- Add fields for eForms:
  - `Bid.hasSubcontracting`
  - `Bid.subcontracting`
  - `SubcontractingTerms.competitiveMaximumPercentage`
  - `SubcontractingTerms.competitiveMinimumPercentage`
  - `Subcontracting.subcontracts`
- Update field descriptions to allow the `Subcontracting` object to be used in the context of bids:
  - `Subcontracting`
  - `Subcontracting.description`
  - `Subcontracting.value`
- Add 'subcontractor' code to the `+partyRole.csv` codelist patch.

### 2022-07-18

- Add `Lot.subcontractingTerms` field.

### 2020-10-07

- Rename `Tender.subcontracting` to `subcontractingTerms`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) y en [pull requests](https://github.com/open-contracting-extensions/ocds_subcontracting_extension/pulls?q=is%3Apr+is%3Aclosed). También puede ver discusiones sobre esta extensión en [este issue](https://github.com/open-contracting-extensions/ocds_subcontracting_extension/issues/2).
