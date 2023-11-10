"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

def mayorEdad(edad):
    if edad >= 16:
        mayoria = True
    else:
        mayoria = False

    return mayoria

def ingresoMinimo(ingreso):
    if ingreso >= 1000:
        capital = True
    else:
        capital = False

    return capital

def tributacion(edad, ingreso):

    if edad >= 16 and ingreso >= 1000:
        return True
    else:
        return False
    

def main():
    edad = int(input("Introduce tu edad: "))
    ingreso = float(input("Introduce tus ingresos: "))
    if tributacion(edad, ingreso):
        print("Tienes que tributar.")

    else:
        print("No tienes que tributar.")




if __name__ == "__main__":
    main()   



