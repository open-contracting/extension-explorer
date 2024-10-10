# Documentos de Hito

En OCDS 1.1, el soporte básico para documentos adjuntos a hitos individuales se eliminó del bloque de hitos para simplificar el estándar.

Esta extensión reintroduce el bloque `documents` en ` milestones`, proporcionando campos para detallar los documentos relacionados con cada hito individual.

## Guía

Los publicadores deben considerar que muchas aplicaciones consumidoras sólo buscarán en la sección `tender/documents`, `award/documents`, `contracts/documents` y `contracts/implementation/documents` para acceder y mostrar la documentación relevante a los usuarios.

Los títulos de los documentos, los tipos de documentos y las descripciones se pueden utilizar para indicar a los lectores humanos la naturaleza particular de los documentos y los hitos con los que se relacionan.

Sin embargo, en los casos en que es importante rastrear los documentos hito por hito, esta extensión puede ser introducida.

Dependiendo de la naturaleza de los documentos, los publicadores deberán considerar duplicar la información en el bloque de documentos de las secciones principales también.

## Ejemplo

Durante la implementación de un contrato, el comprador establece hitos que el proveedor debe de cumplir. Cada uno de estos hitos tiene un documento asociado que ofrece más detalles sobre el hito alcanzado: por ejemplo, un reporte de consultoría:

```json
{
  "contracts": [
    {
      "id": "CO-40002-18-166811",
      "awardID": "354469-jorge-augusto-zarate-leiva-1",
      "implementation": {
        "milestones": [
          {
            "id": "fcrMXKIb3/o=",
            "title": "Informe de Consultoria",
            "type": "reporting",
            "dueDate": "2020-02-13T00:00:00-04:00",
            "dateMet": "2020-02-14T00:00:00-04:00",
            "status": "met",
            "documents": [
              {
                "id": "QQ1cjJZ82Rk=",
                "url": "https://www.contrataciones.gov.py/documentos/download/contrato_detalle_entregable/vki7v5RKGrA%253D",
                "datePublished": "2020-02-17T13:38:25-04:00",
                "language": "es",
                "title": "informe_n__13_1581957505348.pdf",
                "format": "application/pdf"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.5

- Revisar las palabras normativas y no-normativas

### v1.1.4

- Añadir extension.json para el Extension Explorer

### v1.1.3

- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
