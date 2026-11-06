# Document details

[Document objects](https://standard.open-contracting.org/latest/en/schema/reference/#document) are used to describe and link to documents. This extension adds fields to document objects to:

- Indicate the page numbers at which relevant information can be found within a large document
- Describe any special arrangements needed to access the document
- Name the author of the document (not to be confused with its publisher)
- Indicate the languages in which unofficial translations of the document are available

Use cases include:

- Accessing the document and locating the information within it
- Checking whether authors are involved in other ways in the contracting process, e.g. as bidders
- Measuring the accessibility of documents

## Example

```json
{
  "tender": {
    "documents": [
      {
        "id": "1",
        "documentType": "equityTransferCaps",
        "title": "Equity transfer cap terms",
        "description": "No equity transfer is permitted until construction is completed. See document for more details.",
        "url": "http://example.com/ppp_unit/documents/contracts/4g_network_signed_contract.pdf",
        "language": "en",
        "unofficialTranslations": [
          "it"
        ],
        "pageStart": "334",
        "pageEnd": "336",
        "accessDetails": "This document can only be accessed by visiting the PPP unit office by appointment. Please see the PPP unit website for further details.",
        "accessDetailsURL": "http://example.com/ppp_unit/registration/",
        "author": "Contract department, PPP unit"
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-08-04

- Change unofficialTranslation field to `unofficialTranslations` array of languages.

### 2023-04-05

- Add `accessDetailsURL` and unofficialTranslation fields.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-04-15

- Improve documentation
- Use non-normative keywords where appropriate

### 2019-01-30

- Remove obsolete `mergeStrategy` properties
