"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)"""

def pedirEdad(edad):
    cont = 1
 
    while cont < 125:
        cont += 1
    return edad
    

def main():
    edad = input("Teclee su edad: ")
    print(pedirEdad(edad))

if __name__ == "__main__":
    main()