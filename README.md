# Proceso ETL en Python

Este repositorio contiene un ejercicio práctico de **Extract, Transform, Load (ETL)** implementado en Python.  
Se simulan fuentes de datos en formato CSV, se transforman las fechas al estándar `AAAA-MM-DD` y se genera un archivo consolidado listo para análisis.

---

## 📂 Estructura del proyecto

```
proceso_etl/
│── data/
│   ├── source_clientes.csv      # Datos simulados de clientes
│   ├── source_pedidos.csv       # Datos simulados de pedidos
│   └── output_etl.csv           # Resultado final del proceso ETL
│
│── etl_proceso.py               # Script principal ETL
│── documentacion_etl.md         # Documentación del proceso
│── reflexion_etl.md             # Reflexión sobre el ejercicio
│── README.md                    # Este archivo
```

---

## ⚙️ Instalación

1. Clona este repositorio o descarga el ZIP:  
   ```bash
   git clone https://github.com/tu-usuario/proceso_etl.git
   cd proceso_etl
   ```

2. (Opcional) Crea un entorno virtual:  
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. Instala la dependencia principal:  
   ```bash
   pip install pandas
   ```

---

## ▶️ Ejecución

Ejecuta el script principal desde la carpeta raíz del proyecto:

```bash
python etl_proceso.py
```

Si todo funciona correctamente, verás en consola:

```
Proceso ETL completado. Archivo generado: data/output_etl.csv
```

---

## ✅ Resultado esperado

El archivo `data/output_etl.csv` contendrá la información de clientes y pedidos unificada, con las fechas transformadas al formato correcto:

```csv
id_pedido,id_cliente,producto,monto,fecha_pedido,nombre,email,fecha_registro
1001,1,Laptop,1500,2023-07-12,Ana Torres,ana.torres@email.com,2023-05-23
1002,2,Tablet,800,2022-03-05,Carlos Ruiz,carlos.ruiz@email.com,2022-06-14
1003,3,Teclado,50,2021-12-21,María López,maria.lopez@email.com,2021-11-02
```

---

## 📝 Créditos

Ejercicio práctico de **ETL en Python** desarrollado como parte del módulo *Transformación de Datos* en el Bootcamp de Data Analytics.
