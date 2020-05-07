# ds-linq

## Descripción
Proceso de intercambio de información entre Linq y Creze para la administración de cartera

### Procesos
- ALTA: Alta de créditos nuevos en el sistema de Linq
- FAC: Envío de cobranza futura a partir de la fecha de carga
- CACRE: Envío de información sobre acreedores

### Funcionalidad
- PAG -> Creación y envío de XML con información de pagos
- OTROS -> Creación y envío de XML con información de pagos correspondientes a impuestos e intereses
- NCR (Notas de Crédito) -> Creación y envío de XML de créditos refinanciados, liquidados
- SALDOS -> Creación y envío de XML con información de saldos

##### IMPORTANTE
Algunos archivos fueron omitidos para compartir con el motivo de mantener la seguridad de la información íntegra. El presente repositorio pretende mostrar únicamente la forma de integración de los diferentes procesos.
