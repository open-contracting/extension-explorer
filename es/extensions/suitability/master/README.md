# Idoneidad

Adds a suitability object to the tender, lot and lot group objects to describe their suitability to different types of tenderers.

# Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#usage) on whether to use `tender.lots` fields or `tender` fields.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-726 (Suitable For SMEs)](https://github.com/eForms/eForms). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/).

## Ejemplos

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

### Grupo del lote

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

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
