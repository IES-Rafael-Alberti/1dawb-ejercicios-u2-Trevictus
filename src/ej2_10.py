"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""




def pedirPizza(pizza):
    pizza = int
    if pizza == 1:

        print(input("¿Desea pimiento (1), tofu (2) o ambos (3)?: "))
    
        if pizza == 1:
            print("Su pizza es vegetariana con los ingredientes: mozarella, tomate y pimiento.")
        elif pizza == 2:
            print("Su pizza es vegeetariana con los ingredientes: mozarella, tomate y tofu.")
        elif pizza == 3:
            print("Su pizza es vegetariana con los ingredientes: mozarella, tomate, pimiento y tofu.")
        else:
            print("No es una elección adecuada.")

    
    elif pizza == 2:
        print(input("¿Desea peperoni (1), jamón(2), salmón(3), peperoni y jamón (4), peperoni y salmón (5) o salmón y jamón (6)?"))
        if pizza == 1:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate y peperoni.")
        elif pizza == 2:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate y jamón.")
        elif pizza == 3:
            print("Su pizza es no vegetariana con los ingredientes: mozarlla, tomate y salmón.")
        elif pizza == 4:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate, peperoni y jamón.")
        elif pizza == 5:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate, peperoni y salmón.")
        elif pizza == 6:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate, salmón y jamón.")
        elif pizza == 7:
            print("Su pizza es no vegetariana con los ingredientes: mozarella, tomate,peperoni, jamón y salmón.")
        else:
            print("Elige una opción posible.")


    elif pizza != 1 or pizza != 2 or pizza == str:
        print("Pizza incorrecta")


def main():
    
    pizza = input("Elige si quieres la pizza vegetariana (1) o no vegetariana (2): ")
    pedirPizza(pizza)



if __name__ == "__main__":
    main()
