# Extensión de financiamiento

Agregar campos para revelar la financiación de todo el proceso y sus contratos individuales.

A veces, sobre todo en el caso de las asociaciones público-privadas, los contratos se financian con una serie de instrumentos, como préstamos, subvenciones, emisión de acciones, etc. Esta información puede actualizarse a lo largo de la vida del contrato.

## Contexto legal

En la Union Europea, los campos de esta extensión corresponden [eForms BG-611 (Contract EU funds) y BG-61 (EU funds)](https://github.com/eForms/eForms). Vea [OCDS para la Union Europea](http://standard.open-contracting.org/profiles/eu/master/en/) para lo correspondiente a Tenders Electronic Daily (TED).

## Listas de códigos

La lista de códigos `financeType.csv` se basa en la lista de [Página 57 del Marco de divulgación de APP del Banco Mundial](http://pubdocs.worldbank.org/en/143671469558797229/FrameworkPPPDisclosure-071416.pdf#page=57)

## Examples

### Procurement process financing

```json
{
  "planning": {
    "budget": {
      "description": "Adquisición de equipos odontológicos para las Unidades de Salud de la Familia",
      "amount": {
        "currency": "PYG",
        "amount": 643702500
      },
      "finance": [
        {
          "id": "1",
          "title": "Presupuesto de financiación de deuda primaria",
          "financingParty": {
            "id": "XX-FI-22222222",
            "name": "Banco Interamericano de Desarrollo (BID)"
          },
          "financeCategory": "seniorDebt",
          "financeType": "multilateral",
          "value": {
            "amount": 643702500,
            "currency": "PYG"
          }
        }
      ]
    }
  }
}
```

### Public-private partnership contract financing

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
          "financeCategory": "seniorDebt",
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
          "repaymentFrequency": 30.4
        },
        {
          "id": "2",
          "title": "Alpha Holdings equity investment",
          "financingParty": {
            "id": "XX-XXX-11111111",
            "name": "Alpha Holdings Ltd"
          },
          "financeCategory": "equity",
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

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-17

- Agregar el campo `planning.budget.finance`.
- Arreglar la descripción de `financeCategory`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.
- Hacer `interestRate` no nulo (deshacer el cambio anterior).

### 2018-05-08

- Hacer `Finance.id` requerido y no nulo para soportar el seguimiento de revisiones y [list merging](http://standard.open-contracting.org/latest/es/schema/merging/#lists)

### 2018-05-01

- Agregar título y descripción a `Finance.financingParty`.

### 2018-01-29

- Se permite que `interestRate` sea nulo.
