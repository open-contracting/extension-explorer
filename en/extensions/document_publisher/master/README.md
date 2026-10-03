# Document publisher

Adds a publisher field to the document object and an 'informationService' role to indicate the organization responsible for making the document available.

## Usage

For each organization referenced by a `Document.publisher` field, add the 'informationService' code to its `roles` array.

## Legal context

In the European Union, this extension's fields correspond to [eForms OPT-301 (Party ID reference)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Example

```json
{
  "parties": [
    {
      "id": "ORG-0001",
      "roles": [
        "informationService"
      ]
    }
  ],
  "tender": {
    "id": "1",
    "documents": [
      {
        "id": "1",
        "publisher": {
          "id": "ORG-0001"
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
