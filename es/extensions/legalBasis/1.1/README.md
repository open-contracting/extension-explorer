# Base legal

Agregar campos al objeto de licitación para describir la base legal del proceso de contratación – es decir, las leyes y reglamentos que rigen el proceso de contratación y que otorgan autoridad legal a la entidad contratante.

El campo `tender.legalBasis` es un objeto de `Classification`. Ejemplos de esquemas de clasificación son [LEX](<https://en.wikipedia.org/wiki/Lex_(URN)>), [CELEX](https://eur-lex.europa.eu/content/help/faq/intro.html#help8) y \[ELI\] (https://es.wikipedia.org/wiki/Identificador_Europeo_de_Legislación)

Para identificar el procedimiento utilizado, ya sea por nombre formal o por citación legal, utilice el campo [`tender.procurementMethodDetails`](https://standard.open-contracting.org/latest/es/schema/reference/#release-schema.json,/definitions/Tender,procurementMethodDetails).

Para indicar si el proceso de contratación está cubierto por un tratado, como el Agreement on Government Procurement (GPA), usar la extensión [coveredBy](https://extensions.open-contracting.org/es/extensions/coveredBy/). Para indicar si el proceso de contratación es acelerado, involucra acuerdos marco o tiene otras modalidades, [echar un vistazo a las extensiones](https://extensions.open-contracting.org/).

## Guía

Si la base legal es específica de un país, se recomienda anteponer el prefijo [ISO 3166-1 alpha-2 code](https://es.wikipedia.org/wiki/ISO_3166-1_alfa-2) al esquema de clasificación: por ejemplo, "HN-ONCAE" para la Oficina Normativa de Contratación y Adquisiciones del Estado (ONCAE) en Honduras.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-01 (Procedure Legal Basis), BT-09 (Cross Border Law)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/) and [Article 39, paragraph 5 of Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1585836130257&uri=CELEX:32014L0024#d1e4669-65-1). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "tender": {
    "crossBorderLaw": "Italian procurement legislation",
    "legalBasis": {
      "id": "32014L0025",
      "scheme": "CELEX"
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-08-01

- Add 'ELI' code to the `+itemClassificationScheme.csv` codelist patch.

### 2021-01-19

- Agregar orientación sobre la elección del esquema de clasificación para la base legal específica del país.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), y en [pull resquests](https://github.com/open-contracting-extensions/ocds_contractTerms_extension/pulls?q=is%3Apr+is%3Aclosed).
