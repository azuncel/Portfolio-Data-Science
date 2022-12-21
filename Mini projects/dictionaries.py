#Diccionarios
usuarios = [
    {"id": 0, "nombre": "Diana"},
    {"id": 1, "nombre": "Emily"},
    {"id": 2, "nombre": "Hiram"},
    {"id": 3, "nombre": "Elias"},
    {"id": 4, "nombre": "Anna"},
    {"id": 5, "nombre": "Carlos"},
    {"id": 6, "nombre": "Gerardo"},
    {"id": 7, "nombre": "Maricela"},
    {"id": 8, "nombre": "Araceli"},
    {"id": 9, "nombre": "Aura"},
]

#Tupla
amistades_pares = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Inicializar diccionario
amistades = {usuario["id"]: [] for usuario in usuarios}

# amistades ={}
# for usuario in usuarios:
#     amistades[usuario['id']] = []

for i,j in amistades_pares:
    amistades[i].append(j)
    amistades[j].append(i)


print(amistades)