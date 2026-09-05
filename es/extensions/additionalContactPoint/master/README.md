# Puntos de Contacto Adicionales y Lenguajes del Punto de Contacto

Hay algunos casos en los que es importante enumerar varios puntos de contacto para una organización, especialmente en los casos en los que cada punto de contacto se ocupa únicamente de consultas en determinados idiomas.

Esta extensión añade una matriz de `additionalContactPoints` al objeto `organization` e introduce una matriz de `availableLanguage` sobre los lenguajes disponibles a `ContactPoint`.

Cuando se utiliza esta extensión, los editores deben incluir un **punto de contacto principal** para el objeto `contactPoint`, ya que muchas aplicaciones no conocerán la lista `additionalContactPoints`. Sin embargo, si no se puede determinar un punto de contacto principal, todos los puntos de contacto pueden ser revelados en la lista `additionalContactPoints`.

## Ejemplo

```json
{
  "parties": [
    {
      "id": "GB-LAC-E09000003",
      "roles": [
        "procuringEntity"
      ],
      "identifier": {
        "scheme": "GB-LAC",
        "id": "E09000003",
        "legalName": "AnyTown Council"
      },
      "name": "AnyTown Council",
      "address": {
        "streetAddress": "4, North London Business Park, Oakleigh Rd S",
        "locality": "London",
        "region": "London",
        "postalCode": "N11 1NP",
        "countryName": "United Kingdom"
      },
      "contactPoint": {
        "name": "Procurement Team",
        "email": "procurement-team@example.com",
        "telephone": "01234 345 346",
        "availableLanguage": [
          "en"
        ]
      },
      "additionalContactPoints": [
        {
          "name": "Procurement Team (International Enquiries)",
          "email": "procurement-team-international@example.com",
          "telephone": "01234 345 346 Extension 123",
          "availableLanguage": [
            "es",
            "fr",
            "de"
          ],
          "address": {
            "streetAddress": "5, North London Business Park, Oakleigh Rd S",
            "locality": "London",
            "region": "London",
            "postalCode": "N11 1NP",
            "countryName": "United Kingdom"
          }
        }
      ]
    }
  ]
}
```

## Notas de modelado

`availableLanguage` es singular, aunque es una lista, para alinearse con [Schema.org](https://schema.org/availableLanguage).

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2023-12-19

- Add `ContactPoint.address` field.

### 2020-06-04

- Revisar las palabras normativas y no-normativas

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establece `"uniqueItems": true` en campos matriz.

### 2018-12-21

- Colocar  `wholeListMerge` en `Organization.additionalContactPoints`.
- Aclarar el uso de códigos de idioma en `ContactPoint.availableLanguage`
