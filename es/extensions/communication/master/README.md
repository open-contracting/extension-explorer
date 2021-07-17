# Comunicación

Agrega a la licitación un objeto comunicación para describir las modalidades de comunicación de los eventos claves.

## Contexto legal

En la unión Europea, los campos de esta extensión corresponden a[eForms BT-124 and BT-127](https://github.com/eForms/eForms). Ver [OCDS para la unión Europea](http://standard.open-contracting.org/profiles/eu/master/en/) para lo correspondiente a Tenders Electronic Daily (TED).

## Ejemplo

```json
{
  "tender": {
    "communication": {
      "atypicalToolUrl": "https://ecomm-procurement.example.net",
      "futureNoticeDate": "2020-06-17T00:00:00+01:00",
      "documentAvailabilityPeriod": {
        "startDate": "2020-06-15T00:00:00+01:00",
        "endDate": "2020-07-10T00:00:00+01:00"
      }
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2021-01-19

- Agregar el campo `tender.communication.documentAvailabilityPeriod`

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [pull resquests](https://github.com/open-contracting-extensions/ocds_communication_extension/pulls?q=is%3Apr+is%3Aclosed).
