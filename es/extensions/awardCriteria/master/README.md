# Desglose de los criterios de adjudicación

Agrega una matriz de criterios de adjudicación al objeto lote, para desglosar los criterios de adjudicación por precio, costo y calidad.

## Contexto legal

En la Unión Europea, los campos de esta extensión corresponden a \[eForms BG-707 (Award Criteria)\] (https://github.com/eForms/eForms). Consulte \[OCDS para la Unión Europea\] (http://standard.open-contracting.org/profiles/eu/master/en/) para ver las correspondencias con Tenders Electronic Daily (TED).

[Directiva 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj) [Artículo 67](https://eur-lex.europa.eu/eli/dir/2014/24/oj#d1e5950-65-1)(5) describe ponderaciones y órdenes de importancia.

## Ejemplos

### Peso

Estos criterios de adjudicación son 50% calidad de servicio y 50% precio.

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

### Fijado

El precio es fijado a $100,000, de manera que los licitadores compitan únicamente en calidad.

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

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Este modelo fue discutido en <https://github.com/eForms/eForms/issues/119>, <https://github.com/eprocurementontology/eprocurementontology/issues/157> y <https://github.com/eprocurementontology/eprocurementontology/issues/203>. Esta extensión fue discutida originalmente como parte de [OCDS para el perfil de la UE](https://github.com/open-contracting-extensions/european-union/issues), en [pull requests](https://github.com/open-contracting-extensions/ocds_awardCriteria_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/443>.
