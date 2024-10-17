def obtener_precio(fruta, kilos, precios):

    if fruta in precios:
        precio_kilo = precios[fruta]  # Obtener el precio por kilo de la fruta
        return precio_kilo * kilos  # Calcular y devolver el precio total
    return None  # Si la fruta no está, devolver None

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Diccionario que almacena los precios de diferentes frutas por kilo
    precios_frutas = {
        'manzana': 2.5,
        'banana': 1.2,
        'naranja': 1.5,
        'fresa': 3.0,
        'uva': 4.0
    }

    # Solicitar al usuario el nombre de la fruta
    fruta = input("Introduce el nombre de la fruta: ").lower()
    # Solicitar al usuario la cantidad de kilos
    kilos = float(input("Introduce el número de kilos: "))

    # Obtener el precio total utilizando la función obtener_precio
    total = obtener_precio(fruta, kilos, precios_frutas)

    # Verificar si se obtuvo un precio total válido
    if total is not None:
        # Mostrar el precio total si la fruta está en el diccionario
        print(f"El precio total por {kilos} kilos de {fruta} es: ${total:.2f}")
    else:
        # Informar al usuario que la fruta no está en el diccionario
        print("La fruta no está en el diccionario.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
