# Shareholder details

La extensión de accionista se puede utilizar para proporcionar detalles de los propietarios de las partes involucradas en un proceso de contratación.

Por ejemplo, en los procesos de Asociaciones Público-Privadas, a menudo se requiere que las compañías divulguen información sobre sus estructuras de propiedad al licitar y cuando se adjudique el contrato, es necesario mantener información sobre la propiedad de una Sociedad con Fines Específicos (SPV) actualizada durante la ejecución del proyecto.

Debido a que cada propietario mencionado en la matriz de accionistas también debería obtener una entrada en la matriz `parties`, es posible utilizar esta extensión para acumular información sobre las redes de propiedad corporativa involucradas en un proceso de contratación.

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

### 2021-05-24

- Remove `Organization.beneficialOwnership`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `Organization.beneficialOwnership` no nulo (deshacer cambio anterior).

### 2018-05-08

- Hacer `Shareholder.id` obligatorio para soportar el seguimiento de revisiones y [fusión de listas](http://standard.open-contracting.org/latest/es/schema/merging/#lists)

### 2018-01-29

- Hacer que `Organization.beneficialOwnership` pueda ser nulo.
