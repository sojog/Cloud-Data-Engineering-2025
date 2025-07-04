lista_mea = ["Duminica",
    "Luni",
    "Marti",
    "Miercuri",
    "Joi",
    "Vineri",
    "Sambata",]

aux = lista_mea[0]
for i in range(len(lista_mea)-1):
    lista_mea[i] = lista_mea[i + 1]

lista_mea[len(lista_mea) - 1] = aux

print(lista_mea) 