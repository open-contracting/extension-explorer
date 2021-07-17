# Proyecto

Esta extensión agrega un objeto `project` al objeto `planning`.

En OCDS, la información del proyecto está anidada bajo el objeto [`planning.budget`](https://standard.open-contracting.org/latest/es/schema/reference/#budget). Sin embargo, en algunos casos, los sistemas de gestión presupuestaria y de gestión de proyecto están separados, y podría ser importante especificar por separado:

- La cantidad reservada en el presupuesto para un proceso de contratación específico
- El proyecto al que se refiere el contrato y el valor total de dicho proyecto
- Clasificaciones de sector
- Clasificaciones adicionales
- Ubicaciones del proyecto, con opciones de diccionario geográfico o ubicaciones puntuales

Esto es particularmente importante en casos de alianzas público-privadas y grandes proyectos de infraestructura, donde los usuarios pueden querer hacer un seguimiento de todos los procesos de contratación relacionados con el proyecto a gran escala y comprender los contratos individuales en el contexto de su proceso de contratación y el proyecto en general. valores.

## Examples

### Infrastructure project

```json
{
  "planning": {
    "project": {
      "id": "oc4ids-gx3fo2-000002",
      "title": "Construcción de red de drenaje sanitario en diversas calles de la colonia Ruperto Martínez",
      "description": "Construcción de red de drenaje sanitario consistente en excavación de 756 metros cúbicos para alojar la red de drenaje sanitario, suministro y colocación de 712 metros de tubería PVC tipo serie 20 pared solida, construcción de 15 pozos de visita y 30 descargas domiciliarias sencillas en la colonia Ruperto Martinez, en el municipio de Higueras, N.L.",
      "totalValue": {
        "amount": 4010130.1,
        "currency": "MXN"
      },
      "locations": [
        {
          "description": "Col. Ruperto Martínez, Higueras, N.L.",
          "geometry": {
            "type": "Point",
            "coordinates": [
              25.953400063796533,
              -100.01606973176307
            ]
          }
        }
      ]
    }
  }
}
```

### Public-Private Partnership project

```json
{
  "planning": {
    "project": {
      "title": "Example PPP",
      "description": "The Example PPP project will guarantee the installation of a wholesale shared network that allows the provision of telecommunications services by current and future operators.",
      "id": "example_ppp",
      "uri": "http://communications.gov.example/projects/example_ppp",
      "totalValue": {
        "amount": 600000000,
        "currency": "USD"
      },
      "sector": {
        "scheme": "COFOG",
        "description": "Road transportation",
        "id": "04.5.1"
      },
      "locations": [
        {
          "description": "Local Authority Area: Halton Borough Council",
          "gazetteer": {
            "scheme": "GEONAMES",
            "identifiers": [
              "2647601"
            ]
          }
        }
      ]
    }
  }
}
```

## Registro de cambios

### 2021-04-15

- Add infrastructure project example

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-16

- Eliminar guía relacionada al objeto `planning.budget`. Ver [#701](https://github.com/open-contracting/standard/issues/701).

### 2018-05-03

- Agregar guía adicional sobre el uso de los campos de OCDS en el contexto de esta extensión

### 2017-12-29

- Eliminar la repetición de campos OCDS en esta extensión

### 2017-07-08

- Agregar soporte multilingüe para el campo `Project.title`
- Eliminar el soporte multilingüe para los campos inexistentes `Project.source` y `Project.project`
- Restaurar los campos `Budget.project` y `Budget.projectID`
- Eliminar la propiedad obsoleta `mergeStrategy`.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
