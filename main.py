import argparse

def sort_list(lista, ascendente=True):
    """Ordena la lista en orden ascendente o descendente."""
    return sorted(lista, reverse=not ascendente)

if _name_ == "_main_":
    # Configuramos el analizador de argumentos
    parser = argparse.ArgumentParser(description="Ordena una lista de palabras.")
    
    # Argumento opcional para definir el orden ascendente o descendente
    parser.add_argument("--descendente", action="store_true", 
                        help="Ordena la lista en orden descendente")
    
    # Parseamos los argumentos de la línea de comandos
    args = parser.parse_args()

    # Ejemplo de lista de palabras (puedes adaptarlo a tu caso)
    palabras = ["casa", "auto", "bicicleta", "avión"]

    # Llamamos a la función con el parámetro correspondiente
    resultado = sort_list(palabras, ascendente=not args.descendente)

    # Mostramos el resultado por pantalla
    print("Lista ordenada:", resultado)