# OCDS para Asociaciones Público-Privadas

El Estándar de Datos de Contrataciones Abiertas para el perfil de Asociaciones Público Privadas provee un esquema extendido del esquema de Datos de Contrataciones Abiertas, ofreciendo un modelo de datos estructurados para presentar información en proyectos de  Asociaciones Público Privadas.

Se basa en el [Marco del Banco Mundial para la divulgación en proyectos de Asociaciones Público-Privadas](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/744411637834708119/a-framework-for-disclosure-in-public-private-partnership-projects) y se desarrolló entre mayo de 2016 y mayo de 2017 a través de una asociación entre el [equipo de Contratación Abierta del Banco Mundial](https://blogs.worldbank.org/category/tags/open-contracting), [ Equipo de APP](https://www.worldbank.org/en/topic/publicprivatepartnerships), [Open Contracting Partnership](https://www.open-contracting.org) y [Open Data Services Co-operative](https://opendataservices.coop).

La documentación completa del perfil está disponible en [https://standard.open-contracting.org/profiles/ppp/](https://standard.open-contracting.org/profiles/ppp/)

La extensión OCDS consolidada para APP se puede declarar en los [metadatos del paquete OCDS](https://standard.open-contracting.org/latest/en/schema/release_package/) usando:

```json
{
  "extensions": [
    "https://standard.open-contracting.org/profiles/ppp/extension/1__0__0__beta/extension.json"
  ],
  "releases": []
}
```

## Sobre extensiones APP

OCDS para APP se construye a partir de [varias extensiones modulares diferentes de OCDS](https://standard.open-contracting.org/profiles/ppp/latest/en/extensions/), la mayoría de las cuales se pueden usar independientemente del perfil.

Este repositorio contiene una extensión adicional que forma parte del perfil de OCDS para APPs. Esta extensión presenta una serie de campos y bloques de construcción que son específicos de la divulgación de APP según el Marco del Banco Mundial.

### Extensiones específicas de APP

#### Indicadores de Evaluación

El marco de divulgación de APP requiere que se divulguen varios indicadores diferentes relacionados con la evaluación de los gobiernos de un proyecto de APP.

La sección `awards.evaluationIndicators` incluye campos para expresar el **valor** y los **detalles** de respaldo para cada indicador:

- discountRate
- riskPremium
- netPresentValue

##### Ejemplo

```
"evaluationIndicators": {
  "riskPremium": 0.0092,
  "riskPremiumDetails": "Based on a market risk premium of 6.0% (per government guidelines) and an asset beta of 0.45 (per a sample of listed telecommunication network providers) the project risk allocation gives rise to a risk premium of 0.92%",
  "discountRate": 0.03,
  "discountRateDetails": "Based on the current long term public sector bond rate",
  "netPresentValue": {
    "amount": 118044591901.35034,
    "currency": "USD"
  }
```

#### Resumen Financiero

El marco de divulgación de APP requiere una serie de indicadores diferentes relacionados con el modelo financiero de un proyecto APP. Mientras que algunos de estos pueden ser reportados como métricas en forma continua, algunos son simples valores individuales.

La sección `contracts.financeSummary` incluye campos para expresar el **valor** y los **detalles** para cada indicador:

- debtEquityRatio
- shareCapital
- subsidyRatio
- projectIRR

##### Ejemplo

```
"financeSummary": {
  "debtEquityRatio": 2.05,
  "debtEquityRatioDetails": "Until the target population coverage is reached mega Consortium must comply with a contribution of capital of at least 30% of the total value of the company",
  "shareCapital": {
    "amount": 20000000,
    "currency": "USD"
  }
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-06-07

- Remove unused codes from the `+partyRole.csv` codelist patch:
  - consortiaMember
  - grantor
  - notary
  - otherWitness
  - socialWitness

### 2021-04-19

- Reemplazar `documentType.csv` con `+documentType.csv`, que agrega nuevos códigos en lugar de sustituir la lista de códigos.

### 2021-02-15

- Restore 'procuringEntity', 'tenderer' and 'funder' roles.
- Remove 'bidder' role.

### 2021-01-14

- Remove the `+releaseTag.csv` codelist patch.

### 2021-01-11

- Remove the `initiationType.csv` codelist.
- Restaura los campos `buyer` y `awards.suppliers`.

### 2020-11-16

- Restaura campos deprecados.
- Restaura los campos `Budget.project` y `Budget.projectID`.

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-05-01

- Remove 'qualifiedBidder' and 'disqualifiedBidder' codes from the `+partyRole.csv` codelist patch (moved to [qualification](https://github.com/open-contracting-extensions/ocds_qualification_extension) extension).

### 2019-03-20

- Establece `"uniqueItems": true` en campos matriz.
