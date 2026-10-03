# Comunicación

Adds a communication object to the tender and lot objects, to describe the modalities of communication about key events.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-124, BT-127, BT-631, BT-632 and BT-738](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/).For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

### Tender

An example of a planning notice from which a competition notice will follow.

```json
{
  "tender": {
    "communication": {
      "atypicalToolName": "ACertainTool",
      "atypicalToolUrl": "https://ecomm-procurement.example.net",
      "futureNoticeDate": "2020-06-17T00:00:00+01:00",
      "noticePreferredPublicationDate": "2020-03-15T00:00:00+01:00",
      "documentAvailabilityPeriod": {
        "startDate": "2020-06-15T00:00:00+01:00",
        "endDate": "2020-07-10T00:00:00+01:00"
      }
    }
  }
}
```

### Lot

An example of a planning notice that is used as a call for competition and that is divided into lots.

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "communication": {
          "atypicalToolName": "ACertainTool",
          "atypicalToolUrl": "https://ecomm-procurement.example.net",
          "noticePreferredPublicationDate": "2020-03-15T00:00:00+01:00",
          "documentAvailabilityPeriod": {
            "startDate": "2020-06-15T00:00:00+01:00",
            "endDate": "2020-07-10T00:00:00+01:00"
          },
          "invitationToConfirmInterestDispatchDate": "2020-11-15T09:00:00+01:00"
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-03-09

- Add fields:
  - `Communication.atypicalToolName`
  - `Communication.invitationToConfirmInterestDispatchDate`
  - `Communication.noticePreferredPublicationDate`
  - `Lot.communication`

### 2021-01-19

- Agregar el campo `tender.communication.documentAvailabilityPeriod`

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en [pull resquests](https://github.com/open-contracting-extensions/ocds_communication_extension/pulls?q=is%3Apr+is%3Aclosed).
