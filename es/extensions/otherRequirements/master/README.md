# Otros requisitos

Agregar un objeto para describir otros requisitos para participar en un proceso de contratación.

## Guía

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Contexto legal

In the European Union, this extension's fields correspond to [eForms BG-705 (Other Requirements)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/), although not all the fields have been implemented yet. For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Ejemplo

### Tender

```json
{
  "tender": {
    "otherRequirements": {
      "requiresStaffNamesAndQualifications": true,
      "reservedParticipation": [
        "shelteredWorkshop"
      ],
      "qualificationSystemConditions": [
        "The candidates are required to comply with all the technical and financial requisites listed on the National Procurement portal: https://procurement.example.org/requisites",
        "The candidates are required to create an electronic profile on https://procurement.example.org."
      ],
      "qualificationSystemMethods": [
        "Pre-qualification questionnaire",
        "Standard test, based on the results of the pre-qualification questionnaire"
      ],
      "reductionCriteria": "The candidates will be selected according to their technical, financial and legal capacity to undertake the works described in the present notice. More details on the criteria can be found in section 4.3 of the PCG.",
      "securityClearance": "EU Confidential security clearance of Key Management Personnel must be achieved before access to procurement documents be granted"
    }
  }
}
```

### Lot

```json
{
  "tender": {
    "lots": [
      {
        "id": "LOT-0001",
        "otherRequirements": {
          "requiresStaffNamesAndQualifications": true,
          "reservedParticipation": [
            "shelteredWorkshop"
          ],
          "qualificationSystemConditions": [
            "The candidates are required to comply with all the technical and financial requisites listed on the National Procurement portal: https://procurement.example.org/requisites",
            "The candidates are required to create an electronic profile on https://procurement.example.org."
          ],
          "qualificationSystemMethods": [
            "Pre-qualification questionnaire",
            "Standard test, based on the results of the pre-qualification questionnaire"
          ],
          "reductionCriteria": "The candidates will be selected according to their technical, financial and legal capacity to undertake the works described in the present notice. More details on the criteria can be found in section 4.3 of the PCG.",
          "securityClearance": "EU Confidential security clearance of Key Management Personnel must be achieved before access to procurement documents be granted"
        }
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-03-09

- Add `OtherRequirements.securityClearance` field.

### 2022-03-09

- Add `items` to the `OtherRequirements.qualificationSystemConditions` and `OtherRequirements.qualificationSystemMethods` objects.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues) y en [pull requests](https://github.com/open-contracting-extensions/ocds_otherRequirements_extension/pulls?q=is%3Apr+is%3Aclosed).
