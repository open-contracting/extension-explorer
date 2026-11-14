# Financiamiento

Agrega campos para revelar la financiación de todo el proceso y sus contratos individuales.

A veces, sobre todo en el caso de las asociaciones público-privadas, los contratos se financian con una serie de instrumentos, como préstamos, subvenciones, emisión de acciones, etc. Esta información puede actualizarse a lo largo de la vida del contrato.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-611 (Contract EU funds) and BG-61 (EU funds)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/). For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplos

### Financiamiento del proceso de contratación

```json
{
  "planning": {
    "budget": {
      "finance": [
        {
          "id": "1",
          "financingParty": {
            "id": "1",
            "name": "Development Bank of South Africa"
          },
          "financingPartyType": "bilateral",
          "source": "Green Climate Fund",
          "assetClass": [
            "debt"
          ],
          "type": "loan",
          "repaymentPriority": "senior",
          "concessional": false,
          "resultsBased": false
        }
      ]
    }
  }
}
```

### Financiamiento de contratos de Asociación público-privada

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "title": "Public Private Partnership Agreement",
      "description": "Public-Private Partnership agreement entered into by and between telecoms promoter, together with national fibre infrastructure and the special purpose vehicle Mega Consortium Ltd",
      "finance": [
        {
          "id": "1",
          "title": "Primary senior debt financing agreement",
          "description": "Big Bank Corp retains the right to step in should Mega Consortium fail to comply with the repayment schedule for a period of 3 consecutive months.",
          "financingParty": {
            "id": "XX-FI-22222222",
            "name": "Big Bank Corp"
          },
          "assetClass": [
            "debt"
          ],
          "type": "loan",
          "repaymentPriority": "senior",
          "value": {
            "amount": 41000000,
            "currency": "USD"
          },
          "period": {
            "startDate": "2016-01-24T00:00:00Z",
            "endDate": "2021-01-23T00:00:00Z"
          },
          "interestRate": {
            "base": "LIBOR",
            "margin": 0.03,
            "fixed": false
          },
          "stepInRights": true,
          "exchangeRateGuarantee": false,
          "paymentFrequency": 30.4
        },
        {
          "id": "2",
          "title": "Alpha Holdings equity investment",
          "financingParty": {
            "id": "XX-XXX-11111111",
            "name": "Alpha Holdings Ltd"
          },
          "assetClass": [
            "equity"
          ],
          "value": {
            "amount": 6674000,
            "currency": "USD"
          }
        }
      ]
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-11-22

- Reorder fields in logical order.

### 2023-11-13

- Replace fields, to clarify semantics:
  - Replace `Finance.financeType` (`financeType.csv`) with `Finance.financingPartyType` (`financingPartyType.csv`) and `Finance.type` (`financingArrangementType.csv`). Notably:
    - 'publicBondIssue' is replaced by 'debt' in `assetClass.csv` and 'bond' in `financingArrangementType.csv`
    - 'supplierCredit' is replaced by 'vendor' in `financingPartyType.csv`
  - Replace `Finance.financeCategory` (`financeCategory.csv`) with `Finance.assetClass` (`assetClass.csv`), `Finance.type` (`financingArrangementType.csv`) and `Finance.repaymentPriority` (`debtRepaymentPriority.csv`). Notably:
    - 'equity' is replaced by 'equity' in `assetClass.csv`
    - 'seniorDebt' is replaced by 'debt' in `assetClass.csv` and 'senior' in `debtRepaymentPriority.csv`
    - 'mezzanineDebt' is replaced by 'debt' and 'equity' in `assetClass.csv` and 'subordinated' in `debtRepaymentPriority.csv`
    - 'grant' is replaced by 'grant' in `financingArrangementType.csv`
    - 'guarantee' is replaced by 'guarantee' in `financingArrangementType.csv`
  - Replace `Finance.repaymentFrequency` with `Finance.paymentFrequency`.
- Add fields:
  - `Finance.concessional`
  - `Finance.paymentPeriod`
  - `Finance.resultsBased`
  - `Finance.source`
- Update descriptions, for clarity:
  - `Budget.finance`
  - `Contract.finance`
  - `Finance`
  - `Finance.description`
  - `Finance.period`

### 2022-05-17

- Move `Finance.relatedLots` from the Lots extension

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-17

- Agregar el campo `planning.budget.finance`.
- Fix description of `Finance.financeCategory`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `interestRate` no nulo (deshacer el cambio anterior).

### 2018-05-08

- Make `Finance.id` required and non-nullable to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-05-01

- Agregar título y descripción a `Finance.financingParty`.

### 2018-01-29

- Se permite que `interestRate` sea nulo.
