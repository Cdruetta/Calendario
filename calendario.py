import calendar
import locale
from datetime import datetime

# Configurar el locale a español
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, 'C')  # En Windows podría no funcionar 'es_ES.UTF-8'

def obtener_mes(yy, mm):
    hoy = datetime.today()
    es_mes_actual = (yy == hoy.year and mm == hoy.month)
    
    mes = calendar.monthcalendar(yy, mm)
    encabezado = "lu ma mi ju vi sa do"
    
    # Obtener el nombre del mes en español
    nombre_mes = calendar.month_name[mm].capitalize()
    titulo = f"\033[31m{nombre_mes}\033[0m {yy}".center(30)  # Ajuste para mantener alineación
    
    salida = [titulo, encabezado]
    
    for semana in mes:
        linea = []
        for dia in semana:
            if dia == 0:
                linea.append("  ")  # Espacio para días vacíos
            elif es_mes_actual and dia == hoy.day:
                # Resaltar el día actual en rojo
                linea.append(f"\033[33m[{dia}]\033[0m")  # Código ANSI para rojo
            else:
                linea.append(f"{dia:2}")
        salida.append(" ".join(linea))
    
    return salida
# Año
yy = 2025
meses_por_fila = 4  # Número de meses por fila

# Imprimir los meses en filas
for i in range(1, 13, meses_por_fila):
    # Obtener los meses de la fila actual
    meses = [obtener_mes(yy, mm) for mm in range(i, min(i + meses_por_fila, 13))]
    
    # Encontrar el máximo de líneas en los meses de esta fila
    max_lineas = max(len(mes) for mes in meses)
    
    # Rellenar los meses más cortos con líneas vacías
    for mes in meses:
        while len(mes) < max_lineas:
            mes.append(" " * len(mes[0]))  # Línea vacía con el mismo ancho
    
    # Imprimir las líneas alineadas
    for linea in zip(*meses):
        # Asegurarse de que cada mes tenga el mismo ancho en cada línea
        print("   ".join(f"{mes.ljust(21)}" for mes in linea))  # Separador entre meses
    print("-" * 84)  # Separador entre filas de meses
