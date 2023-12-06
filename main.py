import pandas as pd

# Ruta del archivo Excel
ruta_archivo_excel = r'C:\Users\kevin\OneDrive\Desktop\ETL\hurto_automotores.xlsx'

# Cargar el archivo Excel en un DataFrame
dataframe = pd.read_excel(ruta_archivo_excel)

# Imprimir todos los datos del DataFrame
print(dataframe.head)

