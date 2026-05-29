# Análisis de Comentarios de Texto

## Integrantes
- Claudia Eugenia Gonzalez

## Escenario elegido
Escenario C – Procesamiento Básico de Comentarios de Texto

## Descripción del dataset
Archivo CSV con 12 comentarios de usuarios generados para el análisis.
Contiene dos columnas: id y comentario.

## Metodología
1. Carga del dataset desde /datos/comentarios.csv
2. Limpieza y tokenización del texto
3. Cálculo de frecuencia de palabras (Top 10)
4. Clasificación de comentarios por palabras clave positivas/negativas
5. Generación de gráficos y exportación de resultados

## Resultados obtenidos
- 6 comentarios Positivos
- 5 comentarios Negativos  
- 1 comentario Neutro

## Instrucciones para ejecutar
1. Abrir el notebook en Google Colab
2. Ejecutar las celdas en orden desde la celda 1
3. Los resultados se guardan automáticamente en /resultados

## Estructura del repositorio
analisis-comentarios/
├── datos/
│   └── comentarios.csv
├── scripts/
│   └── analisis_comentarios.py
├── resultados/
│   ├── comentarios_clasificados.csv
│   └── grafico_resultados.png
├── README.md
└── .gitignore
