# Extensión de Presupuestos y Gastos de Contrataciones Abiertas

La extensión de Presupuestos y Gastos extiende la extensión de [budget breakdown](https://github.com/open-contracting-extensions/ocds_budget_breakdown_extension/blob/master/README.md) y la sección de implementación del contrato para permitir la publicación de asignaciones de presupuesto detalladas y la ejecución de las mismas para un proceso de contrataciones

Un [artículo de discusión que muestra los antecedentes del enfoque puede encontrarse aquí](https://docs.google.com/document/d/1b43JeG5YQ62tGTTbP7jTE4XqUxYzG-r-emgRILZPRn4/edit).

Este repositorio se encuentra activamente en desarrollo, y actualmente contiene un [ejemplo](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension/tree/master/examples#readme) de cómo puede ser usada esta extensión para registrar compromisos financieros anuales de un proceso de contratación y contratos individuales.

## En resumen

Esta extensión introduce tres nuevas funciones que surgen de la extensión  [budget breakdown](https://github.com/open-contracting-extensions/ocds_budget_breakdown_extension/blob/master/README.md):

- `classifications` permiten que se den clasificaciones funcionales, económicas y administrativas para cada detalle del presupuesto;
- `measures` - permite que se usen diferentes medidas de presupuesto (planeadas, cometidas, ejecutadas, etc.) a nivel del proceso de contrataciones para cada set de clasificaciones de presupuesto
- `fiscalBreakdownFieldMapping` - provee una manera de vincular a un [Paquete de Datos Fiscales](https://frictionlessdata.io/specs/fiscal-data-package/), un archivo datapackage.json, que define el significado de cada clasificación y medida, y provee acceso a datos relacionados a nivel presupuestario.

Adicionalmente, introduce el objeto `financialProgress` en  `contracts/implementation`, permitiendo mostrar el detalle de la ejecución financiera de cada contrato, utilizando los mismos atributos `classifications`, `measures` y `fiscalBreakdownFieldMapping` como para `budgetBreakdown`.

## Para comenzar

La mejor manera de utilizar esta extensión es viendo los ejemplos desarrollados.

- El **[ejemplo de coordinación](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension/blob/master/examples/coordination.md)** muestra como expresar los datos en una asignación presupuestaria y ejecución que pudieron haber surgido de diferentes sistemas de datos (ej. sistemas financieros y sistemas de compras).
- El **[ejemplo de integración](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension/blob/master/examples/integration.md)** muestra como las referencias a un Paquete de Datos Fiscales pueden permitir la visualización de datos a los usuarios, y la comparación entre los datos a nivel de proceso de contrataciones y de presupuesto.
- El **[ejemplo de datos planos](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension/blob/master/examples/flat.md)** muestra como usando esta extensión pueden ser analizados los datos estructurados publicados con herramientas de hojas de cálculo.

## Conceptos claves

Esta extensión da las herramientas para crear datos que relacionen **budgets**, **contracting processes** y **spending**

Drawing on definitions from the [Global Initiative for Fiscal Transparency (GIFT)](https://fiscaltransparency.net):

**Un presupuesto** es una declaración a futuro de como una organización propone aumentar sus ingresos, utilizar sus recursos y financiar sus operaciones. El presupuesto del Gobierno Nacional debe cubrir todas las actividades de un estado. Los presupuestos detallados pueden existir también a nivel de agencias y proyectos. En las contrataciones públicas, el fondo para un proceso de contratación puede provenir de una sección particular del Presupuesto Nacional, o de un presupuesto organizacional. Podría también provenir por completo o parcialmente de un fondo externo (Ej. el Banco Internacional de Desarrollo), ya sea directamente o a través de sistemas gubernamentales.

Las líneas de presupuesto se construyen a partir de un set de  **classifications**  (generalmente descritas en términos de clasificaciones funcional, administrativas o económicas) y las  **measures** (como el monto original designado a un conjunto particular de clasificaciones, o los montos modificados o ejecutados).

**Fiscal reports** are records of \[an organization's\] actual (historical) revenues, **spending** and financing. They may report the fiscal activities of the central government, state governments, or local governments, or of all levels of government in a country (referred to as the general government). Reports may cover a whole government in aggregate as an organization, and/or individual government units, e.g. ministries, departments or agencies. They may be on a cash or accruals basis (full or partial). As payments are made during the execution of a contract, these may be allocated against one or more sections of the budget. In some cases, this may allow the creation of fiscal reporting at the level of individual contracts.

El Open Contracting Data Standard se usa para compartir información sobre **procesos de contrataciones**. Un proceso de contrataciones puede pasar por diferentes etapas a través del tiempo, incluyendo planeación, licitación, adjudicación, firma de contrato e implementación.

## Relacionando presupuesto, contrataciones y gasto

![Relaciones entre Presupuesto, Contrato y Gasto](https://raw.githubusercontent.com/open-contracting-extensions/ocds_budget_and_spend_extension/master/images/budget-contract-spend.png)

La imagen anterior presenta un representación esquemática de como pueden interactuar las bases de datos de presupuesto, contratación y gasto

Debe notar que:

- Esto no representa una secuencia linear de eventos. Los datos pueden estar disponibles en diferentes punto en el tiempo, como cuando el presupuesto se hace en un ciclo anual, pero los contratos se firman a través de los años. En muchos casos, la información de presupuesto en la sección de `planning` de un proceso de contratación OCDS puede actualizarse después de que los contratos se adjudiquen y se estén implementando.
- Los datos de presupuesto y gasto pueden darse en diferentes niveles de detalle, desde una línea de presupuesto única que financia múltiples procesos de contrataciones, hasta la clasificación fiscal de partes únicas contra un contrato en particular. Los publicadores de datos van a variar de acuerdo al nivel de detalle que se puede extraer con confianza de sus sistemas.
- Los datos de ejecución del presupuesto pueden existir en un nivel transaccional, o puede existir en un nivel más agregado. Esta extensión actualmente cubre la ejecución del presupuesto, pero no cubre las clasificaciones detalladas de las transacciones.

La siguiente imagen muestra un mapeo entre las etapas de una transacción y las etapas de un proceso de contratación. Las etapas de una transacción son generalmente comunes en diferentes jurisdicciones y reflejan las descritas en el \[Paquete de Datos Fiscales\] (https://frictionlessdata.io/specs/fiscal-data-package/); sin embargo, es posible que algunas jurisdicciones no registren todas las etapas, algunas pueden utilizar una terminología diferente y algunas pueden tener más etapas.

!\[Mapeo del proceso de transacción y contratación\] (https://raw.githubusercontent.com/open-contracting-extensions/ocds_budget_and_spend_extension/master/images/transaction-contracting_process.png)

Los datos combinados cubiertos por esta extensión generalmente se obtienen de los sistemas de adquisiciones y los Sistemas de Información de Gestión Financiera (SIGF). Entre los ejemplos de cómo se pueden integrar dichos sistemas se incluyen:

- Antes de iniciar una licitación, el sistema de adquisiciones verifica que los fondos estén disponibles para el proceso de contratación a través del SIGF y crea una reserva en el SIGF.
- Cuando se firma un contrato, el sistema de adquisiciones crea un compromiso en el SIGF por el valor del contrato.
- Cuando se completa un hito o entregable de un contrato, el sistema de adquisiciones crea una verificación o devengado en el SIGF.

## Estándares de datos unidos: conexiones con el paquete de datos fiscales

The [Fiscal Data Package](https://frictionlessdata.io/specs/fiscal-data-package/), developed by Open Knowledge with the support of [GIFT](https://fiscaltransparency.net), provides *"a lightweight and user-oriented format for publishing and consuming fiscal data"*. Unlike OCDS, which requires data to be converted to a set JSON structure before publication, a Fiscal Data Package consists of:

- Una definición de paquete de datos (datapackage.json) el cual describe el 'modelo lógico' para aplicar a los archivos de datos existentes. Esto define las columnas, su relación con los conceptos fiscales y cómo deben transformarse mediante el consumo de aplicaciones para crear datos normalizados.
- Los archivos de datos, que dan el 'modelo físico' para la base de datos de presupuesto o de gastos, y puede ser exportado de los sistemas existentes.

Se ha hecho bastante investigación y pruebas con usuarios para desarrollar el Paquete de Datos Fiscales, estableciendo que, en vez de buscar un acuerdo en un set global de conceptos fiscales, es importante, considerando la diversidad de sistemas de compras y presupuesto alrededor del mundo, permitir a los usuarios publicar sus datos utilizando sus conceptos fiscales existentes, y luego complementar estos con datos adicionales que pueden apoyar el análisis y la comparación entre bases de datos.

Para evitar la duplicación de esfuerzos por parte de los editores y consumidores de datos, esta extensión difiere del modelo del Paquete de Datos Fiscales con respecto a la definición de conceptos fiscales y sigue el enfoque del FDP de permitir el uso de nombres de columnas de datos existentes. Si bien el FDP no hace una distinción directa entre "clasificaciones" y "medidas", considerando que ambas son instancias de "conceptos fiscales", en esta extensión sí trazamos una distinción para permitir que las medidas se validen como numéricas, mientras que las clasificaciones pueden pueden ser cadenas o números.

## Antecedentes

Una exploración completa del enfoque que se toma en esta extensión se puede encontrar en el [background discussion paper](https://docs.google.com/document/d/1b43JeG5YQ62tGTTbP7jTE4XqUxYzG-r-emgRILZPRn4/edit).

### Historias de usuarios y requisitos

Esta extensión fue diseñada en base a un conjunto de historias de usuario.

- U1: Como periodista quiero ver cuál es la fuente de presupuesto de un proceso de contratación particular para poder entender si el presupuesto viene de recursos domésticos, préstamos u otras fuentes de ingreso internacionales
- U2: Como periodista, quiero encontrar todos los contratos financiados a través de una fuente de presupuesto en particular para analizar en qué medida se gasta el presupuesto a través de la contratación u otros medios.
- U3: Como organización de la sociedad civil enfocada en infraestructura quiero encontrar todos los procesos de contratación relacionados con un determinado programa o proyecto de infraestructura para poder realizar una revisión del cumplimiento de los requisitos de transparencia del proyecto de infraestructura.
- U4: Como periodista, quiero hacer un seguimiento de los contratos (sospechosos) para identificar posibles conexiones entre los destinatarios y los funcionarios y políticos que controlan los procesos de presupuestación y adjudicación.

Identificar y confirmar asignaciones presupuestarias:

- U5: Como un proveedor potencial quiero ver cuando se confirma la disponibilidad de presupuesto para un proceso de contrataciones especifico para poder planear un inventario de potenciales oportunidades de licitación.
- U6: Como organización de monitoreo de la sociedad civil, quiero identificar proyectos sin un presupuesto confirmado para poder analizar la brecha de financiamiento de las adquisiciones planificadas.
- U7: Como un oficial de tesorería quiero compartir información sobre el estatus de las asignaciones de presupuesto y el gasto para cualquier contrato para poder demostrar al público que el presupuesto se esta gastando de acuerdo a los planes aprobados
- U8: Como un monitor de compras quiero ver que parte del proyecto de infraestructura viene del presupuesto de capital vs el presupuesto de ingresos para poder monitorear si se gasto de más o de menos de lo planeado
- U9: Como organización de la sociedad civil, quiero identificar hasta qué punto se han asignado gastos en determinadas líneas presupuestarias y el estado de ese gasto a lo largo del tiempo para poder informar sobre las áreas de gasto excesivo o insuficiente.

Siguiendo el proceso de pagos:

- U10: Como académico, quiero identificar la brecha entre la fecha de la factura y la fecha de pago para poder analizar cómo los precios se ven afectados por los plazos de pago.
- U11: Como auditor quiero los detalles completos sobre el proceso de cobro y de pago para poder identificar banderas rojas potenciales e investigar los procesos particulares

Estas historias de usuario se utilizaron para identificar un conjunto de requisitos que la extensión debería cumplir. La siguiente lista describe hasta qué punto la extensión actual cumple con los requisitos que se identificaron.

- R1: Identificar inequívocamente cada línea del presupuesto.
  - **¿Requisito cumplido?**: Sí. El Desglose de Presupuesto se amplía con un objeto flexible `classifications` que puede incluir cualquier número de campos de clasificación, reflejando los términos y nombres de columnas utilizados en los conjuntos de datos presupuestarios.
- R2: Identificar inequívocamente los proyectos que aportan financiación a un proceso de contratación.
  - **¿Requisito cumplido?**: Parcialmente. Actualmente no se han introducido cambios para cumplir este caso de uso. El objeto presupuesto básico ya incluye un campo `projectID`.
- R3: Proveer los montos de las diferentes fases del presupuesto incluyendo las asignaciones presupuestarias confirmadas.
  - **¿Requisito cumplido?**: Sí. El Desglose de Presupuesto se amplía con un objeto flexible de `measures` que puede incluir cualquier número de campos de medida, reflejando los términos y nombres de columnas utilizados en los conjuntos de datos de presupuesto y gasto existentes.
- R4: Clasificar transacciones contra líneas presupuestarias
  - **¿Requisito cumplido?**: No. La información desglosada del progreso financiero puede clasificarse en las líneas presupuestarias en la sección de implementación del contrato `financialProgress.breakdown`, pero la extensión no modifica actualmente el bloque de `transactions` para permitir la clasificación a nivel de transacciones individuales.
- R5: Proporcionar información sobre el proceso de transacción, desde la factura hasta el pago.
  - **¿Requisito cumplido?**: Parcialmente. Las `measures` en `financialProgress.breakdown` para cada contrato se pueden utilizar para describir diferentes momentos del procesamiento del pago. Sin embargo, esto solo proporciona un historial completo de la sincronización de los procesos de pago cuando se usa con un historial de versiones detallado de las entregas. En esta extensión no se ha incluido un enfoque alternativo de agregar detalles de `transactions` para representar diferentes momentos, como solicitudes de pago y aprobaciones de pago, pero puede desarrollarse por separado en el futuro.
- R6: Permitir que las asignaciones de montos individuales del presupuesto a contraer dentro de OCDS se verifiquen con las asignaciones generales de la línea presupuestaria en un conjunto de datos presupuestarios
  - **¿Requisito cumplido?**: Sí. Mediante el uso de un enlace al Paquete de Datos Fiscales, es posible comparar la información financiera a nivel de contrato en OCDS con información clasificada de manera similar en un FDP.
- R7: Proporcionar interfaces con la información necesaria para mostrar información presupuestaria a los usuarios.
  - **¿Requisito cumplido?**: Sí. Cuando se usan en conjunto con un Paquete de Dato Fiscal, las aplicaciones pueden buscar etiquetas y meta datos para cada `classifications` y `measures` de manera a mostrar claramente la información a los usuarios.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-06-04

- Revisar las palabras normativas y no-normativas

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2019-03-20

- Establecer `"uniqueItems ": true` en los campos matriz y agregar `"minLength": 1` en los campos de cadena obligatorios.
