"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	      Puntuación
Inaceptable 	0.0
Aceptable	    0.4
Meritorio	    0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario."""


def pedirPuntos(puntos):
    if puntos == 0.0 or puntos == 0.4 or puntos >= 0.6:
        return True
    else:
        return False
    
def obtenerDinero(puntos):
    puntuacion = 2400 * puntos 
    return puntuacion

def obtenerNivel(puntos):
    if puntos == 0.0:
        return "Inaceptable"
    elif puntos == 0.4:
        return "Aceptable"
    elif puntos >= 0.6:
        return "Meritorio"
    else:
        return "ERROR"
    
    
def main():
    puntos = float(input("Introduce los puntos de mérito: "))

    if puntos == 0.0 or puntos == 0.4 or puntos >= 0.6:
        print("Obtienes nivel", obtenerNivel(puntos), "y tu bonificación asciende a", obtenerDinero(puntos))
    else:
        print("ERROR")
    


if __name__ == "__main__":
    main()