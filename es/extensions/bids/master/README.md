# Estadísticas y detalles de las ofertas

Information about bids is important for many use cases, including:

- Market analysis, to understand competition
- Red flag analysis, to monitor corruption risk
- Value for money analysis

This extension introduces a top-level `bids` object to describe individual bids and aggregate statistics.

Depending on the procedure, a bid can be an estimate, offer, proposal, quote or quotation. Regulatory regimes vary on the extent to which they allow information about bids to be proactively published, and at what point in the procurement process. In some systems and processes, a list of invited bidders is published in a tender notice, and full details on the bids received are published in an award notice. In other systems, only summary statistics, like the number of bids received, is published.

## Esquema

La lista `bids/details` se utiliza para proporcionar uno o más objetos ` Bid`, cada uno de los cuales representa una única oferta recibida.

The `bids.statistics` array is used to represent key statistical information about the number of bids and bidders. Each entry in the array is a `Statistic` object containing at least:

- Un identificador
- A measure, from the `statistic.csv` codelist
- Un valor para esa medida

The `statistic.csv` codelist is an **open** codelist. Publishers can add their own codes to this list. When doing so, publishers are encouraged to engage with the open contracting community to agree upon definitions of each code.

Por ejemplo, tal vez los publicadores deseen agregar estadísticas sobre negocios pertenecientes a minorías o mujeres, u ofertas que cumplan ciertos estándares y metas ambientales.

La lista de código en la columna Categoría muestra si la estadística aplica a las ofertas u ofertantes o si esta especificado o requerido por una categoría particular del contexto regulatorio (ej. UE)

## Guía

### Correct a bid's value

Los compradores y entidades contratantes – y en algunas jurisdicciones, los oferentes – puden corregir el valor de una oferta después de que se envía la oferta: por ejemplo, para corregir un error aritmético o un punto decimal erróneo

En el OCDS, el valor de la oferta se publica con el campo `bids.details.value` . Si el valor de la oferta se corrige, el valor del campo `bids.details.value` queda sobreescrito. Si esto pasa, el valor original solo está disponible a través del proceso de contratación ' [change history](https://standard.open-contracting.org/latest/en/primer/releases_and_records/).

Como publicador, para hacer que tanto los valores originales como los valores corregidos esten disponibles para los usuarios, publique al menos dos entregas para el proceso de contratación: una entrega con el valor original de la oferta y otra con el valor corregido.

### Bids submitted for multiple lots

In some cases, potential suppliers can submit bids for multiple lots. Regardless of whether the bids take the form of a single document or multiple documents, OCDS models the "bid" for each lot as a separate object, to improve interoperability.

If a potential supplier submits a bid for multiple lots as a single document, for each lot, add a `Bid` object to the `bids.details` array. Add the bid's identifier to the object's `identifiers` array, and add the lot's identifier to the object's `relatedLots` array.

If the bid cannot be divided (for example, the data source describes only the total value of the bid, and not the individual value for each lot within the bid), create one `Bid` object, and add all lots' identifiers to the object's `relatedLots`.

## Examples

Aggregate post-award statistics and individual bid submissions:

```json
{
  "bids": {
    "statistics": [
      {
        "id": "1",
        "measure": "validBids",
        "value": 1,
        "date": "2016-12-09T01:00:00+01:00",
        "notes": "This statistic covers the total number of unique bids received that were considered valid against relevant criteria."
      },
      {
        "id": "2",
        "measure": "highestValidBidValue",
        "value": 1000,
        "valueGross": 1200,
        "currency": "USD"
      },
      {
        "id": "3",
        "measure": "lowestValidBidValue",
        "value": 1000,
        "valueGross": 1200,
        "currency": "USD"
      }
    ],
    "details": [
      {
        "id": "1",
        "date": "2016-12-09T01:00:00+01:00",
        "status": "valid",
        "identifiers": [
          {
            "id": "bid-123-456",
            "scheme": "internal"
          }
        ],
        "items": [
          {
            "id": "1",
            "description": "Installation and operation of the Shared Public Telecommunications Network",
            "classification": {
              "scheme": "CPV",
              "id": "32412100",
              "description": "Telecommunications network",
              "uri": "http://purl.org/cpv/2008/code-32412100"
            },
            "quantity": 1
          }
        ],
        "value": {
          "amount": 1000,
          "currency": "USD"
        },
        "tenderers": [
          {
            "id": "MEGA",
            "name": "Mega Consortium"
          }
        ],
        "countriesOfOrigin": [
          "MX"
        ],
        "hasRank": true,
        "rank": 1,
        "variant": true
      },
      {
        "id": "2",
        "date": "2016-12-10T01:00:00+01:00",
        "status": "disqualified",
        "value": {
          "amount": 1500,
          "currency": "USD"
        },
        "tenderers": [
          {
            "id": "BETA",
            "name": "Beta Consortium"
          }
        ],
        "hasRank": true,
        "rank": 2
      }
    ]
  },
  "awards": [
    {
      "id": "1",
      "title": "Example PPP contract award",
      "description": "Award of Example PPP contract to Mega Consortium",
      "status": "active",
      "date": "2016-12-17T10:00:00-06:00",
      "relatedBids": [
        "1"
      ]
    }
  ],
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "relatedBids": [
        "1"
      ]
    }
  ]
}
```

A potential supplier submits a bid for two lots as a single document:

```json
{
  "bids": {
    "details": [
      {
        "id": "1",
        "date": "2016-12-09T01:00:00+01:00",
        "identifiers": [
          {
            "id": "ABC-1350",
            "scheme": "internal"
          }
        ],
        "value": {
          "amount": 1000,
          "currency": "USD"
        },
        "tenderers": [
          {
            "id": "MEGA",
            "name": "Mega Consortium"
          }
        ],
        "relatedLots": [
          "LOT-0001"
        ]
      },
      {
        "id": "2",
        "date": "2016-12-09T01:00:00+01:00",
        "identifiers": [
          {
            "id": "ABC-1350",
            "scheme": "internal"
          }
        ],
        "value": {
          "amount": 500,
          "currency": "USD"
        },
        "tenderers": [
          {
            "id": "MEGA",
            "name": "Mega Consortium"
          }
        ],
        "relatedLots": [
          "LOT-0002"
        ]
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### No entregado

- Add fields:
  - `Bid.identifiers`
  - `Bid.description`
  - `Bid.items`
  - `Bid.countriesOfOrigin`
  - `Bid.hasRank`
  - `Bid.rank`
  - `Bid.relatedLots` (moved from the Lots extension)
  - `Bid.validityPeriod`
  - `Bid.variant`
  - `BidsStatistic.valueGross`
  - `Award.relatedBids`
  - `Contract.relatedBids`
- Deprecate the `Award.relatedBid` field
- Add guidance:
  - Correct a bid's value
  - Bids submitted for multiple lots
- Add codes to `statistic.csv`:
  - 'microBids'
  - 'smallBids'
  - 'mediumBids'
  - 'disqualifiedBids'
- Update and clarify `Statistic.value` field description
- Rename the `BidStatistic` definition to `Statistic`, and remove bid-specific language from its fields' descriptions
- Rename the `bidStatistics.csv` codelist to `statistic.csv`

### v1.1.5

- Añada el campo `BidsStatistic.currency`
- Añada los códigos 'lowestValidBidValue' y 'highestValidBidValue' a `bidStatistics.csv`
- Quitar la información sobre el tipo de las descripciones de los campos
- Revisar las palabras normativas y no-normativas

### v1.1.4

- Se corrige el título y la descripción del código 'foreignBidsFromEU' para referirse al Área Económica Europea (AEE). Anteriormente, el título se refería al Mercado Único Europeo, pero su descripción enlistaba los miembros del AEE.
- Añade el código `foreignBidsFromNonEU a `bidStatistics.csv\`
- Quitar propiedad invalida `required` en la matriz del campo `Bids.details`
- Arreglar el comportamiento de unión de  `Bids.statistics` a  `Bid.tenderers` para identificar la estrategia de unión de los identificadores
- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que los campos requeridos `BidsStatistic.id`,` BidsStatistic.measure`, `BidsStatistic.value` sean null
- No permitir que `Bids.statistics` tenga null en su lista de objetos
- Permitir que `Bids.statistics` sea null
- Agregar enum a `Bid.status`
- Mover `BidsStatistic.requirementResponses` a la extensión de requisitos
- Agregar descripciones a bidStatus.csv
- Enlista listas de códigos en extension.json
- Agregar un ejemplo a la documentación
- Agregar pruebas y ordenar el código
