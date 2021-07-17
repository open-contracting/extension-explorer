# Asignación de riesgos

El [marco para la divulgación de APP](http://pubdocs.worldbank.org/en/773541448296707678/Disclosure-in-PPPs-Framework.pdf) exige información individual sobre la asignación de riesgos.

La extensión de asignación de riesgos se usa para dar datos estructurados sobre la asignación de riesgos que se define en un contrato de una asociación público privada.

## Resumen

Las asignaciones de riesgo pueden representarse mediante una matriz de objetos `Risk` en el campo `riskAllocation` de la sección `contracts` de un comunicado OCDS.

La categoría de riesgo puede representarse mediante el campo `Risk.category` utilizando los valores de la lista de códigos `riskCategory.csv` basada en el Programa de Certificación APMG PPP. La columna "Categoría" de la lista de códigos indica la fase o el aspecto del proceso de contratación al que se aplica la categoría de riesgo.

La parte que retiene cada riesgo debe representarse mediante el campo `Risk.allocation` utilizando los valores de la lista de códigos `riskAllocation.csv`.

La descripción del riesgo debe proporcionarse como texto libre utilizando el campo `Risk.description`.

Se puede proporcionar información adicional de texto libre sobre el riesgo utilizando el campo `Risk.notes`.

## Ejemplo

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Public Private Partnership Agreement",
      "description": "Public-Private Partnership agreement entered into by and between telecoms promoter, together with national fibre infrastructure and the special purpose vehicle Mega Consortium Ltd",
      "riskAllocation": [
        {
          "id": "1",
          "category": "compliance",
          "description": "Risks deriving from the compliance or lack thereof of regulatory obligations related to the development of the Project",
          "allocation": "privateParty"
        },
        {
          "id": "2",
          "category": "construction",
          "description": "Risks deriving from procurement or lack thereof of the necessary licenses and permits for the Project’s development",
          "allocation": "privateParty"
        },
        {
          "id": "3",
          "category": "construction",
          "description": "Risks arising from the procurement or lack thereof of rights of way required for the Project’s development",
          "allocation": "privateParty"
        }
      ]
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Revisar de las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2018-05-08

- Hacer que `Risk.id` sea obligatorio para soportar el seguimiento de revisiones y [fusión de listas](http://standard.open-contracting.org/latest/es/schema/merging/#lists)
