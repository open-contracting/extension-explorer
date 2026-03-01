# Fecha de publicación de la licitación

Esta extensión agrega un campo para indicar explícitamente la fecha y hora en que se publicó la licitación. Este campo puede ser diferente de los campos  `tender/tenderPeriod/startDate` y `date`.

## Uso

Tener esta información de manera fácil de acceder puede tener muchos beneficios, por ejemplo, poder computar algunos indicadores que dirán cuántos días tiene un potencial oferente para preparar una oferta.

Para satisfacer tales casos de uso, se debe utilizar el campo `tender/datePublished`.

## Ejemplo

```json
{
  "tender": {
    "datePublished": "2019-07-23T1:27:10.673000-06:00"
  }
}
```

## Registro de cambios

Esta extensión se discutió originalmente en <https://github.com/open-contracting/standard/issues/892>.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
