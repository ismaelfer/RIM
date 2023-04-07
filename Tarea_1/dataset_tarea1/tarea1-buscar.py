# CC5213 - TAREA 1
# 27 de marzo de 2023
# Alumno: [nombre]

import sys
import os.path

def tarea1_buscar(dir_dataset_q, dir_datos_temporales, file_resultados):
    if not os.path.isdir(dir_dataset_q):
        print("ERROR: no existe directorio {}".format(dir_dataset_q))
        sys.exit(1)
    elif not os.path.isdir(dir_datos_temporales):
        print("ERROR: no existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
    elif os.path.exists(file_resultados):
        print("ERROR: ya existe archivo {}".format(file_resultados))
        sys.exit(1)
    # borrar la siguiente linea
    print("ERROR: no implementado!")
    # Implementar la busqueda
    #  1-leer imágenes en dir_dataset_q y calcular descriptores
    #  2-leer descriptores de R de dir_datos_temporales
    #  3-para cada descriptor q localizar el mas cercano en R
    #  4-escribir en file_resultados


# inicio de la tarea
if len(sys.argv) < 4:
    print("Uso: {} [dir_dataset_q] [dir_datos_temporales] [resultados.txt]".format(sys.argv[0]))
    sys.exit(1)

dir_dataset_q = sys.argv[1]
dir_datos_temporales = sys.argv[2]
file_resultados = sys.argv[3]

tarea1_buscar(dir_dataset_q, dir_datos_temporales, file_resultados)
