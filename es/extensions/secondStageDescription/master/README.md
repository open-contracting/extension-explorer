# Descripción de la segunda etapa

Agregar un objeto de segunda etapa a los objetos de licitación y lote, para describir la segunda etapa de un procedimiento de dos etapas. En particular, agregar dos campos para describir los límites en el número de candidatos a ser invitados.

## Guía

Si hay un límite exacto en el número de candidatos, establecer `minimumCandidates` y maximumCandidates\` al mismo número.

Si se establece `maximumCandidates`, utilizar la extensión de criterios de selección (TBD) para describir cómo se utilizarán los criterios de selección para seleccionar candidatos que serán invitados a la segunda etapa.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-709 (Second Stage)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "tender": {
    "lots": [
      {
        "id": "1",
        "secondStage": {
          "minimumCandidates": 5,
          "maximumCandidates": 50,
          "successiveReduction": true,
          "noNegotiationNecessary": false,
          "invitationDate": "2019-08-16T10:30:00Z"
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en \[pull requests\] (https://github.com/open-contracting-extensions/ocds_secondStageDescription_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/695>.
