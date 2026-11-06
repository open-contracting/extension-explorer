# Accionistas

Agrega campos de propiedad de la empresa al objeto de organización utilizado en la lista de partes.

For example, when bidding in Public Private Partnerships, companies can be required to disclose their ownership information. After a contract is signed and during project implementation, the ownership information of the Special Purpose Vehicle (SPV) that is operating the contract might need to be updated.

Since each owner mentioned in the `shareholders` array should have a corresponding entry in the `parties` array, it is possible to use this extension to describe multiple levels of corporate ownership.

## Ejemplo

```json
{
  "parties": [
    {
      "id": "MEGA",
      "name": "Mega Consortium",
      "shareholders": [
        {
          "id": "1",
          "shareholder": {
            "id": "AHL",
            "name": "Alpha Holdings Ltd"
          },
          "shareholding": 0.67,
          "votingRights": "additional",
          "votingRightsDetails": "Alpha Holdings Ltd. is entitled to 5 votes per share.",
          "notes": "Alpha Holdings Ltd. must maintain a minimum shareholding of 30% in the project company until 10 years from the date of commissioning have elapsed."
        },
        {
          "id": "2",
          "shareholder": {
            "id": "BET",
            "name": "Beta Investment Company Ltd"
          },
          "shareholding": 0.33,
          "votingRights": "ordinary"
        }
      ]
    },
    {
      "id": "BET",
      "name": "Beta Investment Company Ltd"
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-12-04

- Update and clarify `Shareholder.shareholding` field description.

### 2021-05-24

- Eliminar `Organization.beneficialOwnership`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `Organization.beneficialOwnership` no nulo (deshacer cambio anterior).

### 2018-05-08

- Make `Shareholder.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-01-29

- Hacer que `Organization.beneficialOwnership` pueda ser nulo.
