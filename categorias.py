import os
import shutil
import pandas as pd

# ------------------------------
# CONFIGURACIÓN
# ------------------------------
# Carpeta donde están las imágenes numeradas
dataset_path = "jpg"  

# Archivo CSV con la tabla de categorías
tabla_csv = "resultado_numeros.csv"  

# Carpeta de salida donde se guardarán las imágenes clasificadas
output_dir = "dataset_clasificado"

# ------------------------------
# PROCESAMIENTO
# ------------------------------

# Cargar la tabla
df = pd.read_csv(tabla_csv)

# Crear carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Recorrer cada fila de la tabla
for _, row in df.iterrows():
    categoria = row["Número"]
    start = int(row["Primera columna"])
    end = int(row["Última columna"])
    
    # Crear carpeta para la categoría
    cat_folder = os.path.join(output_dir, str(categoria))
    os.makedirs(cat_folder, exist_ok=True)

    print(f"Moviendo imágenes {start}-{end} en carpeta {categoria}...")

    # Recorrer el rango de imágenes
    for i in range(start, end + 1):
        # Nombre con formato image_00001.jpg
        img_name = f"image_{i:05d}.jpg"
        img_src = os.path.join(dataset_path, img_name)
        img_dst = os.path.join(cat_folder, img_name)
        
        # Mover solo si la imagen existe
        if os.path.exists(img_src):
            shutil.move(img_src, img_dst)

print("✅ Clasificación terminada. Las imágenes se movieron a:", output_dir)
