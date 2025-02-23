"""
=====================
Project    : WS CAMEF
File       : a_config.py
Description: General configuration settings for the web scraper.
             Includes WebDriver path, target URL, and execution parameters.
Date       : 2025-02-07
Version    : 1.0
Author     : Alex Evanan

Revision History:
    - [2025-02-07] v1.0: Initial version.

Usage:
    Run this script from the terminal or interactive environment:
        $ python 02_src/a_config.py
=====================
"""

# =====================
# Importación de librerías
# =====================

import os

# =====================
# 1: Configuración del WebDriver y Navegación
# =====================

# Directorios
PATH_BASE = os.getcwd()
PATH_DATA_RAW = os.path.join(PATH_BASE, "01_data/01_raw")
PATH_DATA_PRO = os.path.join(PATH_BASE, "01_data/02_processed")
PATH_DRIVER = os.path.join(PATH_BASE, "03_config/chromedriver/chromedriver.exe")
# Url
URL = "https://apps5.mineco.gob.pe/transparencia/mensual/"


# =====================
# 2: Parámetros de Scraping
# =====================

# Años de consulta
YEARS = list(range(2015, 2026))  # no incluye el límite superior
# Nombre del archivo de salida
ARCHIVO_SALIDA = "EJECUCION_GASTO_MUNICI.xlsx"
# Nombre del archivo de salida parcial (en caso de error)
ARCHIVO_SALIDA_PARCIAL = "EJECUCION_GASTO_MUNICI_parcial.xlsx"
# Encabezados base
ENCABEZADOS_BASE = ["Año", "Departamento", "Provincia"]

# =====================
# 3: Parámetros de Procesamiento
# =====================

ARCHIVO_PROCESADO = "EJECUCION_GASTO_MUNICI_procesado.xlsx"
