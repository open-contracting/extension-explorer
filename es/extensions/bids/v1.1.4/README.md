# Estadísticas y detalles de las ofertas

La información sobre las ofertas presentadas como parte de un proceso de contratación es importante para muchas formas de análisis, incluyendo:

- Análisis de mercado para comprender la competitividad de un mercado determinado;
- Análisis de banderas rojas para comprender los posibles riesgos de corrupción; y
- Análisis de valor por dinero;

Los regímenes regulatorios varían en la medida en que permiten que la información sobre licitaciones se publique de forma proactiva y en qué momento del proceso de adquisición. En algunos sistemas y procesos, se publicará una lista de licitadores invitados al comienzo de la licitación, y todos los detalles y documentos sobre las ofertas recibidas podrán ser revelados cuando se complete la evaluación. En otros sistemas, sólo pueden hacerse públicas las estadísticas resumidas sobre el número de ofertas recibidas.

La extensión de oferta de OCDS introduce una sección nueva, flexible y de alto nivel para cada proceso de contratación para capturar información de ofertas. Los ejecutores deberán evaluar qué campos son aplicables a su régimen regulatorio local y los casos de uso locales.

## Esquema

La lista `bids/details` se utiliza para proporcionar uno o más objetos ` Bid`, cada uno de los cuales representa una única oferta recibida.

La lista `bids/statistics` se usa para representar información estadísitca sobre el número de ofertas y ofertantes. En cada entrada de la lista hay un objeto `BidsStatistic` que contiene al menos:

- Un identificador
- Una medida, de la lista de códigos `bidStatistics.csv`
- Un valor para esa medida

La lista de códigos `bidStatistics.csv` es una lista de códigos **abierta**. Los publicadores pueden agregar sus propios códigos a esta lista. Al hacerlo, se alienta a los publicadores a comprometerse con la comunidad de contrataciones abiertas para acordar las definiciones de cada código.

Por ejemplo, tal vez los publicadores deseen agregar estadísticas sobre negocios pertenecientes a minorías o mujeres, u ofertas que cumplan ciertos estándares y metas ambientales.

La lista de código en la columna Categoría muestra si la estadística aplica a las ofertas u ofertantes o si esta especificado o requerido por una categoría particular del contexto regulatorio (ej. UE)

## Ejemplo

A continuación se muestra un ejemplo de una extensión de ofertas:

```json
{
  "bids": {
    "statistics": [{
      "id": "1.0",
      "measure": "validBids",
      "value": 1,
      "date": "2016-12-09T01:00:00+01:00",
      "notes": "This statistic covers the total number of unique bids received that were considered valid against relevant criteria."
    }, {
      "id": "2.0",
      "measure": "disqualifiedBids",
      "value": 1,
      "date": "2016-12-10T01:00:00+01:00",
      "notes": "This statistic covers the total number of unique bids received that were disqualified."
    }],
    "details": [{
      "id": "1.0",
      "date": "2016-12-09T01:00:00+01:00",
      "status": "valid",
      "value": {
        "amount": 1000,
        "currency": "USD"
      },
      "documents": [{
        "id": "1.0",
        "documentType": "evaluationReports",
        "title": "Mega Consortium Bid Evaluation Report",
        "description": "This document provides details of the evaluation of the bid submitted by Mega Consortium",
        "url": "http://communications.gov.example/example_ppp/evaluationReport_megaConsortium.pdf",
        "datePublished": "2016-11-17T10:00:00-06:00",
        "format": "application/pdf",
        "language": "en",
        "author": "Ministry of Communications"
      }],
      "tenderers": [{
        "id": "MEGA",
        "name": "Mega Consortium"
      }]
    }, {
      "id": "2.0",
      "date": "2016-12-10T01:00:00+01:00",
      "status": "disqualified",
      "value": {
        "amount": 1500,
        "currency": "USD"
      },
      "documents": [{
        "id": "1.0",
        "documentType": "evaluationReports",
        "title": "Beta Consortium Bid Evaluation Report",
        "description": "This document provides details of the evaluation of the bid submitted by Beta Consortium",
        "url": "http://communications.gov.example/example_ppp/evaluationReport_betaConsortium.pdf",
        "datePublished": "2016-11-18T10:00:00-06:00",
        "format": "application/pdf",
        "language": "en",
        "author": "Ministry of Communications"
      }],
      "tenderers": [{
        "id": "BETA",
        "name": "Beta Consortium"
      }]
    }]

  },
  "awards": [{
    "id": "111",
    "title": "Example PPP contract award",
    "description": "Award of Example PPP contract to Mega Consortium",
    "status": "active",
    "date": "2016-12-17T10:00:00-06:00",
    "relatedBid": "1.0"
  }]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.4

- Se corrige el título y la descripción del código 'foreignBidsFromEU' para referirse al Área Económica Europea (AEE). Anteriormente, el título se refería al Mercado Único Europeo, pero su descripción enlistaba los miembros del AEE.
- Añade el código `foreignBidsFromNonEU a `bidStatistics.csv\`
- Quitar propiedad  `required` invalide a la matriz del campo `Bids.details`
- Arreglar el comportamiento de unión de  `Bids.statistics` a  `Bid.tenderers` para identificar la estrategia de unión de los identificadores
- Quita las directrices Sphinx del readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- No permitir que los campos requeridos `BidsStatistic.id`,` BidsStatistic.measure`, `BidsStatistic.value` sean null
- No permitir que `Bids.statistics` tenga null en su lista de objetos
- Permitir que `Bids.statistics` sea null
- Agregar enum a `BidsStatistic.status`
- Mover `BidsStatistic.requirementResponses` a la extensión de requisitos
- Agregar descripciones a bidStatus.csv
- Enlista listas de códigos en extension.json
- Agregar un ejemplo a la documentación
- Agregar pruebas y ordenar el código
