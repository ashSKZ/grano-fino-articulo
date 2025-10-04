import pandas as pd

# === 1. Cargar archivo ===
file_path = "labels.csv"  # ajusta la ruta si está en otra carpeta
df_raw = pd.read_csv(file_path, header=None)

# === 2. Obtener la primera fila ===
first_row = df_raw.iloc[0]

# === 3. Identificar posiciones de cada número ===
num_positions = {}

for col_idx, value in enumerate(first_row, start=1):  # columnas numeradas desde 1
    try:
        num = int(value)
        if num not in num_positions:
            num_positions[num] = []
        num_positions[num].append(col_idx)
    except:
        continue

# === 4. Crear resumen con inicio, fin y repeticiones ===
summary = []
for num, cols in sorted(num_positions.items()):
    summary.append({
        "Número": num,
        "Columna inicio": min(cols),
        "Columna fin": max(cols),
        "Veces repetido": len(cols)
    })

summary_df = pd.DataFrame(summary)

# Guardar tabla principal
summary_df.to_csv("posiciones_numeros.csv", index=False)

# === 5. Revisar solapamientos (rango dentro de otro) ===
overlaps = []

for i, row_i in summary_df.iterrows():
    for j, row_j in summary_df.iterrows():
        if i == j:  # evitar compararse con sí mismo
            continue
        if row_i["Columna inicio"] >= row_j["Columna inicio"] and row_i["Columna fin"] <= row_j["Columna fin"]:
            overlaps.append({
                "Número dentro": row_i["Número"],
                "Número que lo contiene": row_j["Número"]
            })

overlaps_df = pd.DataFrame(overlaps)

# Guardar resultados de solapamientos
overlaps_df.to_csv("solapamientos.csv", index=False)

# === 6. Mostrar resultados ===
print("Resumen de posiciones guardado en 'posiciones_numeros.csv'")
print("Solapamientos guardados en 'solapamientos.csv'")
print("\nEjemplo de resumen:")
print(summary_df.head())
print("\nEjemplo de solapamientos:")
print(overlaps_df.head())
