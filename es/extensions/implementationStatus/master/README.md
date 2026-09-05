# Estado de la Implementación

## Descripción:

En México, cuando se habla de trabajos y servicios relacionados, es necesario publicar un set de variables específicas sobre su implementación. Una de las variables es el status de la implementación del trabajo o servicios, esto incluye una lista de código con los siguientes valores:

- planeación
- proyectos en marcha
- proyectos concluidos

## Propuesta:

Añadir un campo nuevo llamado "“implementationStatus” en el objeto  “Implementation”.

### Esquema

- Implementación {object}
  - Estatus (string, null) (codelist)

## Textos definidos:

**Code** | **Title** | **Description**
--|--|--
status | Implementation status | The current status of the contract implementation based on the [implementationStatus](https://github.com/INAImexico/ocds_implementationStatus_extension/blob/master/codelists/implementationStatus.csv)  codelist.
planning | Planning | The contract has been signed, but the provision or construction of the goods, services or works has not started.
ongoing | Ongoing | The provision or construction of the goods, services or works is in progress.
concluded | Concluded | The provision or construction of the goods, services or works has officially ended.

## Issues

Reportar issues para esta extensión en [standard repository](https://github.com/open-contracting/standard/issues/624) de Open Contracting Partnership.
