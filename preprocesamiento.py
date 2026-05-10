import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("datos.csv")

print("=== CONJUNTO DE DATOS ORIGINAL ===")
print(df)

df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))
df = pd.get_dummies(df)

escalador = MinMaxScaler()
df[df.columns] = escalador.fit_transform(df[df.columns])

print("=== CONJUNTO DE DATOS PROCESADO ===")
print(df)

df.to_csv("datos_procesados.csv", index=False)