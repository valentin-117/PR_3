
# Informacion Personal
print("")
print("Este es un programa para almacenar información. ")#imprime la funcion del programa 
print("")
print("Frías Villa Angel Valentin 3W. ") #imprime mi nombre
print("")

def main():
    #se crea el diccionario para almacenar variables
    usuario_info = {}

    # soolicitar su información al usuario
    usuario_info['nombre'] = input("Introduce tu nombre: ")
    usuario_info['edad'] = input("Introduce tu edad: ")
    usuario_info['direccion'] = input("Introduce tu dirección: ")
    usuario_info['telefono'] = input("Introduce tu número de teléfono: ")

    # imprime en pantalla los datos del usuario antes requeridos en orden.
    print(f"{usuario_info['nombre']} tiene {usuario_info['edad']} años,")
    print(f"vive en {usuario_info['direccion']} ")
    print(f"y su número de teléfono es {usuario_info['telefono']}.")

if __name__ == "__main__":
    main()