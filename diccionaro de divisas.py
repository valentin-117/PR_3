
# Diccionario de divisas
print("")
print("Este es un programa que nos dirá el simbolo de una de las 3 monedas mundiales. ")#imprime la funcion del programa 
print("")
print("Frías Villa Angel Valentin 3W. ") #imprime mi nombre
print("")
divisas = {'Euro': '€',
        'Dollar': '$',
        'Yen': '¥' }

# solicita al ususario ingresar una divisa.
divisa_usuario = input("Introduce una divisa (Euro, Dollar, Yen): ")

# muestra al usuario el símbolo de la divisa o un mensaje de error
if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es: {divisas[divisa_usuario]}")
else:
    print("La divisa ingresada no está en las opciones.")

