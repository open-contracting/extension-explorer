# Cargos

La extensión de cargos se utiliza para registrar detalles de los **cargos totales** estimados o aplicados a los usuarios o al gobierno durante la operación de un contrato de Asociación Público Privada.

Esto puede utilizarse para proporcionar un desglose del **apoyo gubernamental** a un proyecto, sobre una base de período por período.

## Resumen

La extensión Cargos introduce una propiedad `charges` tanto para`Contract` como para `Contract/Implementation`.

Contiene una matriz de objetos `Charge` con propiedades para:

- `title` - título descriptivo del cargo;
- `paidBy` - ya sea 'gobierno' o 'usuario';
- `period`: la fecha de inicio y de finalización del período cubierto por el cargo;
- `estimatedValue` - el valor total previsto de este cargo durante el período;
- `actualValue` - el valor real (actualizado después de finalizado el período) del cargo durante el período;
- `notes` - información adicional sobre el cargo;
