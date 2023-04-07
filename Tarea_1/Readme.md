# CC5213 - Recuperación de Información Multimedia
## Profesor: Juan Manuel Barrios 
## Fecha: 30 de marzo de 2023 

# Tarea 1

Para la tarea 1 debe crear dos programas:

  * `tarea1-indexar.py`
     Recibe dos parámetros por la línea de comandos:
	    1. La carpeta con imágenes R de prueba. Por ejemplo: dataset_a/r
        2. Una carpeta donde guardar descriptores. Por ejemplo: datos_r_a
   
  * `tarea1-buscar.py`
     Recibe tres parámetros por la línea de comandos:
       1. La carpeta con imágenes de consulta Q. Por ejemplo: dataset_a/q
	   2. La carpeta con descriptores de R. Por ejemplo: datos_r_a
	   3. El nombre del archivo a crear con el resultado de la comparación de Q y R. Por ejemplo: resultado_a.txt

El archivo de salida debe tener un formato de 3 columnas separadas por un tabulador. En cada
fila debe tener el nombre de una imagen de Q, el nombre de la imagen de R más cercana y la
distancia entre ambas imágenes.

Por ejemplo, un posible archivo de resultados sería este:

q0001.jpg	r0432.jpg	610.2
q0002.jpg	r0231.jpg	126.1
[......]
q2441.jpg	r0156.jpg	11.5
q2442.jpg	r1849.jpg	119.5


Para probar su tarea debe usar el programa de evaluación:

  `python evaluarTarea1.py`

Este programa llamará su tarea con el dataset "a" y mostrará el resultado obtenido y la nota.

Para probar su tarea con todos los datasets debe ejecutar:

  `python evaluarTarea1.py --full`

Su tarea no puede demorar más de 15 minutos en evaluar sobre un dataset.