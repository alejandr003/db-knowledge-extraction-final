# Guia Final del Proyecto - Presentacion Ejecutiva

**Curso:** Database Knowledge Extraction  
**Proyecto:** Enterprise Multi-Modal Data Visualization and Storytelling  
**Fecha limite:** 24 de noviembre de 2026, 11:59 PM  
**Presentacion:** 24 de noviembre de 2026, 10 minutos, 5 integrantes (~2 min c/u)  
**Repositorio:** https://github.com/alejandr003/db-knowledge-extraction-final

> **Objetivo de esta guia:** darle a Josmar (Rol 4) y al equipo una base clara y completa para armar la presentacion final: que se hizo, por que, con que herramientas, que resultados salieron y que debe decir cada integrante.

---

## 1. Resumen ejecutivo del proyecto

### Que pide la asignacion
Construir un portafolio de visualizacion de datos empresarial multimodal que combine:

1. **Pipeline de datos reproducible** (limpieza y preparacion).
2. **Dashboard BI interactivo** (Power BI).
3. **Visualizaciones programaticas/estadisticas** (Python/Jupyter).
4. **Narrativa ejecutiva de storytelling** con el marco:  
   **Setup -> Conflict/Insight -> Resolution**.

### Que problema resuelve
Una empresa tiene datos de ventas, pero los datos crudos por si solos no permiten tomar decisiones rapido. Este proyecto transforma un CSV empresarial en informacion util para responder:

- **Donde se gana dinero?**
- **Donde se pierde dinero?**
- **Que esta causando la fuga de utilidad?**
- **Que acciones recomendar para mejorar el rendimiento?**

### Resultado final
El equipo entrego un flujo completo: CSV crudo -> limpieza -> CSV procesado -> dashboard interactivo + notebook estadistico + hallazgos ejecutivos listos para presentacion.

---

## 2. Dataset usado (CSV real del proyecto)

Se utilizo el **Superstore Sales Dataset** (Kaggle), un dataset empresarial con mezcla de campos temporales, continuos, categoricos y geoespaciales.

| Item | Valor |
|---|---|
| Dataset | Superstore Sales Dataset |
| Fuente | Kaggle: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final |
| CSV raw en repo | `data/raw/superstore_raw.csv` |
| CSV procesado en repo | `data/processed/clean_dataset.csv` |
| Diccionario | `data/DATA_DICTIONARY.md` |
| Filas / columnas originales | 9,994 filas x 21 columnas |
| Columnas procesadas | 27 (incluye 6 campos derivados) |
| Rango temporal | 2014-01-03 a 2017-12-30 |
| Alcance | Estados Unidos |
| Moneda | USD |
| Granularidad | Una fila por linea de pedido (producto dentro de una orden) |

### Campos por tipo (cumple el requisito)
- **Temporal:** `Order Date`, `Ship Date`
- **Continuos:** `Sales`, `Profit`, `Discount`, `Quantity`
- **Categoricos:** `Segment`, `Category`, `Sub-Category`, `Ship Mode`
- **Geoespaciales:** `Country`, `Region`, `State`, `City`, `Postal Code`

### Campos derivados creados en limpieza
`Order Year`, `Order Month`, `Order Quarter`, `Shipping Days`, `Profit Margin`, `Is Loss`.

---

## 3. Herramientas y tecnologias usadas

| Area | Herramientas | Para que se uso |
|---|---|---|
| Datos / ETL | Python, Pandas, NumPy | Cargar CSV, auditar calidad, limpiar, tipar, imputar, exportar CSV procesado |
| Visualizacion estadistica | Jupyter Notebook, Matplotlib, Seaborn, Plotly | Distribuciones, boxplots, CI 95%, heatmap de correlacion, scatter interactivo |
| BI Dashboard | Power BI Desktop | Modelo estrella, DAX, KPIs, mapa, tendencia, drill-down, slicers |
| Control de versiones / QA | Git, GitHub, PR reviews | Integracion por roles, revision, trazabilidad, control de calidad |
| Presentacion | Markdown/PDF/PPT/Canva (Rol 4) | Storytelling ejecutivo para presentacion final |

**Archivos clave:**
- `src/clean_data.py` - script de limpieza.
- `data/DATA_DICTIONARY.md` - diccionario y calidad de datos.
- `dashboard/enterprise_dashboard.pbix` - dashboard BI.
- `notebooks/final_visualizations.ipynb` - visualizaciones programaticas.
- `FINAL_PROJECT_PREVIEW.ipynb` - vista previa ejecutiva del proyecto.

---

## 4. Pipeline y arquitectura de solucion

```text
data/raw/superstore_raw.csv
        │
        ▼
src/clean_data.py
(auditoria, limpieza, tipos, imputacion, derivadas)
        │
        ▼
data/processed/clean_dataset.csv
        ├──▶ notebooks/final_visualizations.ipynb  → assets/plots (PNG/SVG/HTML)
        └──▶ dashboard/enterprise_dashboard.pbix   → insights ejecutivos / presentacion
```

### Por que este pipeline importa
- **Reproducibilidad:** cualquiera puede ejecutar el script y obtener el mismo CSV procesado.
- **Calidad:** se documentan nulos, duplicados, reglas y validaciones.
- **Consistencia:** dashboard y notebook consumen la misma fuente procesada.
- **Trazabilidad:** el diccionario y el README explican el origen y transformaciones.

---

## 5. KPIs y resultados clave (validados)

KPIs calculados sobre `data/processed/clean_dataset.csv` / validados en el modelo Power BI:

| KPI | Valor |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin % | 12.47% |
| Total Orders | 5,009 |
| Total Quantity | 37,873 |
| Average Discount | 15.62% |
| Loss-Making Rows | 1,871 |
| Loss Rate % | 18.72% |
| Loss Amount | -$156,131.29 |
| Avg Shipping Days | 3.96 |

**Lectura rapida:** el negocio vende bien, pero casi 1 de cada 5 lineas de pedido pierde dinero (18.72%), lo que reduce la rentabilidad.

---

## 6. Hallazgos principales (Conflict / Insight)

1. **Ventas sesgadas (concentracion):** hay muchas transacciones pequeñas y pocas de alto valor; el promedio de venta es mucho mayor que la mediana.
2. **Rentabilidad desigual por categoria/subcategoria:** no todas las ventas generan utilidad; algunas subcategorias destruyen margen.
3. **Descuentos como principal fuga de utilidad:** los descuentos altos se asocian con perdidas. El analisis muestra un fuerte deterioro de margen cuando el descuento sube, especialmente por encima de 20%.
4. **Riesgo operativo/comercial:** un volumen importante de lineas con perdida indica que la politica comercial (descuentos/precios) necesita control.
5. **Oportunidad:** existen segmentos/regiones con mejor margen que pueden servir como modelo para crecer con rentabilidad.

> Mensaje para la presentacion: **El problema no es solo vender mas, sino vender con margen.**

---

## 7. Recomendaciones (Resolution)

1. **Politica de descuentos basada en rentabilidad**  
   Definir umbrales de descuento por categoria/subcategoria. Revisar/aprobar descuentos altos (>20%) con justificacion comercial.

2. **Intervenir subcategorias con perdida**  
   Priorizar analisis de precio, costo y descuento en subcategorias con margen negativo (ej. Tables, Bookcases, Supplies segun notebook).

3. **Replicar mezcla rentable**  
   Identificar segmentos/regiones con mejor margen (ej. Home Office / East en hallazgos) y replicar estrategia comercial/producto.

4. **Monitoreo continuo en dashboard**  
   Usar el dashboard Power BI para seguimiento semanal/mensual de KPIs, tasa de perdida y efecto de descuentos.

---

## 8. Guia por integrante (que hizo, que mostrar, que decir)

## Rol 1 - Edwing (Data Architect & Wrangler) | 0:00 - 2:00

### Responsabilidad
Preparar los datos: obtener CSV, limpiar, validar calidad, documentar y generar la fuente unica de verdad.

### Que hizo
- Integro `data/raw/superstore_raw.csv`.
- Creo/ajusto `src/clean_data.py` para auditoria y limpieza.
- Genero `data/processed/clean_dataset.csv`.
- Completo `data/DATA_DICTIONARY.md` (tipos, nulos, reglas, calidad, derivadas).

### Que mostrar
- Estructura `data/raw`, `data/processed`, `src/`, `DATA_DICTIONARY.md`.
- Fragmento del pipeline (raw -> clean_data.py -> processed).

### Puntos para decir (guion)
- "Partimos de un CSV empresarial de 9,994 filas y 21 columnas con campos temporales, continuos, categoricos y geoespaciales."
- "Limpiamos y estandarizamos datos, validamos calidad y generamos un CSV procesado con 27 columnas, incluyendo campos derivados para analisis."
- "Este dataset procesado es la fuente unica que usan el dashboard y el notebook, asegurando consistencia."

### Entregables
`data/raw/superstore_raw.csv`, `data/processed/clean_dataset.csv`, `src/clean_data.py`, `data/DATA_DICTIONARY.md`.

---

## Rol 2 - Neyzer (BI Dashboard Lead) | 2:00 - 4:00

### Responsabilidad
Construir un dashboard ejecutivo interactivo en Power BI para explorar KPIs, tendencias y causas.

### Que hizo
- Construyo `dashboard/enterprise_dashboard.pbix`.
- Creo modelo estrella, relaciones, medidas DAX y tema accesible.
- Implemento 2 paginas: **Executive Overview** y **Operational Drill-Down**.
- Documento medidas/modelo en `dashboard/README.md` y exporto screenshots.

### Que mostrar
- Pagina 1: KPIs, tendencia, mapa, ventas por categoria, slicers.
- Pagina 2: drill-down Categoria -> Subcategoria -> Producto; descuento vs utilidad/perdida.

### Puntos para decir (guion)
- "El dashboard convierte el CSV procesado en una vista ejecutiva interactiva con KPIs y filtros por fecha, region y segmento."
- "Podemos ir del resumen ejecutivo al detalle operativo con drill-down para identificar donde se pierde margen."
- "El hallazgo visual clave es que los descuentos altos estan asociados con perdida de utilidad."

### Entregables
`dashboard/enterprise_dashboard.pbix`, `dashboard/README.md`, `dashboard/theme.json`, `dashboard/screenshots/*`.

---

## Rol 3 - Laura (Python Visualization Specialist) | 4:00 - 6:00

### Responsabilidad
Generar visualizaciones programaticas para validar patrones estadisticos y comunicar incertidumbre/relaciones.

### Que hizo
- Desarrollo `notebooks/final_visualizations.ipynb` (ejecutado con comentarios).
- Genero visualizaciones requeridas: hist/KDE, boxplot, CI 95%, heatmap correlacion, scatter interactivo Plotly.
- Exporto assets a `assets/plots/` (PNG/SVG/HTML).

### Que mostrar
- `distribution_kde.png` / `boxplot_profit.png`
- `uncertainty_ci.png`
- `correlation_heatmap.png`
- `interactive_scatter.html` (o captura)

### Puntos para decir (guion)
- "En Python confirmamos la distribucion sesgada de ventas y la variabilidad de utilidad por categoria."
- "La banda de confianza al 95% muestra incertidumbre en la tendencia mensual; no basta con ver solo promedios."
- "La correlacion y el scatter interactivo muestran que mayores descuentos tienden a asociarse con menor margen/utilidad."

### Entregables
`notebooks/final_visualizations.ipynb`, `assets/plots/distribution_kde.png`, `correlation_heatmap.png`, `uncertainty_ci.png`, `interactive_scatter.html` (+ extras SVG/boxplot).

---

## Rol 4 - Josmar (Narrative & Data Storytelling Lead) | 6:00 - 8:00

### Responsabilidad
Convertir los hallazgos tecnicos en una historia ejecutiva clara y persuasiva para toma de decisiones.

### Que debe hacer / enfocar en la presentacion
- Construir la narrativa **Setup -> Conflict/Insight -> Resolution**.
- Seleccionar visuales clave (no saturar diapositivas).
- Traducir hallazgos en 3 recomendaciones accionables.
- Preparar el deck final y enlace publico (Canva/PPT) en `presentation/LINKS.md`.

### Que mostrar
- Diapositiva de contexto (Setup).
- Diapositiva de conflicto/hallazgo (descuentos y perdida de margen).
- Diapositiva de recomendaciones (Resolution) con impacto esperado.

### Puntos para decir (guion)
- "El negocio vende $2.29M, pero la utilidad se ve afectada por una tasa de perdida del 18.72% en lineas de pedido."
- "El conflicto principal es comercial: descuentos altos estan erosionando el margen."
- "Nuestra recomendacion es controlar descuentos, intervenir subcategorias con perdida y escalar segmentos rentables."

### Entregables objetivo
`presentation/Executive_Presentation.pdf` (o PPTX), `presentation/LINKS.md`, `presentation/SPEAKER_NOTES.md`.

---

## Rol 5 - Jesus (QA & Integration Lead) | 8:00 - 10:00

### Responsabilidad
Asegurar integridad del repositorio, calidad visual, reproducibilidad y preparacion de entrega/presentacion.

### Que hizo
- Estructuro el repo base y documentos de soporte (README, requirements, plantillas).
- Realizo QA y revision de PRs de Roles 1-3 antes de merge.
- Verifico ejecucion del notebook (nbconvert + scipy) y apertura del dashboard en Power BI.
- Creo `FINAL_PROJECT_PREVIEW.ipynb` y guia de ejecucion para presentacion.

### Que mostrar
- README/checklist, estructura del repo, evidencia de reproducibilidad.
- Mencion rapida de controles de calidad: 0-baseline, paletas accesibles, rutas relativas, CSV unico procesado.

### Puntos para decir (guion)
- "Validamos que el proyecto no solo se vea bien, sino que sea reproducible y consistente entre notebook, dashboard y datos."
- "El notebook se ejecuto de inicio a fin, el dashboard abre con las dos paginas y el repo mantiene estructura y trazabilidad por roles."
- "Con esto, la recomendacion se sustenta en datos limpios, visualizaciones correctas y un flujo reproducible."

### Entregables
`.gitignore`, `requirements.txt`, `README.md`, QA de PRs, `FINAL_PROJECT_PREVIEW.ipynb`, apoyo en `presentation/LINKS.md` y `SPEAKER_NOTES.md`.

---

## 9. Estructura de diapositivas sugerida para Josmar (10 min)

1. **Portada** - nombre del proyecto, equipo, curso, fecha.
2. **Agenda / objetivo** - que pregunta de negocio resolvemos.
3. **Dataset y pipeline** - CSV raw/procesado, 9,994 filas, tipos de datos, flujo.
4. **Hallazgos estadisticos (Python)** - distribucion, CI 95%, correlacion, descuento vs profit.
5. **Dashboard BI** - KPIs, mapa, tendencia, drill-down.
6. **Insight principal (Conflict)** - descuentos altos erosionan utilidad; 18.72% lineas con perdida.
7. **Recomendaciones (Resolution)** - 3 acciones concretas.
8. **QA y reproducibilidad** - calidad visual, ejecucion, consistencia.
9. **Cierre / Q&A** - mensaje final y siguiente paso.

---

## 10. Checklist final antes de presentar

- [x] CSV raw y procesado en repo (`data/raw`, `data/processed`).
- [x] Script de limpieza funcional (`src/clean_data.py`).
- [x] Dashboard PBIX con 2 paginas (`dashboard/enterprise_dashboard.pbix`).
- [x] Notebook ejecutado y assets exportados (`notebooks/`, `assets/plots/`).
- [x] README actualizado con dataset real y estado del proyecto.
- [x] Verificacion de notebook por ejecucion (nbconvert) y dashboard abierto en Power BI.
- [ ] Deck final y link publico (Rol 4).
- [ ] Ensayo cronometrado 10 min (equipo completo).

---

## 11. Mensaje final recomendado (cierre de 20-30s)

"Transformamos un CSV empresarial de casi 10 mil registros en un flujo reproducible de analisis y visualizacion. Descubrimos que el principal riesgo no es la falta de ventas, sino la erosion de utilidad por descuentos y subcategorias con perdida. Con el dashboard, el notebook y el control de calidad, proponemos decisiones concretas para proteger el margen y crecer con rentabilidad."