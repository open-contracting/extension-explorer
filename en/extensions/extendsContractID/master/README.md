# extendsContractID

Under some procurement rules and processes, to extend the duration or value of a contract, or to make other substantial alterations, requires a new contract to be signed.

This new contract will form part of the same overall contracting process as the old contract which it extends.

In these cases, the `extendsContractID` field can be used to identify that a given entry in the `contracts` array should be understood as related to a previous contract.

Use this extension **only if** there is a substantive new contract signed as the extension of a previous contract. In most cases, an update to the value or duration of a contract should be modelled as an amendment within a single entry in the `contracts` array.

## Example

The extract below shows three contracts in the contracts array of an OCDS release.

The first two contracts were signed in 2011: one for one year for property rental, and the other for two years for services related to property rental.

The third contract was signed in 2012, and renews the property rental for another year. This is related back to the contract for the first year of rental with the `extendsContractID` field.

```json
{
  "contracts": [
    {
      "id": "207002-armin-hahner-stollmaier-21",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "title": "Alquileres para la SNNA",
      "status": "terminated",
      "period": {
        "startDate": "2011-01-02T23:59:59+00:00",
        "endDate": "2012-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 1800000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "01",
          "description": "Alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2011-03-14T16:58:40+00:00"
    },
    {
      "id": "207004-armin-hahner-stollmaier-21-service",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "title": "Servicios relacionados con alquileres para la SNNA",
      "status": "active",
      "period": {
        "startDate": "2011-01-02T23:59:59+00:00",
        "endDate": "2013-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 10000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "02",
          "description": "Servicios relacionados con alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2011-03-14T16:58:40+00:00"
    },
    {
      "id": "207002-armin-hahner-stollmaier-21-renovacion",
      "awardID": "207002-armin-hahner-stollmaier-21",
      "extendsContractID": "207002-armin-hahner-stollmaier",
      "title": "Ad Referendum - Alquileres para la SNNA (Amends contract 207002)",
      "status": "active",
      "period": {
        "startDate": "2012-01-02T23:59:59+00:00",
        "endDate": "2013-01-02T23:59:59+00:00"
      },
      "value": {
        "amount": 12780000,
        "currency": "PYG"
      },
      "items": [
        {
          "id": "01",
          "description": "Alquiler de Inmueble",
          "classification": {
            "scheme": "CPV",
            "id": "70000000-1",
            "description": "Real Estate Services",
            "uri": "http://cpv.data.ac.uk/code-70000000"
          }
        }
      ],
      "dateSigned": "2012-03-14T16:58:40+00:00"
    }
  ]
}
```

The image below shows an example of how the information provided by the `extendsContractID` field is used in Paraguay, to display two contracts resulting from an award (the blue boxes), with one of those contracts then extended (the blue circle).

![Paraguay Example](https://cloud.githubusercontent.com/assets/342624/9915392/aecb1e52-5cae-11e5-9824-a6eb616e568b.png)

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-06-04

- Review normative and non-normative words.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2018-01-29

- Make `Contract.extendsContractID` nullable.
