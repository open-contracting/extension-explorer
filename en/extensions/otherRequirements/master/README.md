# Other Requirements

Adds an object to describe other requirements to participate in a contracting process.

## Guidance

If you are using the [Lots extension](https://extensions.open-contracting.org/en/extensions/lots/master/), [follow its guidance](https://extensions.open-contracting.org/en/extensions/lots/master/#guidance) on whether to use `tender.lots` fields or `tender` fields.

## Legal context

In the European Union, this extension's fields correspond to [eForms BG-705 (Other Requirements)](https://docs.ted.europa.eu/eforms/latest/reference/business-terms/), although not all the fields have been implemented yet. For correspondences to Tenders Electronic Daily (TED), see [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/).

## Example

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

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-03-09

- Add `OtherRequirements.securityClearance` field.

### 2022-03-09

- Add `items` to the `OtherRequirements.qualificationSystemConditions` and `OtherRequirements.qualificationSystemMethods` objects.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

This extension was originally discussed as part of the [OCDS for EU profile](https://github.com/open-contracting-extensions/european-union/issues) and in [pull requests](https://github.com/open-contracting-extensions/ocds_otherRequirements_extension/pulls?q=is%3Apr+is%3Aclosed).
