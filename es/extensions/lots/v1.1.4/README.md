# Lotes

Cuando se desglosa una sola licitación en partes que pueden ofertarse y se adjudican separadamente, esto se presenta utilizando la **extensión de lotes**.

La extensión de lotes mantiene la estructura general de una entrega de OCDS, con artículos, documentos e hitos incluidos inmediatamente dentro de los elementos `tender`, `award` y `contract`, pero introduce una lista de lotes en la sección `tender`, y la capacidad de hacer referencia cruzada a un `relatedLot` específico para cada elemento, y una lista de `relatedLots` para documentos, hitos y adjudicaciones

La sección opcional `lotDetails` y `lotGroups` permite que se expresen condiciones más complejas en torno a la adjudicación de lotes, como el valor máximo de un grupo de lotes.

Esto significa que los sistemas que no conocen la 'existencia de lotes' de igual forma pueden entender el valor global de la contratación que se esta llevando a cabo, los acontecimientos clave y las relaciones entre los compradores y los proveedores. Al mismo tiempo, los sistemas que sí conocen de la 'existencia de lotes' pueden hacer uso de la información referenciada para presentar una visión centrada-en-lotes en la información a los usuarios, o para analizar la contratación lote por lote.

## Lote Relacionado

La propiedad `relatedLot` (singular) está disponible para:

- items

Se puede proporcionar una lista de `relatedLots` (plural) para cada uno de los siguientes:

- documents
- milestones
- awards

Cuando se usan lotes, **todos los elementos** deben tener una propiedad `relatedLot`.

Los documentos e hitos pueden tener opcionalmente una propiedad `relatedLots`. Aquellos sin esta propiedad deben interpretarse como aplicables a la licitación en su conjunto.

Los artículos dentro de una adjudicación deben tener cada uno una propiedad `relatedLot`, pero los publicadores pueden también hacer referencia a todos los lotes en los que se relaciona una adjudicación en el nivel de adjudicación usando `relatedLots`

Cuando la extensión de ofertas también está en uso, cada oferta también puede declarar sus lotes relacionados.

## Ejemplo desarrollado

Se emite una licitación para consultoría en el desarrollo de un nuevo edificio público. Esto podría incluir elementos para:

- Diseño arquitectónico
- Servicios de asesoramiento arquitectónico
- Consultoría de ingeniería civil
- Consultoría en ingeniería estructural

Aunque forma parte de la misma oferta, el comprador está dispuesto a adjudicar estos diferentes artículos a diferentes empresas, y así divide la oferta en tres lotes.

```json
{
  "tender": {
    "items": [
      {
        "id": "0001",
        "description": "Architectural advice",
        "classification": {
          "scheme": "CPV",
          "id": "71210000",
          "description": "Advisory architectural services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0002",
        "description": "Architectural design",
        "classification": {
          "scheme": "CPV",
          "id": "71220000",
          "description": "Architectural design services"
        },
        "relatedLot": "lot-1"
      },
      {
        "id": "0003",
        "description": "Civil engineering consultant",
        "classification": {
          "scheme": "CPV",
          "id": "71311000",
          "description": "Civil engineering consultancy services"
        },
        "relatedLot": "lot-2"
      },
      {
        "id": "0004",
        "description": "Structural engineering services",
        "classification": {
          "scheme": "CPV",
          "id": "71312000",
          "description": "Structural engineering consultancy services"
        },
        "relatedLot": "lot-3"
      }
    ],
    "value": {
      "amount": 1200000,
      "currency": "GBP"
    },
    "lots": [
      {
        "id": "lot-1",
        "title": "Architectural services",
        "description": "For architectural services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 200000
        }
      },
      {
        "id": "lot-2",
        "title": "Civil engineering services",
        "description": "For civil engineering services delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 400000
        }
      },
      {
        "id": "lot-3",
        "title": "Structural engineering",
        "description": "For structural engineering consultancy delivered in the project",
        "status": "active",
        "value": {
          "currency": "GBP",
          "amount": 600000
        }
      }
    ],
    "lotGroups": [
      {
        "id": "lot-group-1",
        "relatedLots": [
          "lot-2",
          "lot-3"
        ],
        "optionToCombine": true,
        "maximumValue": {
          "currency": "GBP",
          "amount": 1000000
        }
      }
    ],
    "lotDetails": {
      "maximumLotsBidPerSupplier": 4,
      "maximumLotsAwardedPerSupplier": 2
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.4

- No permitir que `Tender.lotDetails` sea null (error introducido en la primera versión)
- `Tender.lotDetails` ya no usa `$ref` para una definición de `LotDetails`
- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que los campos `relatedLots` tengan null en sus listas de cadenas
- Agregar enum a `Lot.status`
- Permitir que los campos `relatedLots` sean null
- Agregar título y descripción a `Tender.lotDetails`
- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
