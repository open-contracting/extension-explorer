# Cubierto por

This extension adds a field to indicate the international legal instruments that the contracting process is covered by.

For example, the Agreement on Government Procurement (GPA) is a treaty that requires members to indicate whether a contracting process is covered by it. The Clean Vehicles Directive is a legal act that provides for member states of the European Union to indicate associated information in procurement notices. The `coveredBy` field should be used to meet such requirements.

Para revelar las leyes o reglamentos que rigen el proceso de contratación y que otorgan autoridad legal a la entidad contratante, utilice la [extensión legalBasis](https://github.com/open-contracting-extensions/ocds_legalBasis_extension) en vez.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

Si necesita hacer referencia a un tratado que no está en el lista de códigos `coveredBy`:

1. Si el tratado tiene un alcance nacional o subnacional, elegir un código de país relevante [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (por ejemplo "CA" para Canadá).
1. Si el tratado tiene un alcance subnacional, elegir un código de región relevante \[ISO 3166-2 region code\] (https://en.wikipedia.org/wiki/ISO_3166-2) (por ejemplo "NT" para [Northern Territories](https://en.wikipedia.org/wiki/ISO_3166-2:CA#Current_codes), una provincia de Canadá).
1. Concatenate the code(s) to the acronym of the treaty, separating each part with a dash (e.g "CA-NT-BIP").
1. Add this code to the `coveredBy` array.
1. Documentar el nuevo código (ver [Extending open codelists](https://standard.open-contracting.org/latest/en/schema/codelists/)).

## Contexto legal

El [Revised Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) incluye: "cada aviso de contratación prevista deberá incluir ... l. una indicación que la contratación está cubierta por este Acuerdo".

La Unión Europea es una [parte](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) al GPA, y como tal su [Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Contratos públicos - que establecen reglas básicas claras) incluye: "Parte C: Información que debe incluirse en los avisos de contrato ... 29. Indicación de si el contrato está cubierto por GPA".

## Ejemplo

The `coveredBy` field is an array of strings, whose values are selected from the `coveredBy.csv` open codelist.

### Tender

```json
{
  "tender": {
    "coveredBy": [
      "GPA"
    ]
  }
}
```

### Lot

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "coveredBy": [
          "EU-CVD"
        ]
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-10-08

- Add 'EU-FSR' code to the `coveredBy` codelist.

### 2024-02-07

- Add 'CPTPP' code to the `coveredBy` codelist.

### 2023-03-02

- Add 'EU-CVD' code to the `coveredBy` codelist.
- Add `coveredBy` to the `Lot` object.

### 2020-11-04

- Agregar guía acerca de la creación de nuevos códigos para la lista de códigos `coveredBy`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.
