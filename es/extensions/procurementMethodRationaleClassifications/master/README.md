# Clasificaciones de los fundamentos de métodos de contratación

Agregar una lista al objeto de licitación para clasificar la justificación del método de contratación.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BT-136 (Direct Award Justification Code)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to eForms fields, see [OCDS for eForms](https://standard.open-contracting.org/profiles/eforms/latest/en/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

```json
{
  "tender": {
    "procurementMethodRationaleClassifications": [
      {
        "id": "D_NO_TENDERS_REQUESTS",
        "description": "No tenders or no suitable tenders/requests to participate in response to a procedure with prior call for competition",
        "scheme": "TED_PT_AWARD_CONTRACT_WITHOUT_CALL"
      },
      {
        "id": "D_FROM_LIQUIDATOR_CREDITOR",
        "description": "Purchase of supplies or services on particularly advantageous terms from the liquidator in an insolvency procedure, an arrangement with creditors or a similar procedure under national laws and regulations",
        "scheme": "TED_PT_AWARD_CONTRACT_WITHOUT_CALL"
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-04-05

- Add 'eu-direct-award-justification' code to the `+itemClassificationScheme.csv` codelist patch.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_procurementMethodRationaleClassifications_extension/pulls?q=is%3Apr+is%3Aclosed).
