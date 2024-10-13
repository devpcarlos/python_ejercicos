numeros = [9,2,5,6,7,8]

#numeros.sort(reverse=True)
num= sorted(numeros)
print(numeros)
print(num)

usuarios =[
    [ " CARLOS", 4],
    ["JESUS", 2],
    ["BARRERA",1]
    ]
usuarios.sort(key=lambda x: x[1], reverse=True)
print(usuarios)

nombres=[]
for usuario in usuarios:
    nombres.append(usuario[0])
    print(nombres)

#Map
nombres=[usuario[1] for usuario in usuarios]
print(nombres)

#Filter
nombres=[usuario[0] for usuario in usuarios if usuario[1]>2]
print(nombres)

nombres=(map(lambda usuario: usuario[0], usuarios))
print(nombres)

menosUsuario = list(filter(lambda usuario: usuario[1]>2, usuarios))
print(menosUsuario)
