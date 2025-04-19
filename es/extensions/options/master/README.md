# Opciones

Esta extensión agrega campos para indicar si se utilizan opciones y otra información sobre las mismas.

Un comprador puede tener el derecho, pero no la obligación, de realizar compras adicionales a un proveedor mientras el contrato sea válido.

For example, a contract may concern a thousand uniforms, and the buyer may have the option to request an additional hundred uniforms. This might occur if the buyer doesn't yet know whether a planned increase in staff will take place.

## Contexto legal

El \[Acuerdo Revisado Sobre Contratación Pública\] (https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) incluye: "cada aviso de contratación prevista deberá incluir ... d. una descripción de las opciones".

La Unión Europea es una [parte](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) para el Acuerdo sobre Contratación  Pública GPA, y como tal su [Directiva 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Contratos públicos — establecimiento de reglas básicas claras) incluye: "Parte C: Información que se incluirá en los avisos de contrato ... 7. ... Donde corresponda, descripción de las opciones".

## Ejemplo

```json
{
  "tender": {
    "hasOptions": true,
    "options": {
      "description": "The buyer has the option to buy an additional hundred uniforms.",
      "period": {
        "durationInDays": 180
      }
    }
  }
}
```

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2024-05-02

- Add fields:
  - `Award.hasOptions`
  - `Award.options`
  - `Contract.hasOptions`
  - `Contract.options`
- Clarify the description of `Tender.hasOptions` and `Lot.hasOptions`.

### 2020-10-06

- Add `Options.period` field.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

Esta extensión se discutió originalmente como parte del \[OCDS para el perfil de la UE\] (https://github.com/open-contracting-extensions/european-union/issues), en \[pull requests\] (https://github.com/open-contracting-extensions/ocds_options_extension/pulls?q=is%3Apr+is%3Aclosed) y en <https://github.com/open-contracting/standard/issues/691>.
