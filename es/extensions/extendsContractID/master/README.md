# extendsContractID

Bajo algunas reglas y procesos de compras públicas, para extender el valor o duración del contrato, o para hacer grandes cambios, se requiere firmar un nuevo contrato.

Este nuevo contrato forma parte de el mismo proceso de contrataciones así como el contrato antiguo que esta extendiendo

En estos casos, el campo `extendsContractID` puede utilizarse para identificar que una entrada determinada en la lista `contracts` debe entenderse como relacionada a un contrato anterior.

Utilice esta extensión **sólo si** hay un nuevo contrato sustantivo firmado como la extensión de un contrato anterior. En la mayoría de los casos, una actualización del valor o de la duración de un contrato debería modelarse como una enmienda dentro de una única entrada en la lista `contracts`.

## Ejemplo

El extracto más abajo muestra tres contratos en la matriz de contratos en un release OCDS.

Los primeros dos contratos se firmaron en 2011: uno por cada año de renta de la propiedad, y otro por dos años de servicios relacionados con la propiedad rentada.

El tercer contrato se firmó en 2012, y renueva el alquiler de la propiedad por un año más. Se relaciona de nuevo con el contrato del primer año de alquiler con el campo `extendsContractID`.

```json
{
  "contracts": [
    {
      "id": "207002-armin-hahner-stollmaier-21",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "title": "Alquileres para la SNNA",
      "status": "terminated",
      "period": {
        "startDate": "2011-01-02T23:59:59+00:00",
        "endDate": "2012-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 1800000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "01",
          "description": "Alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2011-03-14T16:58:40+00:00"
    },
    {
      "id": "207004-armin-hahner-stollmaier-21-service",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "title": "Servicios relacionados con alquileres para la SNNA",
      "status": "active",
      "period": {
        "startDate": "2011-01-02T23:59:59+00:00",
        "endDate": "2013-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 10000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "02",
          "description": "Servicios relacionados con alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2011-03-14T16:58:40+00:00"
    },
    {
      "id": "207002-armin-hahner-stollmaier-21-renovacion",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "extendsContractID": "207002-armin-hahner-stollmaier",
      "title": "Ad Referendum - Alquileres para la SNNA (Amends contract 207002)",
      "status": "active",
      "period": {
        "startDate": "2012-01-02T23:59:59+00:00",
        "endDate": "2013-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 12780000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "01",
          "description": "Alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2012-03-14T16:58:40+00:00"
    }
  ]
}
```

La imagen siguiente muestra un ejemplo de cómo se utiliza la información proporcionada por el campo `extendsContractID` en Paraguay, para mostrar dos contratos resultantes de una adjudicación (las casillas azules), con uno de esos contratos prorrogado (el círculo azul).

![Paraguay Example](https://cloud.githubusercontent.com/assets/342624/9915392/aecb1e52-5cae-11e5-9824-a6eb616e568b.png)

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2018-01-29

- Hacer que `Contract.extendsContractID` pueda ser nulo.
