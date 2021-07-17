# Tender Date Published

This extension adds a field to explicitly indicate the date and time when the tender was published. This field can be different from `tender/tenderPeriod/startDate` and `date` fields.

## Usage

Having this information in a easy way to access it can have many benefits, for instance, to be able to compute some indicators that will say how many days a potential bidder has to prepare an offer.

To satisfy such use cases, the `tender/datePublished` field should be used.

## Ejemplo

```json
{
  "tender": {
    "datePublished": "2019-07-23T1:27:10.673000-06:00"
  }
}
```

## Registro de cambios

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/892>.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
