# Firmantes del contrato

Adds a signatories array to the contract object, for when the signatories differ from the buyer for the contracting process and the suppliers for the award.

In OCDS, the signatories to a contract are not explicitly declared in the `contracts` section. Instead, the signatories are implicitly assumed to be the `buyer` and the `suppliers` in the award associated to the contract.

In some types of contracting processes, there can be additional signatories to the contract, or the signatories to the contract can differ from those specified in `buyer` and `suppliers`.

Utilice esta extensión **sólo si** los firmantes de un contrato difieren de los proveedores `suppliers` de su adjudicación y del comprador `buyer` del proceso de contratación. En ese caso, enumere todos los firmantes del contrato, incluidos el comprador `buyer` y los proveedores `suppliers`.

## Guía

Each signatory should have an associated entry in the `parties` section.

## Ejemplo

A contract with a third signatory, in addition to the buyer and supplier:

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

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.
