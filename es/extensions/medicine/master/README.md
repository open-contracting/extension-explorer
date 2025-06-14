# Extensión de medicamentos

Agrega campos al objeto artículo relevantes para la adquisición de medicamentos.

## Guía

Esta extensión se utiliza para describir medicamentos en las fases de licitación, adjudicación y/o contrato. Con esta extensión, un publicador puede especificar los principios activos del medicamento y su concentración, la forma de dosificación, el envase del medicamento y la vía de administración. De este modo, se facilita la comparación de la adquisición de medicamentos entre jurisdicciones y, por tanto, se apoya los [precios de referencia externos](https://en.wikipedia.org/wiki/External_reference_pricing).

Las formas de dosificación y los tamaños de los envases difieren significativamente entre países, lo que dificulta la comparación. Para facilitar la comparación, la extensión proporciona listas de códigos estandarizadas para la forma de dosificación, el recipiente inmediato y la vía de administración, basadas en [Health Level Seven (HL7)](https://www.hl7.org), un conjunto de normas internacionales para datos sanitarios. Dicho esto, si no ha adoptado y no puede mapear sus valores a los códigos HL7, puede utilizar sus propios códigos. Para que un usuario pueda interpretar sus códigos, debe describir las listas de códigos, y cómo encontrar las definiciones de los mismos, en su [política de publicación](https://standard.open-contracting.org/latest/en/guidance/publish/#finalize-your-publication-policy).

Para los nombres de los principios activos, se recomienda utilizar las Denominaciones Comunes Internacionales o por sus siglas en inglés [International Nonproprietary Names (INN)](https://www.who.int/teams/health-product-and-policy-standards/inn). La Organización Mundial de la Salud (OMS) mantiene una lista acumulativa de todas las INNs, con nombres equivalentes en latín, inglés, francés, español, árabe, chino y ruso. Para facilitar la comparación, se recomienda utilizar el nombre latino en minúsculas.

Si un proceso de contratación está en fase de adjudicación o contrato, es posible conocer más información sobre el medicamento, como la marca, el fabricante, el país de origen, la fecha de caducidad, si deben mantener una cadena de frío y todas las demás condiciones comerciales, financieras y logísticas. Utilice la extensión [atributos genéricos del artículo](https://extensions.open-contracting.org/en/extensions/itemAttributes/master/) para todos los casos en que el artículo del medicamento tenga otros atributos no incluidos en esta extensión.

Si un medicamento tiene más de un principio activo, agregue cada uno de ellos a la lista de `activeIngredients`.

## Ejemplos

### Un principio activo

En este ejemplo, demostramos cómo utilizar esta extensión para describir un [proceso de adquisición de medicamentos](https://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?qs=OE1kSVnLUBVxS5IkXPNLRQ==) de Chile. (Puede ver sus [datos originales OCDS](https://api.mercadopublico.cl/APISOCDS/ocds/tender/734-82-LP14).)

El punto 3 se describe como:

Description | Minimum dispensing unit
-|-
Acetilcisteina | ACETILCISTEINA-N 100 MG/ML SOLUCION PARA NEBULIZAR FRASCO 15-30 ML ENVASE INDIVIDUAL RESISTENTE CON SELLO QUE ASEGURE INVIOLABILIDAD DEL CONTENIDO

La concentración se expresa como "100 MG/ML". La lista de códigos UN/CEFACT [Recomendación 20 - Códigos de Unidades de Medida Utilizados en el Comercio Internacional](https://unece.org/trade/uncefact/cl-recommendations) incluye unidades como mg/l, g/l y kg/l, pero no mg/ml. Así, "100 MG/ML" se expresa como 100 g/l a continuación.

Based on this information, we can add the `dosageForm`, `administrationRoute`, `immediateContainer` and `activeIngredients`.

```json
{
  "tender": {
    "items": [
      {
        "id": "1",
        "description": "Acetilcisteina",
        "classification": {
          "id": "51161701",
          "scheme": "UNSPSC",
          "uri": "https://apis.mercadopublico.cl/OCDS/data/productos/categoria/51161701"
        },
        "dosageForm": "SOL",
        "administrationRoute": "NASINHL",
        "immediateContainer": {
          "name": "vial",
          "capacity": {
            "unit": {
              "scheme": "UNCEFACT",
              "id": "ml"
            },
            "value": "[15,30]"
          }
        },
        "activeIngredients": [
          {
            "name": "acetylcysteinum",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "g/l"
              },
              "value": 100
            }
          }
        ]
      }
    ]
  }
}
```

### Más de un principio activo

En este ejemplo, demostramos cómo utilizar esta extensión para describir un [proceso de adquisición de medicamentos](https://www.contrataciones.gov.py/licitaciones/convocatoria/391507-adquisicion-medicamentos-hospital-clinicas-1.html#pliego) de Paraguay. (Puede ver sus [datos originales del OCDS](https://contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-391507).)

En la pestaña "Suministros requeridos - especificaciones técnicas", artículo 1 del lote 8 ("LOTE N° 8 - ANESTESICOS LOCALES - 2") se describe como:

Description | Technical specifications | Unit of measurement | Presentation |  Delivery presentation
-|-|-|-|-
Clorhidrato de Bupivacaina Hiperbarica Inyectable | clorhidrato de bupivacaina 25 mg. + dextrosa 82,5 mg. - solución inyectable | UNIDAD | AMPOLLA | ampollas como minimo de 5 ml.

Para el nombre del principio activo, el Anexo 2 del [INN Stem Book 2018](https://www.who.int/teams/health-product-and-policy-standards/inn/stembook), describe cómo nombrar las sales ácidas: en este caso, "bupivacainum hydrochloridum".

Based on this information, we can add the `dosageForm`, `administrationRoute`, `immediateContainer` and `activeIngredients`.

```json
{
  "tender": {
    "items": [
      {
        "id": "1",
        "dosageForm": "SOL",
        "administrationRoute": "ISINJ",
        "immediateContainer": {
          "name": "amp",
          "capacity": {
            "unit": {
              "scheme": "UNCEFACT",
              "id": "ml"
            },
            "value": "[5,INF["
          }
        },
        "activeIngredients": [
          {
            "name": "bupivacainum hydrochloridum",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "mg"
              },
              "value": 25
            }
          },
          {
            "name": "dextrosa",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "mg"
              },
              "value": 82.5
            }
          }
        ],
        "quantity": 25
      }
    ]
  }
}
```

## Estándares relacionados

Los campos, las definiciones y las listas de códigos utilizados en esta extensión se basan en las siguientes normas que se utilizan habitualmente en los datos sobre compras de medicamentos públicos.

- Most of the fields are based on the [Drug](https://schema.org/Drug) definition by the [Schema.org Community Group](https://www.w3.org/community/schemaorg/) and the [Medication Resource](https://www.hl7.org/fhir/medication.html) from [Fast Healthcare Interoperability Resources (FHIR)](https://hl7.org/fhir/) standard.
- La lista de códigos `administrationRoute` contiene los conceptos de nivel superior de la lista de códigos HL7 [Vía de Administración](https://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration/), excluyendo cualquier término sinónimo.
- La lista de códigos `dosageForm` contiene los conceptos de nivel superior de la lista de códigos HL7 [Formulario de pedido de medicamentos](https://terminology.hl7.org/CodeSystem/v3-orderableDrugForm/), excluyendo las formas específicas de aerosoles.
- The `immediateContainer` codelist is a copy of the codes and titles from FHIR's [Medication Knowledge Package Type](https://terminology.hl7.org/CodeSystem/medicationknowledge-package-type/) codelist. Given that the terms are undefined in FHIR, the descriptions are copied from corresponding terms from the [EDQM Standard Terms database](https://standardterms.edqm.eu), reproduced with the permission of the European Directorate for the Quality of Medicines & HealthCare, Council of Europe (EDQM). The EDQM Standard Terms database is not a static list and content can change over time; the descriptions were retrieved on July 21, 2021.

## Antecedentes

This extension is based on research with 4 data users and 6 data publishers including public organizations, journalists, medicine price analysts, and software developers for medicine purchase systems from 9 countries in Latin America, Europe, and Africa. The extension includes the most used fields from the different countries.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-12-04

- Rename `container` to `immediateContainer`
- Rename `container.csv` to `immediateContainer.csv`
