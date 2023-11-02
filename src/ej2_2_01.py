"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

def pedirPalabra(palabra):
    result= ""
    cont=0
    while cont < 10:
        result = (result+palabra) + "\n"
        cont = cont + 1
    return result

def main():
    palabra = input("Teclee una palabra: ")
    print(pedirPalabra(palabra))


if __name__ == "__main__":
    main()