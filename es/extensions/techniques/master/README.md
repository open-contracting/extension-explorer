# Técnicas

Agrega campos a los objetos de licitación y lote para describir el uso de técnicas, como acuerdos marco, sistemas dinámicos de compra y subastas electrónicas.

## Guía

### `value` y  `period` del acuerdo marco

Los campos `value` y` period` de los objetos `FrameworkAgreement` solo deben usarse si una fuente de datos proporciona valores y períodos tanto para el contrato / lote como para el acuerdo marco, como TED XML Schema R2.08. De lo contrario:

- Si una adquisición no está dividida en lotes, utilice los campos `tender.value` y` tender.contractPeriod`.
- Si una adquisición se divide en lotes, utilice los campos `value` y` contractPeriod` de los objetos `Lot`.

### `method` del acuerdo marco

Estos son los valores posibles para `FrameworkAgreement.method` y sinónimos comunes:

- withoutReopeningCompetition: cancelaciones
- withReopeningCompetition: mini-competencias
- withAndWithoutReopeningCompetition: cancelaciones y mini-competencias

## Contexto legal

En la Unión Europea, los campos de esta extensión corresponden a \[eForms BG-706 (Técnicas)\] (https://github.com/eForms/eForms). Consulte \[OCDS para la Unión Europea\] (http://standard.open-contracting.org/profiles/eu/master/en/) para ver las correspondencias con Tenders Electronic Daily (TED).

## Ejemplos

### Acuerdo marco

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasFrameworkAgreement": true,
          "frameworkAgreement": {
            "minimumParticipants": 2,
            "maximumParticipants": 100,
            "method": "withoutReopeningCompetition",
            "periodRationale": "<A good justification>",
            "buyerCategories": "all hospitals in the Tuscany region",
            "value": {
              "amount": 240000,
              "currency": "EUR"
            },
            "period": {
              "durationInDays": 730
            },
            "description": "Call offs are estimated to be organized every 3 months, with an average value of 60,000 euros per contract."
          }
        }
      }
    ]
  }
}
```

### Sistema de compra dinámica

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasDynamicPurchasingSystem": true,
          "dynamicPurchasingSystem": {
            "type": "closed",
            "status": "active"
          }
        }
      }
    ]
  }
}
```

### Subasta electrónica

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "techniques": {
          "hasElectronicAuction": true,
          "electronicAuction": {
            "url": "https://example.com/auction/1",
            "description": "<Any relevant details>"
          }
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-10-05

- Agregar los campos `minimumParticipants`, `value`, `period` y  `description` al objeto `FrameworkAgreement`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en \[pull requests\] (https://github.com/open-contracting-extensions/ocds_techniques_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/695>.
