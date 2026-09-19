# Implementation Status

## Description:

In Mexico, when talking about works and services related with them it is necessary to publish a set of specific variables about its implementation. One of them is the implementation status of the work or service related with it. It includes a code list whose values are the following:

- planning
- ongoing
- concluded

## Proposal:

Add a new field named “implementationStatus” in the “Implementation” object.

### Schema

- Implementation {object}
  - status (string, null) (codelist)

## Defining texts:

**Code** | **Title** | **Description**
--|--|--
status | Implementation status | The current status of the contract implementation based on the [implementationStatus](https://github.com/INAImexico/ocds_implementationStatus_extension/blob/master/codelists/implementationStatus.csv)  codelist.
planning | Planning | The contract has been signed, but the provision or construction of the goods, services or works has not started.
ongoing | Ongoing | The provision or construction of the goods, services or works is in progress.
concluded | Concluded | The provision or construction of the goods, services or works has officially ended.

## Issues

Report issues for this extension in the [standard repository](https://github.com/open-contracting/standard/issues/624) of the Open Contracting Partnership.
