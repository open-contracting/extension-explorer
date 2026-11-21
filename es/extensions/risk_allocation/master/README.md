# Asignación de riesgos

The [framework for disclosure in PPPs](https://thedocs.worldbank.org/en/doc/773541448296707678-0100022015/original/DisclosureinPPPsFramework.pdf) calls for individual risk allocation information.

La extensión de asignación de riesgos se utiliza para proporcionar datos estructurados sobre las asignaciones de riesgo definidas en un contrato de asociación público-privada, a través de una lista de `contracts.riskAllocation`.

La lista de códigos `riskCategory.csv` se basa en el programa de certificación APMG PPP. La columna Category (Categoría) de la lista de códigos indica la fase o el aspecto del proceso de contratación al que se aplica la categoría de riesgo.

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

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Agregar `"minLength": 1` en los campos de cadena obligatorios.

### 2018-05-08

- Make `Risk.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)
