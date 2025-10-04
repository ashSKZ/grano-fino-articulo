import pandas as pd

# Ruta al archivo
file_path = "labels.csv"

# Leer el archivo sin encabezados (porque la primera fila son datos)
df = pd.read_csv(file_path, header=None)

# Extraer la primera fila (única)
values = df.iloc[0].tolist()

# Crear lista de resultados
resultados = []

# Encontrar valores únicos
unique_numbers = set(values)

for num in unique_numbers:
    indices = [i for i, x in enumerate(values) if x == num]
    resultados.append({
        "Número": num,
        "Primera columna": indices[0],
        "Última columna": indices[-1],
        "Repeticiones": len(indices)
    })

# Convertir a DataFrame ordenado por número
res_df = pd.DataFrame(resultados).sort_values(by="Número").reset_index(drop=True)

# Mostrar tabla
print(res_df)

# Si quieres guardar la tabla en CSV
res_df.to_csv("resultado_numeros.csv", index=False)
