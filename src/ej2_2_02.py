"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)"""

def pedirEdad(edad):
    cont = 1
    resultado = ""
 
    while cont <= edad:
        resultado = resultado + (f"{cont}   ")
        cont = cont + 1
    return resultado


    

def main():
    edad = int(input("Teclee su edad: "))
    fin = pedirEdad(edad)
    print(fin)

    



if __name__ == "__main__":
    main()