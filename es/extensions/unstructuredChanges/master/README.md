# Cambios no estructurados

Agrega una matriz unstructuredChanges al objeto Amendment.

# Guía

En muchos regímenes de contratación, es habitual modificar un anuncio de licitación describiendo los cambios en palabras, en lugar de volver a publicar el anuncio completo. Esto se debe a que el proceso está diseñado para los humanos: es más fácil para un humano leer una descripción de los cambios, que calcular la diferencia entre dos anuncios completos.

En cambio, para una máquina es fácil calcular la diferencia entre dos notificaciones completas, pero es difícil o imposible interpretar una descripción de cambios. Hay muchas formas en las que una descripción de cambios puede salir mal, de las que un humano puede recuperarse, pero que una máquina no puede. Por ejemplo:

- La etiqueta del campo que está sujeto a modificación puede hacer referencia a:
  - una etiqueta que no aparece en el aviso anterior
  - una etiqueta incorrecta o imprecisa en el aviso anterior
- El tipo de datos del nuevo valor puede ser inconsistente con el tipo de datos del campo.

El OCDS está diseñado para ser leído por máquinas. Lo ideal es que el sistema fuente desde el que se exportan los datos de OCDS contenga los valores de cada campo antes y después de un cambio. En ese caso, debería seguir simplemente [el modelo de entregas y registros](https://standard.open-contracting.org/latest/es/schema/reference/#release-handling).

Esta extensión está pensada para ser utilizada sólo en los casos en que un sistema de origen no rastrea los valores de los campos, sino que rastrea una descripción de los cambios, como en la UE (véase *Contexto legal* más abajo). Nota: La falta de estructura impide muchos análisis de datos.

## Contexto legal

Esta extensión se desarrolló principalmente para permitir la asignación de los formularios estándar de la Unión Europea para la contratación pública a OCDS (específicamente el Formulario 14 Corrigendum), pero podría ser útil en contextos no comunitarios.

See [OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/forms/F14/) for guidance on how to use it with TED F14 data.

## Ejemplo

```json
{
  "tender": {
    "amendments": [
      {
        "id": "1",
        "unstructuredChanges": [
          {
            "oldValue": {
              "text": "https://city.example.org/procurement"
            },
            "newValue": {
              "text": "https://procurement.example.org"
            },
            "where": {
              "section": "I.1",
              "label": "Main address"
            }
          },
          {
            "oldValue": {
              "date": "2020-12-15"
            },
            "newValue": {
              "date": "2019-12-15T14:00:00+03:00"
            },
            "where": {
              "section": "I.4",
              "label": "Notice date"
            }
          },
          {
            "oldValue": {
              "classifications": [
                {
                  "scheme": "CPV",
                  "id": "79000000"
                }
              ]
            },
            "newValue": {
              "classifications": [
                {
                  "scheme": "CPV",
                  "id": "79822500"
                }
              ]
            },
            "where": {
              "section": "II.2.2",
              "label": "Main CPV code"
            },
            "relatedLot": "lot-2"
          }
        ]
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-09-16

- Agregar sección Guía

### 2020-07-13

- Relajar el formato de fecha para permitir fecha o fecha y hora

### 2020-06-04

- Revisar las palabras normativas y no normativas.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues/63), en [pull resquests](https://github.com/open-contracting-extensions/ocds_unstructuredChanges_extension/pulls?q=is%3Apr+is%3Aclosed).
