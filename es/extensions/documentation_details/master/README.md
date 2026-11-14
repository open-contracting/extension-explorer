# Detalles del documento

Los [objetos document](https://standard.open-contracting.org/latest/es/schema/reference/#document) son usados para describir y enlazar a documentos. Esta extensión agrega campos a los objetos documento para:

- Indique los números de página en los que se puede encontrar información relevante dentro de un documento grande
- Describe cualquier arreglo especial necesario para acceder al documento.
- Nombre del autor del documento (a no ser confundido con su publicador)
- Indicate the languages in which unofficial translations of the document are available

Los casos de usos incluyen:

- Acceder al documento y localizar la información en él
- Comprobar si los autores participan de otras formas en el proceso de contratación, por ejemplo, como licitadores
- Medir la accesibilidad de los documentos

## Ejemplo

```json
{
  "tender": {
    "documents": [
      {
        "id": "1",
        "documentType": "equityTransferCaps",
        "title": "Equity transfer cap terms",
        "description": "No equity transfer is permitted until construction is completed. See document for more details.",
        "url": "http://example.com/ppp_unit/documents/contracts/4g_network_signed_contract.pdf",
        "language": "en",
        "unofficialTranslations": [
          "it"
        ],
        "pageStart": "334",
        "pageEnd": "336",
        "accessDetails": "This document can only be accessed by visiting the PPP unit office by appointment. Please see the PPP unit website for further details.",
        "accessDetailsURL": "http://example.com/ppp_unit/registration/",
        "author": "Contract department, PPP unit"
      }
    ]
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-08-04

- Change unofficialTranslation field to `unofficialTranslations` array of languages.

### 2023-04-05

- Add `accessDetailsURL` and unofficialTranslation fields.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-15

- Mejora en la documentación
- Uso de palabras clave no normativas donde es apropiado

### 2019-01-30

- Eliminar la propiedad obsoleta `mergeStrategy`.
