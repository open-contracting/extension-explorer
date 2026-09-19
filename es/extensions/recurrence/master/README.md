# Recurrencia

Esta extensión agrega campos de información sobre la recurrencia del proceso de contratación.

"Recurrence" means another contracting process for the same goods, services or works is likely to occur. This is not the same as awarding multiple contracts within a [framework agreement](https://standard.open-contracting.org/latest/en/guidance/map/framework_agreements/).

A company might, for example, use this information to decide to invest in the machinery they would need to compete for the potential future contract.

## Contexto legal

El \[Revised Agreement on Government Procurement\] (https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) incluye: "cada aviso de contratación prevista deberá incluir ... c. para los contratos recurrentes, una estimación, si es posible, del calendario de avisos posteriores de contratación prevista".

La Unión Europea es una [parte](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) al GPA, y como tal su [Directiva 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Contratos públicos - que establecen reglas básicas claras) incluye: "Parte C: Información que se incluirá en los avisos de contrato ... 27. En el caso de adquisiciones periódicas, tiempo estimado para que se publiquen más avisos".

This extension's fields correspond to [eForms BT-94 (Recurrence) and BT-95 (Recurrence Description)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/).

## Ejemplo

```json
{
  "tender": {
    "hasRecurrence": true,
    "recurrence": {
      "dates": [
        {
          "startDate": "2020-01-01T00:00:00Z"
        },
        {
          "startDate": "2021-01-01T00:00:00Z"
        }
      ],
      "description": "The duration of this contract and recurrent contracts will not exceed three years."
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

El borrador original de la extensión se puede encontrar en el [repositorio archivado de perfiles comerciales](https://github.com/open-contracting-archive/trade/tree/master/draft_extensions/lot_RecurrentProcurement)
