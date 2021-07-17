# OCDS para Asociaciones Público-Privadas

El Estándar de Datos de Contrataciones Abiertas para el perfil de Asociaciones Público Privadas provee un esquema extendido del esquema de Datos de Contrataciones Abiertas, ofreciendo un modelo de datos estructurados para presentar información en proyectos de  Asociaciones Público Privadas.

Esta basado en el [Marco del Banco Mundial para la Divulgación de Proyectos de Asociación Público Privada](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T1) y fue desarrollado entre Mayo 2016 y Mayo 2017 a través de una asociación entre el equipo del [Banco Mundial Open Contracting](https://blogs.worldbank.org/category/tags/open-contracting), [PPP team](http://www.worldbank.org/en/topic/publicprivatepartnerships), [Open Contracting Partnership](http://open-contracting.org), y  [Open Data Services Co-operative](http://www.opendataservices.coop).

La documentación completa del perfil esta disponible en:  [http://standard.open-contracting.org/profiles/ppp/](http://standard.open-contracting.org/profiles/ppp/)

La consolidación de la extensión OCDS para APPs puede ser declarada en OCDS package metadata\](http://standard.open-contracting.org/latest/es/schema/release_package/) usando:

```json
{
  "extensions": [
    "http://standard.open-contracting.org/profiles/ppp/extension/1__0__0__beta/extension.json"
  ],
  "releases": []
}
```

## Sobre extensiones APP

OCDS para APPS esta construida a partir de [un numero de diferentes extensiones modulares de OCDS](http://standard.open-contracting.org/profiles/ppp/latest/es/extensions/),, de los cuales la mayoría puede ser usadas independientemente del perfil.

Este repositorio contiene una extensión adicional que forma parte del perfil de OCDS para APPs. Esta extensión presenta una serie de campos y bloques de construcción que son específicos de la divulgación de APP según el Marco del Banco Mundial.

### Extensiones específicas de APP

#### Indicadores de Evaluación

El marco de divulgación de APP requiere que se divulguen varios indicadores diferentes relacionados con la evaluación de los gobiernos de un proyecto de APP.

La sección `awards.evaluationIndicators` incluye propiedades para expresar el **valor** y **detalles de texto libre** de apoyo para cada indicador:

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

La sección `contracts.financeSummary` incluye propiedades para expresar el **value** y soporta **detalles de texto libre** para cada indicador:

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

### 2021-04-19

- Replace `documentType.csv` with `+documentType.csv`, which adds new codes instead of replacing the codelist.

### 2021-02-15

- Restaura los reoles 'procuringEntity', 'tenderer' y 'funder'. Elimina el rol 'bidder'.

### 2021-01-14

- Elimina la lista de códigos `+releaseTag.csv`.

### 2021-01-11

- Elimina la lista de códigos `initiationType.csv`.
- Restaura los campos `buyer` y `awards.suppliers`.

### 2020-11-16

- Restaura campos deprecados.
- Restaura los campos `Budget.project` y `Budget.projectID`.

### 2020-06-04

- Revisar de las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-05-01

- Elimina los códigos 'qualifiedBidder' y 'disqualifiedBidder'  de `+partyRole.csv` (se movieron a la extensión [calificación](https://extensions.open-contracting.org/es/extensions/qualification/master/)).

### 2019-03-20

- Establece `"uniqueItems": true` en campos matriz.
