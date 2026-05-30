# Guarantees

## Description:

Some procurement processes consider the specification of guarantees in order to ensure compliance with the terms of a contract.

There are many types of guarantees, so we consider the creation of a new extension based on the formats that are required for the Federal Treasury (Mexico).

## Proposal:

### Codelist

- Guarantee types:

  - Bail
  - Deposit slip
  - Letter of credit
  - Surety bond
  - Check

- Guaranteed obligations:

  - Fulfillment
  - Prepaid
  - Latent defects
  - Confidentiality
  - Quality

Add an array named "guarantees" with the following fields:

### Schema

- Contract {object}
  - guarantees \[array\]
    - Guarantee {object}
      - id (string, integer)
      - type (string, null) (codelist)
      - date (Format: date-time) (string, null)
      - obligations (string, null) (codelist)
      - value {object}
        - $ref : #/definitions/Value
      - guarantor  {object}
        - $ref : #/definitions/OrganizationReference
      - period {object}
        - $ref : #/definitions/Period

## Defining texts:

**Code** | **Title** | **Description**
--|--|--
guarantees | Guarantees | A list of the guarantees given for this contract.
Guarantee | Guarantee | Information of the guarantee used to ensure compliance with the terms of a contract.
id | Guarantee ID | A local identifier for this guarantee, unique within this block.
type | Guarantee type | Specify the guarantee type for this contract using the [guaranteeType](https://github.com/INAImexico/ocds_guarantees_extension/blob/master/codelists/guaranteeType.csv) codelist.
bail | Bail | A bail bond is a written promise by which a person agrees with the creditor to pay for the debtor, if he does not.
depositSlip | Deposit slip | The deposit slip is an instrument used to establish cash guarantees available to judicial or administrative authorities.
letterOfCredit | Letter of credit | Letters of credit are used to guarantee that a supplier will receive a specified amount of money within a specified time providing strict terms.
suretyBond | Surety bond | A surety bond is an instrument through which The surety is obliged to compensate the obligee for the damages suffered in the event that the principal fails to comply with the terms of the contract.
check | Check | A certified check as a form of guarantee.
date | Guarantee date | The date of the guarantee. This is the date on which the guarantee is issued.
obligations | Guaranteed obligations | Specify the type of obligations that are guaranteed, using the [obligationType](https://github.com/INAImexico/ocds_guarantees_extension/blob/master/codelists/guaranteedObligations.csv) codelist.
fulfillment | Fulfillment | Guarantees fulfillment in time with the conditions stipulated in the contract.
prepaid | Prepaid | Guarantee by which the supplier requests a prepayment from the procuring entity.
latentDefects | Latent defects | Guarantee on the possible defects that a good may have that are not discoverable through general inspection at the time of delivery.
confidentiality | Confidentiality | Guarantee that commits the supplier to safeguard the confidential information that has been granted.
quality | Quality | Commitment from the supplier to deliver the goods and services in the quality specified in the contract.
value | Guarantee value | Total amount of the guarantee.
guarantor | Guarantor | Institution that issues the guarantee.
period | Guarantee period | The period on which this quote is valid.

## Issues

Report issues for this extension in the [standard repository](https://github.com/open-contracting/standard/issues/651) of the Open Contracting Partnership.
