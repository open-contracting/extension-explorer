# Extensión de Métricas

La extensión de métricas proporciona un bloque de construcción común para reportar información estructurada de rendimiento de los contratos.

Las métricas están estructuradas como un [cubo de datos OLAP](https://en.wikipedia.org/wiki/OLAP_cube) con cada instancia de `Metric` representando una sola **observation**, categorizada por un número de **dimensions**.

```json
{
  "metrics":[
    {
      "id":"annualDemand",
      "title":"Annual Demand",
      "description":"The annual demand",
      "observations":[
        {
          "period":{
            "startDate":"2015-01-01T00:00:00Z",
            "endDate":"2015-12-31T23:59:59Z"
          },
          "quantity":"10000",
          "dimensions":{
            "vehicleType":"Car"
          }
        },
        {
          "period":{
            "startDate":"2015-01-01T00:00:00Z",
            "endDate":"2015-12-31T23:59:59Z"
          },
          "quantity":"1000",
          "dimensions":{
            "vehicleType":"Trucks"
          },
          "note":"Simple note"
        }
      ]
    },
    {

    }
  ]
}
```

## Uso con requerimientos

Las métricas se pueden utilizar junto con la **extensión de requisitos** que agregará una propiedad 'relatedRequirementID' a las métricas.

Con la extensión de requisitos, las ofertas, adjudicaciones y contratos pueden incluir un `requirementResponse` que indica los valores contra cada métrica que un proveedor desea cumplir.

Esto puede permitir un cierto grado de comparación entre el rendimiento previsto en las fases de licitación, adjudicación, contrato y ejecución.

## Por hacer

- \[ \] Comprobar la sintaxis del esquema oneOf para value **o**quantity
- \[ \] Agregar relatedRequirementID a la extensión de requisitos
- \[ \] Validar actualizaciones de esquema
