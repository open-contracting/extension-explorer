# Procurement method rationale classifications

Adds an array to the tender object to classify the procurement method rationale.

## Legal context

En la unión Europea, esta extensión de campo corresponde a [eForms BT-135, BT-136](https://github.com/eForms/eForms). Ver [OCDS para la unión Europea](http://standard.open-contracting.org/profiles/eu/master/en/) para lo correspondiente a las Tenders Electronic Daily (TED).

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

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_procurementMethodRationaleClassifications_extension/pulls?q=is%3Apr+is%3Aclosed).
