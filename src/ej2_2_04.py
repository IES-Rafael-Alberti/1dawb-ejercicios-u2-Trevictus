"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""



def cuentaAtras(num: int):
    
    contador = num
    while contador > 0:
        contador = contador - 1
        print (contador)
    
    


def main():
    num = int(input("Introduce numero: "))
    
    cuentaAtras(num)


if __name__ == "__main__":
    main()
