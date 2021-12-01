def funcion(x):
    #aqui se definio la funcion a la cual se le desa saber la raiz aproximada
    return (((-x) ** 4) + (30 * (x ** 3)) + (15 * (x ** 2)) + (34 * x) + 540)


def biseccion(x0, x1):
    #Se asigna el valor de exactitud deseada
    exactitud = 0.001
    #Se realiza la aproximacion de la raiz entre los intervalos
    m = (x0 + x1) / 2
    #Se verifica que la cnvergencia de la raiz sea menor a la de la exactud
    #de ser asi la raiz estaria dada por la aproximacion de los intervalos
    if abs((funcion(m) - funcion(x0)) / funcion(m)) < exactitud:
        print("La aproximacion de la raiz es: ", m)
        return 0
    #Se analiza si la raiz está aproximada a la derecha o a la izquierda de la raiz m, para ir reduciendo las opciones
    if (funcion(x0) * funcion(m)) <= 0:
        #Se utiliza la recursividad para seguir iterando las raices obtenidas
        biseccion(x0, m)
    else:
        #Se utiliza la recursividad para seguir iterando las raices obtenidas
        biseccion(m, x1)


if __name__ == '__main__':
    # Se hace el ingreso de los valores de las variables independientes y se verifica si el intervalo escogido contiene una raiz
    # Se realzia la iteracion hasta conseguir un intervalo con una raiz valida
    while (True):
        print("Ingrese el valor de x0:")
        x0 = int(input())
        print("Ingrese el valor de x1:")
        x1 = int(input())
        if ((funcion(x0) * funcion(x1)) < 0):
            break
        else:
            print("Los intervalos no son validos, ingrese los valores nuevamente")
    #Se llama a la funcion biseccion para hacer el procedimeinto
    biseccion(x0, x1)
