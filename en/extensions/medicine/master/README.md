# Medicine extension

Adds fields to the item object relevant to the procurement of medicines.

## Guidance

This extension is used to describe medicinal products at the tender, award and/or contract stages. Using this extension, a publisher can specify the medicinal product's active ingredients and their strength, the dosage form, the medicine's container, and the administration route. In doing so, it makes it easier to compare the procurement of medicinal products across jurisdictions, and thereby supports [external reference pricing](https://en.wikipedia.org/wiki/External_reference_pricing).

Dosage forms and container sizes differ significantly across countries, which makes comparison difficult. To ease comparison, the extension provides standardized codelists for the dosage form, immediate container and administration route, based on [Health Level Seven (HL7)](https://www.hl7.org), a set of international standards for health data. That said, if you haven't adopted and can't map your values to the HL7 codes, you may use your own codes. To allow a user to interpret your codes, you should describe the codelists, and how to find the definitions of codes, in your [publication policy](https://standard.open-contracting.org/latest/en/guidance/publish/#finalize-your-publication-policy).

For the names of active ingredients, it is recommended to use [International Nonproprietary Names (INN)](https://www.who.int/teams/health-product-and-policy-standards/inn). The World Health Organization (WHO) maintains a cumulative list of all INNs, with equivalent names in Latin, English, French, Spanish, Arabic, Chinese and Russian. To ease comparison, it is recommended to use the lowercase Latin name.

If a contracting process is in the award or contract stage, it’s possible to know more information about the medicine, such as the brand, the manufacturer, the country of origin, the expiration date, if they must maintain a cold chain and all the other commercial, financial and logistical conditions. Use the [generic item attributes](https://extensions.open-contracting.org/en/extensions/itemAttributes/master/) extension for all the cases where the medicine item has other attributes not included in this extension.

If a medicine item has more than one active ingredient, add each one to the `activeIngredients` array.

## Examples

### One active ingredient

In this example, we demonstrate how to use this extension to describe a [drug procurement process](https://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?qs=OE1kSVnLUBVxS5IkXPNLRQ==) from Chile. (You can view its [original OCDS data](https://api.mercadopublico.cl/APISOCDS/ocds/tender/734-82-LP14).)

Item 3 is described as:

Description | Minimum dispensing unit
-|-
Acetilcisteina | ACETILCISTEINA-N 100 MG/ML SOLUCION PARA NEBULIZAR FRASCO 15-30 ML ENVASE INDIVIDUAL RESISTENTE CON SELLO QUE ASEGURE INVIOLABILIDAD DEL CONTENIDO

The strength is expressed as "100 MG/ML". The UN/CEFACT [Recommendation 20 – Codes for Units of Measure Used in International Trade](https://unece.org/trade/uncefact/cl-recommendations) codelist includes units like mg/l, g/l and kg/l, but not mg/ml. So, "100 MG/ML" is expressed as 100 g/l below.

Based on this information, we can add the `dosageForm`, `administrationRoute`, `immediateContainer` and `activeIngredients`.

```json
{
  "tender": {
    "items": [
      {
        "id": "1",
        "description": "Acetilcisteina",
        "classification": {
          "id": "51161701",
          "scheme": "UNSPSC",
          "uri": "https://apis.mercadopublico.cl/OCDS/data/productos/categoria/51161701"
        },
        "dosageForm": "SOL",
        "administrationRoute": "NASINHL",
        "immediateContainer": {
          "name": "vial",
          "capacity": {
            "unit": {
              "scheme": "UNCEFACT",
              "id": "ml"
            },
            "value": "[15,30]"
          }
        },
        "activeIngredients": [
          {
            "name": "acetylcysteinum",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "g/l"
              },
              "value": 100
            }
          }
        ]
      }
    ]
  }
}
```

### More than one active ingredient

In this example, we demonstrate how to use this extension to describe a [drug procurement process](https://www.contrataciones.gov.py/licitaciones/convocatoria/391507-adquisicion-medicamentos-hospital-clinicas-1.html#pliego) from Paraguay. (You can view its [original OCDS data](https://contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-391507).)

In the "Suministros requeridos - especificaciones técnicas" tab, item 1 of lot 8 ("LOTE N° 8 - ANESTESICOS LOCALES - 2") is described as:

Description | Technical specifications | Unit of measurement | Presentation |  Delivery presentation
-|-|-|-|-
Clorhidrato de Bupivacaina Hiperbarica Inyectable | clorhidrato de bupivacaina 25 mg. + dextrosa 82,5 mg. - solución inyectable | UNIDAD | AMPOLLA | ampollas como minimo de 5 ml.

For the name of the active ingredient, Annex 2 of the [INN Stem Book 2018](https://www.who.int/teams/health-product-and-policy-standards/inn/stembook), describes how to name acid salts: in this case, "bupivacainum hydrochloridum".

Based on this information, we can add the `dosageForm`, `administrationRoute`, `immediateContainer` and `activeIngredients`.

```json
{
  "tender": {
    "items": [
      {
        "id": "1",
        "dosageForm": "SOL",
        "administrationRoute": "ISINJ",
        "immediateContainer": {
          "name": "amp",
          "capacity": {
            "unit": {
              "scheme": "UNCEFACT",
              "id": "ml"
            },
            "value": "[5,INF["
          }
        },
        "activeIngredients": [
          {
            "name": "bupivacainum hydrochloridum",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "mg"
              },
              "value": 25
            }
          },
          {
            "name": "dextrosa",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "mg"
              },
              "value": 82.5
            }
          }
        ],
        "quantity": 25
      }
    ]
  }
}
```

## Related standards

The fields, definitions and codelists used in this extension are based on the following standards that are commonly used in the data on public medicine purchases.

- Most of the fields are based on the [Drug](https://schema.org/Drug) definition by the [Schema.org Community Group](https://www.w3.org/community/schemaorg/) and the [Medication Resource](https://www.hl7.org/fhir/medication.html) from [Fast Healthcare Interoperability Resources (FHIR)](https://hl7.org/fhir/) standard.
- The `administrationRoute` codelist contains the top-level concepts in HL7's [Route of Administration](https://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration/) codelist, excluding any synonymous terms.
- The `dosageForm` codelist contains the top-level concepts in HL7's [Orderable Drug Form](https://terminology.hl7.org/CodeSystem/v3-orderableDrugForm/) codelist, excluding the specific forms of sprays.
- The `immediateContainer` codelist is a copy of the codes and titles from FHIR's [Medication Knowledge Package Type](https://terminology.hl7.org/CodeSystem/medicationknowledge-package-type/) codelist. Given that the terms are undefined in FHIR, the descriptions are copied from corresponding terms from the [EDQM Standard Terms database](https://standardterms.edqm.eu), reproduced with the permission of the European Directorate for the Quality of Medicines & HealthCare, Council of Europe (EDQM). The EDQM Standard Terms database is not a static list and content can change over time; the descriptions were retrieved on July 21, 2021.

## Background

This extension is based on research with 4 data users and 6 data publishers including public organizations, journalists, medicine price analysts, and software developers for medicine purchase systems from 9 countries in Latin America, Europe, and Africa. The extension includes the most used fields from the different countries.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-12-04

- Rename `container` to `immediateContainer`
- Rename `container.csv` to `immediateContainer.csv`
