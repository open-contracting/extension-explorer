# Documentos de Hito

En OCDS 1.1, el soporte básico para documentos adjuntos a hitos individuales se eliminó del bloque de hitos para simplificar el estándar.

Esta extensión reintroduce el bloque `documents` en ` milestones`, proporcionando campos para detallar los documentos relacionados con cada hito individual.

## Guía

Los publicadores deben considerar que muchas aplicaciones consumidoras sólo buscarán en la sección `tender/documents`, `award/documents`, `contracts/documents` y `contracts/implementation/documents` para acceder y mostrar la documentación relevante a los usuarios.

Los títulos de los documentos, los tipos de documentos y las descripciones se pueden utilizar para indicar a los lectores humanos la naturaleza particular de los documentos y los hitos con los que se relacionan.

Sin embargo, en los casos en que es importante rastrear los documentos hito por hito, esta extensión puede ser introducida.

Dependiendo de la naturaleza de los documentos, los publicadores deberán considerar duplicar la información en el bloque de documentos de las secciones principales también.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.3

- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
