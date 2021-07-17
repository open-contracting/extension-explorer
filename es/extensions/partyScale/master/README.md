# Detalles de las partes - Escala

This extension adds a `scale` field to the `parties.details` object, to indicate the size or scale of an organization, in particular commercial enterprises or economic operators.

This information can be used to calculate procurement statistics, like the share of contracts awarded to micro, small and medium-sized enterprises.

The codes in the `partyScale.csv` codelist do not have precise definitions, and instead defer to local laws and regulations, for example:

- [OECD: Small and Medium-Sized Enterprises (SMEs) definition](https://stats.oecd.org/glossary/detail.asp?ID=3123)
- [European Commission: What is an SME?](https://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition_en)

## Guía

For small and medium-sized enterprises, if you can distinguish between the two sizes, use the 'small' and 'medium' codes. Otherwise, use the 'sme' code.

For self-employed individuals and sole traders, if you can distinguish them from micro enterprises, use the 'selfEmployed' code. Otherwise, use the 'micro' code.

For enterprises without employees, use the 'micro' code.

## Ejemplo

```json
{
  "parties": [
    {
      "id": "GB-COH-1234567844",
      "name": "AnyCorp Cycle Provision",
      "details": {
        "scale": "sme"
      }
    }
  ]
}
```

## Registro de cambios

### 2020-05-20

- Add 'selfEmployed' code to `partyScale.csv`

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-03-11

- Clarify use of codes

### 2020-03-10

- Add 'small' and 'medium' codes to `partyScale.csv`

### 2018-05-22

- Add description to 'large' code in `partyScale.csv`

### 2018-05-21

- Remove '' code from `partyScale.csv`

### 2018-01-09

- Add partyScale.csv codelist for `Organization.details.scale`

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
