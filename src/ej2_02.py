"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
------retorna la cadena de caracteres-> contraseña
"""

def pedircontraseña():

    salir = False

    while not salir:
        entrada = input("Introduzca contraseña: ")

        if entrada.isalpha() and len(entrada) == 10:
            salir = True
        else:
            print("Contraseña no coincide con contraseña.")


    return entrada  


    """e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
    ------True la contraseña coincide-----
    ------False la contraseña no coincide-----
    """


def coincideContrasenia(contrasenia, entrada):
    if contrasenia.upper() == entrada.upper():
        return True
    else:
        return False
    

def main():
    contrasenia = "contraseña"
    entradaUsuario = pedircontraseña()

    if coincideContrasenia(contrasenia, entradaUsuario):
        print("La contraseña coincide.")

    else:
        print("La contraseña no coincide.")

if __name__ == "__main__":
    main()