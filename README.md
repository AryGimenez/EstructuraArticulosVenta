# EstructuraArticulosVenta
Este proyecto automatiza la creación de directorios basados en una hoja de cálculo de Google Sheets. Utiliza Python y gspread para leer datos de la hoja y generar directorios nombrados con el código y nombre del producto. Facilita la organización y gestión de información de manera eficiente.


## Características

- **Lectura de datos desde Google Sheets:** Utiliza la biblioteca `gspread` para acceder y leer los datos de una hoja de cálculo de Google.
- **Creación automatizada de directorios:** Genera directorios en la ubicación especificada usando los valores de las columnas especificadas en la hoja de cálculo.
- **Facilidad de configuración:** Permite especificar la ubicación base donde se crearán los directorios.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `gspread`
  - `oauth2client`

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/tu_proyecto.git
   cd tu_proyecto
