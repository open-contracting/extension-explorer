# Paginación

Agregar un objeto de enlaces a los paquetes para dar soporte a la paginación.

## Enlaces

El objeto `links` de nivel superior en paquetes de entrega y paquetes de registro tiene tres campos:

- `next`: una URL al siguiente paquete secuencial
- `prev`: una URL al paquete secuencial anterior

Para construir las URLs `next` y / o` prev`, se recomienda utilizar parámetros de cadena de consulta como:

- `since=TIMESTAMP`, para devolver a una página de resultados que se modifican después de `since` timestamp, en orden cronológico
- `offset=NUMBER`, para devolver a una página de resultados que se colocan después del número `offset` en orden secuencial (por ejemplo, si los resultados se recuperan de un [SQL database](https://www.postgresql.org/docs/current/queries-limit.html))

No se aconseja utilizar `page = NUMBER` con los resultados ordenados en cronología inversa, porque:

- Una página determinada no devolverá los mismos resultados a lo largo del tiempo. `page = 1` devolverá resultados diferentes hoy, la semana que viene y el año que viene.
- Los usuarios pueden recibir resultados duplicados mientras paginan. Por ejemplo, si se publica una nueva versión en la página 1 mientras los usuarios están paginando, el resultado en la parte inferior de cada página se moverá a la parte superior de la página siguiente.
- Es más difícil para los usuarios sincronizar con la API. Con `since` o `offset`, los usuarios pueden recuperar nuevos resultados enviando timestamp o el last request. Con `page`, los usuarios deben determinar qué resultados son nuevos o antiguos.

Referencia: [HTML link types](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types), [18F API Standards](https://github.com/18F/api-standards#pagination), [Government of Canada Standards on APIs](https://www.canada.ca/en/government/system/digital-government/modern-emerging-technologies/government-canada-standards-apis.html), [Government of Ontario API Guidelines](https://github.com/ongov/API-Guidelines/blob/develop/API-Guidelines.md#implement-pagination-and-data-segmentation), [OpenActive Realtime Paged Data Exchange](https://www.openactive.io/realtime-paged-data-exchange/#overall-approach).

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
