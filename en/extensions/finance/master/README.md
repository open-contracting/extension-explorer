# Finance extension

Adds fields to disclose the financing of the whole process and its individual contracts.

Sometimes, particularly in the case of Public Private Partnerships, contracts are financed using a range of instruments, including loans, grants, share issues and so-on. This information can be updated over the lifetime of the contract.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-611 (Contract EU funds) and BG-61 (EU funds)](https://github.com/eForms/eForms). See [OCDS for the European Union](http://standard.open-contracting.org/profiles/eu/master/en/) for the correspondences to Tenders Electronic Daily (TED).

## Codelists

The `financeType.csv` codelist is based on the list on [Page 57 of the World Bank PPP Disclosure Framework](http://pubdocs.worldbank.org/en/143671469558797229/FrameworkPPPDisclosure-071416.pdf#page=57)

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

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-06-04

- Review normative and non-normative words.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-04-17

- Add `planning.budget.finance` field.
- Fix description of `financeCategory`.

### 2019-03-20

- Set `"uniqueItems": true` on array fields, and add `"minLength": 1` on required string fields.
- Make `interestRate` non-nullable (undo earlier change).

### 2018-05-08

- Make `Finance.id` required and non-nullable to support revision tracking and [list merging](http://standard.open-contracting.org/latest/en/schema/merging/#lists)

### 2018-05-01

- Add title and description to `Finance.financingParty`.

### 2018-01-29

- Make `interestRate` nullable.
