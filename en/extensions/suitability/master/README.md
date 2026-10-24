# Suitability

Adds a suitability object to the tender, lot and lot group objects to describe their suitability to different types of tenderers.

# Guidance

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#usage) on whether to use `tender.lots` fields or `tender` fields.

## Legal context

In the European Union, this extension's fields correspond to [eForms BT-726 (Suitable For SMEs)](https://github.com/eForms/eForms). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Examples

### Tender

```json
{
  "tender": {
    "id": "1",
    "suitability": {
      "sme": true
    }
  }
}
```

### Lot

```json
{
  "tender": {
    "id": "1",
    "lots": [
      {
        "id": "1",
        "suitability": {
          "sme": true
        }
      }
    ]
  }
}
```

### Lot group

```json
{
  "tender": {
    "id": "1",
    "lotGroups": [
      {
        "id": "1",
        "suitability": {
          "sme": true
        }
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
