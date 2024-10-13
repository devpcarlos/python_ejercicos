numeros = [1,2,3,4,5,6,7]
ceros=[0] * 10
rango = list(range(1, 11))

print(rango)

primero, *otros = numeros
print(primero)

nombres = ["carlos", "sarah", "dianis"]

print(nombres[0])

nombres[0]="Bicho"
print(nombres )

nombres.insert(1, "kakaroto")
nombres.append("jesus")
nombres.remove("kakaroto") 

for nombre in enumerate(nombres):
    print(nombre)


