# Organization scale

Esta extensión añade un campo `scale` al objeto`parties.details` para indicar el tamaño o la escala de una organización, en particular de empresas comerciales u operadores económicos.

Esta información se puede utilizar para calcular estadísticas de contrataciones, como la proporción de contratos adjudicados a micro, pequeñas y medianas empresas.

Los códigos de la lista de códigos `partyScale.csv` no tienen definiciones precisas y, en cambio, se rigen por las leyes y regulaciones locales, por ejemplo:

- [OECD: Pequeñas y medianas empresas definición (SMEs)](https://stats.oecd.org/glossary/detail.asp?ID=3123)
- [Comisión Europea: ¿Qué son las pequeñas y medianas empresas (SME)?](https://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition_en)

## Guía

Para las pequeñas y medianas empresas, si puede distinguir entre los dos tamaños, utilice los códigos 'small' y 'medium'.  De lo contrario, use el código 'sme'.

Para los trabajadores autónomos y los comerciantes individuales, si puede distinguirlos de las microempresas, utilice el código  'selfEmployed'. De lo contrario, use el código 'micro'.

Para empresas sin empleados, use el código 'micro'.

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

- Add 'selfEmployed' code to the `partyScale.csv` codelist.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-03-11

- Clarify use of codes.

### 2020-03-10

- Add 'small' and 'medium' codes to the `partyScale.csv` codelist.

### 2018-05-22

- Add Description to 'large' code in the `partyScale.csv` codelist.

### 2018-05-21

- Remove '' (blank) code from the `partyScale.csv` codelist.

### 2018-01-09

- Add a `partyScale.csv` codelist to `Organization.details.scale`.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
