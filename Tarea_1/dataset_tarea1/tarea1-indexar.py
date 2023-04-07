# CC5213 - TAREA 1
# 27 de marzo de 2023
# Alumno: [nombre]

import sys
import os.path

def tarea1_indexar(dir_dataset_r, dir_datos_temporales):
    if not os.path.isdir(dir_dataset_r):
        print("ERROR: no existe directorio {}".format(dir_dataset_r))
        sys.exit(1)
    elif os.path.exists(dir_datos_temporales):
        print("ERROR: ya existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
    # borrar la siguiente linea
    print("ERROR: no implementado!")
    # Implementar la tarea:
    #  1-leer imágenes en dir_dataset_r
    #  2-calcular descriptores de imágenes
    #  3-crear dir_datos_temporales con: os.makedirs(dir_datos_temporales, exist_ok=True)
    #  4-escribir en dir_datos_temporales los descriptores


# inicio de la tarea
if len(sys.argv) < 3:
    print("Uso: {} [dir_dataset_r] [dir_datos_temporales]".format(sys.argv[0]))
    sys.exit(1)

dir_dataset_r = sys.argv[1]
dir_datos_temporales = sys.argv[2]

# llamar a la funcion
tarea1_indexar(dir_dataset_r, dir_datos_temporales)
