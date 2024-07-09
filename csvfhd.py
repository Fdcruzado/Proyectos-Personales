import wfdb
import os
import pandas as pd

def convert_to_csv(record_name, output_directory):
    # Leer el registro usando wfdb
    record = wfdb.rdrecord(record_name)
    
    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(record.p_signal, columns=record.sig_name)
    
    # Generar el nombre del archivo CSV
    csv_filename = os.path.join(output_directory, f"{os.path.basename(record_name)}.csv")
    
    # Guardar el DataFrame como CSV
    df.to_csv(csv_filename, index=False)
    
    print(f"Archivo {csv_filename} guardado con éxito.")

def process_directory(input_directory, output_directory):
    # Crear el directorio de salida si no existe
    os.makedirs(output_directory, exist_ok=True)
    
    # Procesar todos los archivos .hea en el directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith(".hea"):
            record_name = os.path.splitext(filename)[0]
            record_path = os.path.join(input_directory, record_name)
            convert_to_csv(record_path, output_directory)

# Directorio de entrada y salida
input_directory = r'C:\Users\danie\Downloads\3001202 0037'
output_directory = r'C:\Users\danie\Downloads\3001202 0037\csv_output'

# Procesar los archivos en el directorio
process_directory(input_directory, output_directory)
