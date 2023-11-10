"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error."""

def divisionNumeros(num1, num2):
    if num2 == 0:
        division = "ERROR"
    else:
        division = str(num1/num2)

    return division


def main():
    num1 = float(input("introduce un dividendo: "))
    num2 = float(input("Introduce un divisor: "))

    print(f"El resultado de la operación {num1}/{num2} = {divisionNumeros(num1, num2)}")

if __name__ == "__main__":
    main()
