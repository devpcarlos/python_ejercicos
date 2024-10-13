punto={"x": 25, "y": 40}
print(punto)
print(punto["x"])
print(punto.get("x"))
del punto["x"]

usuarios = [
    {"id":1, "Nombre":"carlos"},
{"id":2, "Nombre":"k"},
{"id":3, "Nombre":"jose"},
{"id":4, "Nombre":"estebana"}
]

for usuario in usuarios:
    print(usuario["Nombre"])

