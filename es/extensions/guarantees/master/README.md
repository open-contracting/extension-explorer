# Garantías

## Descripción:

Algunos procesos de adquisiciones consideran la especificación de garantías para asegurar el cumplimiento de los términos de un contrato.

Existen muchos tipos de garantías, por lo que consideramos la creación de una nueva extensión en base a los formatos que se requieren para la Tesorería de la Federación (México).

## Propuesta:

### Lista de códigos

- Tipos de garantías:

  - Fianza
  - Comprobante de depósito
  - Carta de crédito
  - Fianza de garantía
  - Cheque

- Obligaciones garantizadas:

  - Cumplimiento
  - Pagado por adelantado
  - Defectos ocultos
  - Confidencialidad
  - Calidad

Agregar una matriz llamada "garantías" con los siguientes campos:

### Esquema

- Contrato {objeto}
  - garantías \[matriz\]
    - Garantía {objeto}
      - id (string, integer)
      - tipo (string, null) (lista de códigos)
      - fecha (Formato: fecha-hora) (string, null)
      - obligaciones (string, null) (lista de códigos)
      - valor {objeto}
        - $ref : #/definitions/Value
      - garante {objeto}
        - $ref : #/definitions/OrganizationReference
      - período {objeto}
        - $ref : #/definiciones/Periodo

## Textos definidos:

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

Informar problemas de esta extensión en el \[repositorio estándar\] (https://github.com/open-contracting/standard/issues/651) de Open Contracting Partnership.
