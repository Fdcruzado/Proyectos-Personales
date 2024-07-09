import wfdb
import os

# Directorio que contiene los archivos .hea
input_directory = r'C:\Users\danie\Downloads\3001202 0037'

# Iterar a través de los archivos en el directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".hea"):
        record_name = os.path.join(input_directory, os.path.splitext(filename)[0])
        try:
            record = wfdb.rdheader(record_name)
            print(f"Registro: {filename}")
            print(f"Señales: {record.sig_name}")
            print()
        except Exception as e:
            print(f"No se pudo leer el registro {filename}: {e}")
