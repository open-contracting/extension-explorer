# Título y descripción del proceso

En algunos casos, es importante proporcionar un título y una descripción generales para un proceso de contratación, distintos de los campos individuales de título y descripción contenidos en los bloques `tender`, ` awards` y `contracts`.

La extensión añade campos  `title` y `description`  al esquema de release.

A menudo se utilizarán para proporcionar un resumen legible de la información que se proporciona en otra parte del documento OCDS como datos estructurados.

Los publicadores que utilicen estos campos deben ser conscientes de que no todas las aplicaciones mostrarán su contenido y, por lo tanto, la información clave para comprender la naturaleza del proceso de contratación generalmente también se debe proporcionar utilizando los campos centrales del OCDS.

## Ejemplo

```json
{
  "title": "Next-Generation Telecommunications PPP",
  "description": "The Next-Generation Telecommunications PPP project will guarantee the installation of a wholesale shared network that allows the provision of telecommunications services by current and future operators. The project will increase the telecommunication services coverage, promote competitive prices and enhance the quality of services according to international standards."
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### v1.1.5

- Revisar las palabras normativas y no-normativas

### v1.1.4

- Añadir el ejemplo al readme
- Añadir extension.json para el Extension Explorer

### v1.1.3

- Usa la licencia Apache 2.0
- Agregar pruebas y ordenar el código
