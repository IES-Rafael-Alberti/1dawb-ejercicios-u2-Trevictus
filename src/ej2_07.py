"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""


def rentaAnual(renta):

    if renta < 10000:
        return "5%"
    elif renta >= 10000 and renta <= 20000:
        return "15%"
    elif renta >= 20000 and renta <= 35000:
        return  "20%"
    elif renta >= 35000 and renta <= 60000:
        return "30%"
    else:
        return "45%"
    
    
def main():
    renta = int(input("Introduce tu cantidad de ingresos: "))
    porcentaje = rentaAnual(renta)
    print(f"El impuesto tuyo asciende a {porcentaje}")


if __name__ == "__main__":
    main()