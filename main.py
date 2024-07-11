import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Configuración de las credenciales y acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

# Accede a la hoja de cálculo
spreadsheet = client.open("nombre_de_tu_hoja_de_calculo")
sheet = spreadsheet.sheet1

# Lee los datos desde la fila 3 en adelante
data = sheet.get_all_values()[2:]  # Saltar las dos primeras filas

# Función para crear la estructura de directorios
def create_directory_structure(base_path, data):
    for row in data:
        mCodProducto = row[0]  # Columna A
        mNomProducto = row[1]  # Columna B
        if mCodProducto and mNomProducto:
            dir_name = f"{mCodProducto} - {mNomProducto}"
            dir_path = os.path.join(base_path, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directorio creado: {dir_path}")

# Define el directorio base donde se crearán los nuevos directorios
base_path = 'path/to/your/base_directory'

# Crea la estructura de directorios
create_directory_structure(base_path, data)


