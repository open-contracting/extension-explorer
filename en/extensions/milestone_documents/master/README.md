# Milestone Documents

In OCDS 1.1, core support for documents attached to individual milestones was removed from the milestones block to simplify the standard.

This extension re-introduces the `documents` block to `milestones`, providing fields to detail the documents related to each individual milestone.

## Guidance

Publishers ought to consider that many consuming applications will only look at the `tender.documents`, `awards.documents`, `contracts.documents` and `contracts.implementation.documents` section to access and display relevant documentation to users.

Document titles, document types, and descriptions can be used to indicate to human readers the particular nature of the documents and any milestones they relate to.

However, in cases where it is important to track documents on a milestone-by-milestone basis this extension can be introduced.

Depending on the nature of the documents, publishers ought to consider duplicating information in the parent section's documents block.

## Example

During the implementation of a contract, the buyer sets milestones that the supplier needs to meet. Each of these milestones can have an associated document that offers more details about the met milestone: for example, a consultancy report:

```json
{
  "contracts": [
    {
      "id": "CO-40002-18-166811",
      "awardID": "354469-jorge-augusto-zarate-leiva-1",
      "implementation": {
        "milestones": [
          {
            "id": "fcrMXKIb3/o=",
            "title": "Informe de Consultoria",
            "type": "reporting",
            "dueDate": "2020-02-13T00:00:00-04:00",
            "dateMet": "2020-02-14T00:00:00-04:00",
            "status": "met",
            "documents": [
              {
                "id": "QQ1cjJZ82Rk=",
                "url": "https://www.contrataciones.gov.py/documentos/download/contrato_detalle_entregable/vki7v5RKGrA%253D",
                "datePublished": "2020-02-17T13:38:25-04:00",
                "language": "es",
                "title": "informe_n__13_1581957505348.pdf",
                "format": "application/pdf"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### v1.1.5

- Review normative and non-normative words

### v1.1.4

- Update extension.json for Extension Explorer

### v1.1.3

- Use Apache 2.0 License
- Add tests and tidy code
