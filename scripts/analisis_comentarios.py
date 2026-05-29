
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re

# ── Carga de datos ──────────────────────────────────────────────
# Usamos ruta relativa para garantizar reproducibilidad en Colab
df = pd.read_csv("datos/comentarios.csv")
print(f"Dataset cargado: {len(df)} comentarios")

# ── Frecuencia de palabras ──────────────────────────────────────
# Unimos todos los comentarios en un solo texto y limpiamos
texto_completo = " ".join(df["comentario"].str.lower())
palabras = re.findall(r'\b[a-záéíóúñ]{4,}\b', texto_completo)

# Contamos frecuencia de cada palabra
frecuencia = Counter(palabras)
palabras_comunes = frecuencia.most_common(10)
print("\nPalabras más frecuentes:")
for palabra, cantidad in palabras_comunes:
    print(f"  {palabra}: {cantidad}")

# ── Clasificación positivo/negativo ────────────────────────────
# Definimos palabras clave para clasificar comentarios
palabras_positivas = ["bueno", "excelente", "encantó", "recomiendo",
                      "satisfecho", "maravilloso", "fantástico", "perfecto"]
palabras_negativas = ["malo", "terrible", "horrible", "pésimo",
                      "decepcionante", "no", "peor"]

def clasificar(comentario):
    # Clasificamos según presencia de palabras clave
    texto = comentario.lower()
    puntos_pos = sum(1 for p in palabras_positivas if p in texto)
    puntos_neg = sum(1 for p in palabras_negativas if p in texto)
    if puntos_pos > puntos_neg:
        return "Positivo"
    elif puntos_neg > puntos_pos:
        return "Negativo"
    else:
        return "Neutro"

df["clasificacion"] = df["comentario"].apply(clasificar)

# ── Informe de resultados ───────────────────────────────────────
resumen = df["clasificacion"].value_counts()
print("\nResumen de clasificación:")
print(resumen)

# Guardamos el informe en /resultados
df.to_csv("resultados/comentarios_clasificados.csv", index=False)
print("\n✓ Resultados guardados en /resultados/comentarios_clasificados.csv")

# ── Gráfico ────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: clasificación de comentarios
resumen.plot(kind="bar", ax=ax1, color=["green", "red", "gray"])
ax1.set_title("Clasificación de Comentarios")
ax1.set_xlabel("Sentimiento")
ax1.set_ylabel("Cantidad")
ax1.tick_params(axis="x", rotation=0)

# Gráfico 2: palabras más frecuentes
palabras_graf = [p[0] for p in palabras_comunes[:7]]
cantidades_graf = [p[1] for p in palabras_comunes[:7]]
ax2.barh(palabras_graf, cantidades_graf, color="steelblue")
ax2.set_title("Palabras Más Frecuentes")
ax2.set_xlabel("Frecuencia")

plt.tight_layout()
plt.savefig("resultados/grafico_resultados.png", dpi=150, bbox_inches="tight")
plt.show()
print("✓ Gráfico guardado en /resultados/grafico_resultados.png")
