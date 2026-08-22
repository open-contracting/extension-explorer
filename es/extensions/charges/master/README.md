# Cargos

La extensión de cargos se utiliza para registrar detalles de los **cargos totales** estimados o aplicados a los usuarios o al gobierno durante la operación de un contrato de Asociación Público Privada.

Esto puede utilizarse para proporcionar un desglose del **apoyo gubernamental** a un proyecto, sobre una base de período por período.

La extensión de cargos introduce una lista `charges` al objeto `contracts.implementation`.

## Ejemplo

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Public Private Partnership Agreement",
      "description": "Public-Private Partnership agreement entered into by and between telecoms promoter, together with national fibre infrastructure and the special purpose vehicle Mega Consortium Ltd",
      "implementation": {
        "charges": [
          {
            "id": "2025-user",
            "title": "User charges for calendar year 2025 resulting from 4G, 3G, voice and SMS tariffs",
            "estimatedValue": {
              "amount": 1019100000,
              "currency": "USD"
            },
            "paidBy": "user",
            "period": {
              "startDate": "2025-01-01T00:00:00Z",
              "endDate": "2025-12-31T23:59:59Z"
            }
          },
          {
            "id": "2026-user",
            "title": "User charges for calendar year 2026 resulting from 4G, 3G, voice and SMS tariffs",
            "estimatedValue": {
              "amount": 1129206411.9632988,
              "currency": "USD"
            },
            "paidBy": "user",
            "period": {
              "startDate": "2026-01-01T00:00:00Z",
              "endDate": "2026-12-31T23:59:59Z"
            }
          }
        ]
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2018-05-08

- Make `Charge.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
