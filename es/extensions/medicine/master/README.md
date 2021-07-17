# Medicine extension

Adds fields to the item object relevant to the procurement of medicines.

## Guidance

This extension is intended to be used in the medicines-related items in the tender, award, or contract stages, to add more specific details that a medicine item may have. To use it, set the properties that are known, including the active ingredients, dosage form, the medicine container, and the administration route.

If a contracting process is in the award or contract stage, it’s possible to know more information about the medicine, such as the brand, the manufacturer, the country of origin, the expiration date, if they must maintain a cold chain and all the other commercial, financial and logistical conditions. Use the [generic item attributes](https://extensions.open-contracting.org/en/extensions/itemAttributes/master/) extension for all the cases where the medicine item has other attributes not included in this extension.

If a medicine item has more than one active ingredient, add each one to the `activeIngredients` array.

If a medicine item is packaged in a multi-drug container, use `items.quantity` for the quantity in the container and `items.unit` for the unit.

## Examples

### One Active Ingredient

This is an [example](https://api.mercadopublico.cl/APISOCDS/ocds/tender/734-82-LP14) of an item of a drug procurement process in Chile, and its modeling in the extension.

Description | Minimum dispensing unit
--|--
Acetilcisteina | ACETILCISTEINA-N 100 MG/ML SOLUCION PARA NEBULIZAR FRASCO 15-30 ML ENVASE INDIVIDUAL RESISTENTE CON SELLO QUE ASEGURE INVIOLABILIDAD DEL CONTENIDO

The strength is expressed as "100 MG/ML", but the UN/CEFACT codes for unit codes only includes "mg/L", so 100mg/ml is converted to 100000mg/L.

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
        "dosageForm": "solution",
        "administrationRoute": "nasal",
        "container": {
          "name": "jar",
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
            "name": "acetilcisteina",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "ml/L"
              },
              "value": 100000
            }
          }
        ]
      }
    ]
  }
}
```

### More than one Active Ingredient

This is an [example](https://www.contrataciones.gov.py/licitaciones/convocatoria/391507-adquisicion-medicamentos-hospital-clinicas-1.html#pliego) of an item of a drug procurement process in Paraguay and how it would be represented with the extension.

Description | Technical specifications | Unit of measurement | Presentation |  Delivery presentation
--|--|--|--|--
Clorhidrato de Bupivacaina Hiperbarica Inyectable     | clorhidrato de bupivacaina 25 mg. + dextrosa 82,5 mg. - solución inyectable | UNIDAD | VIAL | caja conteniendo 25 ampollas como minimo de 5 ml.

```json
{
  "tender": {
    "items": [
      {
        "id": "1",
        "dosageForm": "injection",
        "administrationRoute": "transdermal",
        "container": {
          "name": "blister",
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
            "name": "clorhidrato de bupivacaina",
            "strength": {
              "unit": {
                "scheme": "UNCEFACT",
                "id": "mg"
              },
              "value": 250
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
        "quantity": 25,
        "unit": {
          "id": "UNI",
          "name": "Unidad"
        }
      }
    ]
  }
}
```

## Related Standards

The fields, definitions and codelists used in this extension are based on the following standards that are commonly used in the data on public medicine purchases. Each standard is used for the classification, designation, or listing of drugs in different countries.
The `administrationRoute` codelist is based on the [FDA Route of Administration list](https://www.fda.gov/drugs/data-standards-manual-monographs/route-administration) (see `items.administrationRoute`).
The `dosageForm` codelist is based on the [European Medicines Agency (EMA) dosage form list](https://www.ema.europa.eu/documents/other/list-pharmaceutical-dosage-forms_en.xls).
The `container` codelist is based on the Health Level Seven (HL7) Fast Healthcare Interoperability Resources (FHIR) [Medication knowledge package type codes](http://terminology.hl7.org/CodeSystem/medicationknowledge-package-type).

Standard | Maintainer |  Purpose
--|--|--
[Anatomical, Therapeutic, Chemical classification system (ATC)](https://www.whocc.no/atc_ddd_index/)   | [World Health Organization](https://www.who.int/home)         | medicine classification
[Drug](https://schema.org/Drug) (Schema.org type)        | [Schema.org Community Group](https://www.w3.org/community/schemaorg/)         | medicine classification
[International nonproprietary names (INN)](https://www.who.int/teams/health-product-and-policy-standards/inn/)        | [World Health Organization](https://www.who.int/home)         | medicine names
[MSH Products Price Guide](https://www.msh.org/resources/international-medical-products-price-guide)        | [Management Sciences for Health](https://www.msh.org/about-us)         | medicine list
[Listado de Medicamentos Esenciales](https://www.mspbs.gov.py/dependencias/dggies/adjunto/db7bee-ListadodeMedicamentosEsenciales.pdf) | [Ministerio de Salud del Paraguay](https://www.mspbs.gov.py/index.php) | medicine list
[Cuadro Básico y Catálogo de Medicamentos (CBM)](http://www.csg.gob.mx/contenidos/priorizacion/cuadro-basico/med/catalogos.html)| [Consejo de Salubridad General de México](http://www.csg.gob.mx/index.html) | medicine catalogue
[United Nations Standard Products and Services Code (UNSPSC)](https://www.unspsc.org/) | [United Nations](https://www.un.org/en/) |classification of products and services, including medicines
[Catálogo de Productos Farmacéuticos](http://observatorio.digemid.minsa.gob.pe/Precios/ProcesoL/Catalogo/CatalogoProductos.aspx)|[Ministerio de Salud de Perú](https://www.gob.pe/minsa/)| medicine catalogue

## Background

This extension is based on research with 4 data users and 6 data publishers including public entities, journalists, medicine price analysts, and software developers for medicine purchase systems from 9 countries from Latin America, Europe, and Africa.

The extension includes the most used fields in different countries. The field names are standardized according to the [Anatomical, Therapeutic, Chemical classification system (ATC)](https://www.whocc.no/atc_ddd_index/), developed by the World Health Organization, and the Drug definition by [Schema.org](https://schema.org/Drug).

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
