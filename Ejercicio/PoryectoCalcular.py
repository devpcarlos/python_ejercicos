print("Bienvenidos a la calculadora")
print("Para salir escriba salir")

comando=""

while comando !="salir":
      n1=input("Ingresa un numero: ")
      n1 = int(n1)
      operacion = input("Ingresa la operacion: ")
      n2 = input("Ingresa el siguiente numero: ")
      n2 = int(n2)

      suma = n1 + n2
      mult = n1 * n2
      if operacion == "suma":
         print(suma)
      elif operacion == "mult":
         print(mult)






