"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""


def pedirNombre(nombre, genero):

    if genero == "M":
        if nombre.lower() < "m":
            return "A"
        else:
            return "B"
    else:
        if nombre.lower() > "n":
            return "A"
        else:
            return "B"

    




def main():
    nombre = input("Introduce nombre: ")
    genero = input("Introduce tu genero (M o H): ")

    print("Tu grupo es el ", pedirNombre(nombre, genero))



if __name__ == "__main__":
    main()
    