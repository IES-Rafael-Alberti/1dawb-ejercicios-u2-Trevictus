"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

def parImpar(num):

    if num%2 == 0:
        resultado = "par"

    else:
        resultado = "impar"
    
    return resultado

def main():
    num = int("Introduce un nº: ")

    print("El nº introducido es", parImpar(num))



if __name__ == "__main__":
    main()   