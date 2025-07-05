# Desglose de los criterios de adjudicación

Adds an award criteria array to the `Lot` and `LotGroup` objects, to break down award criteria by price, cost and quality.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-707 (Award Criteria)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/).For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

[Directiva 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj) [Artículo 67](https://eur-lex.europa.eu/eli/dir/2014/24/oj#d1e5950-65-1)(5) describe ponderaciones y órdenes de importancia.

## Ejemplos

### Lotes

#### Peso

The award criteria for the lot are 50% service quality and 50% price.

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "awardCriteria": {
          "criteria": [
            {
              "type": "quality",
              "name": "Service quality",
              "numbers": [
                {
                  "number": 50,
                  "weight": "percentageExact"
                }
              ]
            },
            {
              "type": "price",
              "name": "Price",
              "numbers": [
                {
                  "number": 50,
                  "weight": "percentageExact"
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

#### Fijado

The price of the lot is fixed at $100,000, such that tenderers compete on quality only.

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "awardCriteria": {
          "criteria": [
            {
              "type": "price",
              "name": "Fixed price",
              "numbers": [
                {
                  "number": 100000,
                  "fixed": "total"
                },
                {
                  "number": 0,
                  "weight": "decimalExact"
                }
              ]
            },
            {
              "type": "quality",
              "name": "Service quality",
              "numbers": [
                {
                  "number": 1,
                  "weight": "decimalExact"
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

### Grupo del lote

The award criteria for the lot group is 100% price.

```json
{
  "tender": {
    "lotGroups": [
      {
        "id": "1",
        "awardCriteria": {
          "criteria": [
            {
              "type": "price",
              "name": "Price",
              "numbers": [
                {
                  "number": 100,
                  "weight": "percentageExact"
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

### 2022-04-25

- Add expressions of interest to the `criterionThreshold.csv` code descriptions.
- Generalize AwardCriterionNumber to `CriterionNumber` for reuse in other extensions.

### 2022-02-27

- Add `LotGroup.awardCriteria` field.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Este modelo fue discutido en <https://github.com/eForms/eForms/issues/119>, <https://github.com/eprocurementontology/eprocurementontology/issues/157> y <https://github.com/eprocurementontology/eprocurementontology/issues/203>. Esta extensión fue discutida originalmente como parte de [OCDS para el perfil de la UE](https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_awardCriteria_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/443>.
