# Paginación

Agregar un objeto de enlaces a los paquetes para dar soporte a la paginación.

## Enlaces

El objeto `links` de nivel superior en paquetes de entrega y paquetes de registro tiene tres campos:

- `next`: una URL al siguiente paquete secuencial
- `prev`: una URL al paquete secuencial anterior

For guidance on constructing the `next` and/or `prev` URLs, refer to the [OCDS documentation](https://standard.open-contracting.org/latest/en/guidance/build/hosting/#pagination).

## Ejemplo

Un publicador tiene una gran cantidad de entregas. En lugar de reunirlas en un paquete de entrega, las segmenta en varios paquetes de entrega, a través de una API con paginación. El campo `links.next` proporciona el enlace a la página siguiente.

```json
{
  "uri": "https://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-05-contract.json",
  "license": "http://opendatacommons.org/licenses/pddl/1.0/",
  "publicationPolicy": "https://github.com/open-contracting/sample-data/",
  "version": "1.1",
  "releases": [
    {
      "ocid": "ocds-213czf-000-00001",
      "id": "ocds-213czf-000-00001-05-contract",
      "date": "2010-05-10T10:30:00Z",
      "language": "en",
      "tag": [
        "contract"
      ],
      "initiationType": "tender"
    }
  ],
  "links": {
    "next": "https://raw.githubusercontent.com/open-contracting/api-specification/master/multiple-file-api-next/releases-2015.json"
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-11-05

- Remover `links.all`.
- Eliminar `packageMetadata`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-15

- Descontinuar `links.all`.
- Descontinuar `packageMetadata`.
