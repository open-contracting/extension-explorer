# Proveedores de Contrato

El OCDS se ha diseñado alrededor de un modelo de contrataciones que:

- Uno o más licitaciones se hacen nombrando a los proveedores seleccionados;
- Un contrato se firma por cada licitación, refiriéndose a la licitación relacionada;

Por esta razón, el principal bloque `Contract` no incluye información sobre los `suppliers`. Estos se pueden encontrar en el `Award` relacionado usando la referencia cruzada `awardID`.

De cualquier forma, existen algunos procesos de contratación en las que una misma adjudicación a múltiples proveedores, resulta en contratos múltiples, cada uno para un solo proveedor. En esas instancias, es importante especificar los proveedores al nivel contrato.

La extensión Proveedores de Contratos introduce la matriz `contracts.suppliers` para este propósito.

## Ejemplo

Se otorga una adjudicación a un consorcio con múltiples proveedores. Luego, se firma un contrato con cada uno de ellos por separado. Cuando se utiliza esta extensión, se debe completar `contratos.items` y` contract.value` con los ítems adjudicados y el valor para cada proveedor.

```json
{
  "awards": [
    {
      "id": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 100000,
        "currency": "GBP"
      },
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 10,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ],
      "suppliers": [
        {
          "id": "GB-COH-1234567844",
          "name": "AnyCorp Cycle Provision"
        },
        {
          "id": "GB-COH-789456123",
          "name": "OtherCorp"
        }
      ]
    }
  ],
  "contracts": [
    {
      "id": "ocds-213czf-000-00001-contract-01",
      "awardID": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 70000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "GB-COH-1234567844",
          "name": "AnyCorp Cycle Provision"
        }
      ],
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 7,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ]
    },
    {
      "id": "ocds-213czf-000-00001-contract-02",
      "awardID": "ocds-213czf-000-00001-award-01",
      "value": {
        "amount": 30000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "GB-COH-789456123",
          "name": "OtherCorp"
        }
      ],
      "items": [
        {
          "id": "0001",
          "description": "Construction work for highways",
          "quantity": 3,
          "unit": {
            "name": "Miles",
            "value": {
              "amount": 10000,
              "currency": "GBP"
            }
          }
        }
      ]
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.
