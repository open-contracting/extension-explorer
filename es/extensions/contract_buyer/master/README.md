# Información del comprador a nivel de contrato

## Antecedentes

El esquema OCDS central da un espacio para un solo `buyer`&#160;que puede describirse en cada proceso de contrataciones. El comprador se define como una organización cuyos fondos se usan directamente para la compra de bienes, servicios o trabajos descritos en el contrato.

Sin embargo, algunos procesos de contrataciones, como los acuerdos macro, son resultado de múltiples contratos, con cada contrato firmado por un comprador diferente

Esta extensión provee una forma de dar información sobre `buyer` por contrato.

## Campos de extensión

Esta extensión agrega la propiedad `buyer` a la sección `contracts` de OCDS.

`contracts.buyer` es un `OrganizationReference` que consta de los siguiente campos:

- `name` - El nombre de la parte a la que se hace referencia. Esto debe ser igual que el nombre en la entrada de la sección `parties`.
- `id` - El id de la parte a la que se hace referencia. Debe ser igual que el id en la entrada de la sección  `parties`.

## Dependencias

Esta extensión solo es válida de la Versión 1.1 del OCDS, ya que hace uso del enfoque de referencia de organización actualizado.

## Ejemplo

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "buyer": {
        "name": "Example Department of Transport",
        "id": "GB-GOV-00000000"
      }
    },
    {
      "id": "2",
      "awardID": "2",
      "buyer": {
        "name": "Example Department of Education",
        "id": "GB-GOV-12345678"
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
