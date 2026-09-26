# Exclusion grounds

Adds an object to describe the criteria to exclude tenderers from participating in a contracting process.

## Guía

If you use a codelist for `tender.exclusionGrounds.criteria.type`, you should explain where the codes are from in your publication policy/user guide.

## Ejemplo

```json
{
  "tender": {
    "id": "1",
    "exclusionGrounds": {
      "criteria": [
        {
          "description": "Applicants not satisfying...",
          "type": "crime-org"
        }
      ]
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
