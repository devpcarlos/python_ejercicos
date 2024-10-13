def hola(nombre):
    print("Programado desde python")
    print(f"Bienvenido {nombre}")


hola("Carlos")


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(1, 2, 3, 4, 5)
suma(3, 4, 7)


def get_product(**datos):
    print(datos)

get_product(id="id")


def get_suma(a , d):
    resultado = a + d
    return resultado

rs= get_suma(1, 2)
print(rs)
