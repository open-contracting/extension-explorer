# Beneficiarios finales

Agregar una lista de beneficiarios finales al objeto organización para indicar los beneficiarios finales de una organización.

If beneficial ownership (BO) information is collected via contracting processes, then this extension is appropriate: for example, if tenderers are obligated to disclose their beneficial owners within their bid submission. Similarly, to use this extension, the **laws in your jurisdiction must permit the publication of personal identifiers**.

You can find the complete guidance on publishing personal identifiers in the [Beneficial Ownership Data Standard documentation](https://standard.openownership.org/en/0.3.0/schema/guidance/identifiers.html#shared-identifiers)

Por otro lado, si la información de beneficiarios finales se recoge en un registro central por otros medios, se recomienda publicar esa información como un conjunto de datos separados. El conjunto de datos de beneficiarios finales y el conjunto de datos OCDS deben [identificar las organizaciones](https://standard.open-contracting.org/latest/en/schema/identifiers/#organization-ids) de la misma manera, para que los usuarios puedan cruzar los conjuntos de datos. El conjunto de datos de Beneficiarios Finales puede seguir el [Estándar de Datos sobre Beneficiarios Finales](https://standard.openownership.org/en/latest/).

## Ejemplo

### With nationality

The beneficial owner's nationality is disclosed.

```json
{
  "parties": [
    {
      "id": "AHL",
      "name": "Alpha Holdings Ltd",
      "beneficialOwners": [
        {
          "id": "1",
          "name": "Juan Perez",
          "identifier": {
            "scheme": "PRY-IDCARD",
            "id": "12345"
          },
          "nationalities": [
            "PY"
          ],
          "address": {
            "streetAddress": "Avenida Eusebio Ayala 1347",
            "locality": "Asunción",
            "region": "Gran Asunción",
            "postalCode": "1001",
            "countryName": "Paraguay"
          },
          "email": "jperez@example.com",
          "faxNumber": "+595210000001",
          "telephone": "+595210000000"
        }
      ]
    }
  ]
}
```

### Without nationality

The beneficial owner's nationality is not disclosed because the organization is listed on a regulated market (e.g. a stock exchange) that ensures adequate transparency in line with anti-money laundering legislation.

```json
{
  "parties": [
    {
      "id": "AHL",
      "name": "Alpha Holdings Ltd",
      "beneficialOwners": [
        {
          "id": "1",
          "name": "Juan Perez",
          "identifier": {
            "scheme": "PRY-IDCARD",
            "id": "12345"
          },
          "address": {
            "streetAddress": "Avenida Eusebio Ayala 1347",
            "locality": "Asunción",
            "region": "Gran Asunción",
            "postalCode": "1001",
            "countryName": "Paraguay"
          },
          "email": "jperez@example.com",
          "faxNumber": "+595210000001",
          "telephone": "+595210000000"
        }
      ],
      "details": {
        "listedOnRegulatedMarket": true
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-08-04

- Replace `nationality` string with `nationalities` array.

### 2023-06-07

- Add a `country.csv` codelist for `nationality`.

### 2023-02-27

- Add fields:
  - `Person.address`
  - `Person.email`
  - `Person.faxNumber`
  - `Person.telephone`
  - `Organization.details.listedOnRegulatedMarket`
