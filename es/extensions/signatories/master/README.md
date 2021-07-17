# Firmantes del contrato

## Antecedentes

En OCDS, los firmantes del contrato no se declaran explícitamente en la sección `contracts`. En su lugar, se asume implícitamente que los firmantes son el `buyer`  (la `publicAuthority` en la ampliación de la APP) y los `suppliers` en la adjudicación asociada al contrato (los `preferredBidders` en la ampliación de la APP).

En algunos tipos de procesos de contratación, pueden existir firmantes adicionales del contrato, o los firmantes del contrato pueden diferir de los especificados en `buyer` (`publicAuthority`) y `suppliers` (`preferredBidders`).

## Uso

Esta extensión agrega un campo `signatories` a la sección `contracts`. La propiedad `signatories` es una lista de `OrganizationReference`.

Utilice esta extensión sólo si los firmantes de un contrato difieren de los `suppliers` de su adjudicación y del `buyer` del proceso de contratación. En ese caso, liste todos los firmantes del contrato, incluidos el `buyer`  y los `suppliers`.

## Ejemplo

El siguiente fragmento de JSON modela un proceso de contratación en el que hay un firmante adicional del contrato además de los definidos en los campos `buyer` y `awards.suppliers`.

```json
{
  "buyer": {
    "name": "Ministry of Communications",
    "id": "GB-GOV-12345678"
  },
  "awards": [
    {
      "id": "1",
      "suppliers": [
        {
          "name": "Example Consortium",
          "id": "GB-COH-00000000"
        }
      ]
    }
  ],
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "signatories": [
        {
          "name": "Ministry of Communications",
          "id": "GB-GOV-12345678"
        },
        {
          "name": "Example Consortium",
          "id": "GB-COH-00000000"
        },
        {
          "name": "Telecommunications UK",
          "id": "GB-GOV-99999999"
        }
      ]
    }
  ]
}
```

## Notas de uso

Cada firmante del contrato debe tener una entrada asociada en la sección `parties` de OCDS.

Esta extensión sigue el enfoque de modelización de organizaciones introducidas en OCDS V1.1.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.
