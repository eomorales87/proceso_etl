import pandas as pd
from datetime import datetime

# ========================
# 1. EXTRACCIÓN
# ========================
clientes = pd.read_csv("data/source_clientes.csv")
pedidos = pd.read_csv("data/source_pedidos.csv")

# ========================
# 2. TRANSFORMACIÓN
# ========================

# Requisito: cambio de formato de fecha dd-mm-aa → AAAA-MM-DD
def transformar_fecha(fecha):
    return datetime.strptime(fecha, "%d-%m-%y").strftime("%Y-%m-%d")

clientes["fecha_registro"] = clientes["fecha_registro"].apply(transformar_fecha)
pedidos["fecha_pedido"] = pedidos["fecha_pedido"].apply(transformar_fecha)

# Unir clientes con pedidos
df_final = pedidos.merge(clientes, on="id_cliente", how="left")

# ========================
# 3. CARGA
# ========================
df_final.to_csv("data/output_etl.csv", index=False)

print("Proceso ETL completado. Archivo generado: data/output_etl.csv")
