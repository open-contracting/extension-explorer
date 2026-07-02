# Fuentes

En muchos casos, la publicación OCDS combina información de múltiples sistemas de información o bases de datos. Por ejemplo:

- Un publicador puede obtener información de varios sistemas para crear un release único.
- Distintos sistemas pueden ser responsables de distintos procesos de contrataciones; por ejemplo, compras tradicionales, marcos de referencia y asociaciones público-privadas se pueden gestionar en diferentes sistemas.
- Distintos sistemas pueden ser responsables de distintos procesos de contrataciones, publicado en distintos releases: por ejemplo, datos de presupuesto del sistema de Ministerio de Finanzas y solicitudes de datos de del sistema de la Agencia de Compras Públicas.
- Distintos sistemas pueden cubrir diferentes períodos, por ejemplo, datos más antiguos que no se han migrado al nuevo sistema.

La procedencia de los datos es relevante para muchos casos de uso, incluyendo la verificación de datos.

Para satisfacer los casos de uso, esta extensión incluye una lista de `sources` en el esquema de release, en el cual el publicador puede hacer una lista de los sistemas de información de los cuales surgen los datos del release.

## Ejemplo

```json
{
	"sources": [
		{
			"id": "sample-source",
			"name": "Sample Source",
			"url": "http://example.com"
		},
		{
			"id": "honducompras",
			"name": "HonduCompras 1.0",
			"url": "http://h1.honducompras.gob.hn/"
		}
	]
}
```

## Notas de uso

Existen casos donde la fuente de los datos de un release vienen de diferentes sistemas de información del mismo publicador.

Existen casos en donde se ligan los datos de bases de datos de contratos con las bases de datos de ofertas y procesos tradicionales.

## Registro de cambios

Esta extensión se discutió originalmente en  <https://github.com/open-contracting/standard/issues/800>.
