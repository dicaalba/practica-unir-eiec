# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista


## Explicación

El script Python lee una lista de palabras de un archivo, las ordena y opcionalmente elimina duplicados.

Funciones principales:
sort_list(items, ascending=True):

Toma una lista de elementos y los ordena.
Si el parámetro ascending es True, la lista se ordena de forma ascendente; si es False, de forma descendente.
Verifica que el parámetro items sea una lista, lanzando un error si no lo es.
remove_duplicates_from_list(items):

Toma una lista de elementos y devuelve una nueva lista sin duplicados utilizando un conjunto (set).
