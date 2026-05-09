import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar dataset
df = pd.read_csv("datos.csv")

# Mostrar dataset original
print("=== DATASET ORIGINAL ===")
print(df)

# Eliminar duplicados
df = df.drop_duplicates()

# Rellenar valores nulos
df = df.fillna(df.mean(numeric_only=True))

# Convertir variables categóricas
df = pd.get_dummies(df)

# Normalización
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

# Mostrar dataset procesado
print("=== DATASET PROCESADO ===")
print(df)

# Guardar dataset procesado
df.to_csv("datos_procesados.csv", index=False)

print("Preprocesamiento completado correctamente.")