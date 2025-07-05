# Asignación de riesgos

El [marco para la divulgación de APP](http://pubdocs.worldbank.org/en/773541448296707678/Disclosure-in-PPPs-Framework.pdf) exige información individual sobre la asignación de riesgos.

La extensión de asignación de riesgos se utiliza para proporcionar datos estructurados sobre las asignaciones de riesgo definidas en un contrato de asociación público-privada.

## Resumen

Las asignaciones de riesgos se pueden representar utilizando una lista de [bloques de riesgo](../../../schema/reference/#organization) en el campo `riskAllocation` de la sección `contract` de una entrega de OCDS.

La categoría de riesgo se puede representar utilizando el campo `risk/category` utilizando valores de la [lista de códigos de categoría de riesgo](../schema/codelists/#risk-category) basados ​​en el APMG PPP Certification Program.

La parte que conserva cada riesgo debe representarse utilizando el campo `risk/allocation`, utilizando valores de la [lista de códigos de asignación de riesgos](../schema/codelists/#risk-allocation).

La descripción del riesgo debe proporcionarse como texto libre utilizando el campo `risk/description` y la mitigación del riesgo debe proporcionarse como texto libre utilizando el campo `risk/mitigation`.

Se puede proporcionar información de texto libre adicional sobre el riesgo utilizando el campo `risk/notes`.
