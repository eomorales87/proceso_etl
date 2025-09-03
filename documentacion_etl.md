# Documentación del Proceso ETL

## Extracción
Se usaron dos fuentes de datos en formato CSV (`source_clientes.csv` y `source_pedidos.csv`), simuladas con datos ficticios.

## Transformación
- Se aplicó un cambio de formato de fecha de `dd-mm-aa` a `AAAA-MM-DD`.
- Se realizó una unión entre las tablas de clientes y pedidos para consolidar la información.

## Carga
El resultado fue exportado a un archivo CSV único (`output_etl.csv`), manteniendo la integridad de los datos.
