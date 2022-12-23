
the_list = {}
the_list = {"Combo 1":["Agua", "Chicharrón preparado", "Dulce"], "Combo 2":["Refresco", "Palomitas", "Dulce"]}
the_list["Combo 3"] = ["Refresco", "Palomitas", "Dulce"]

#Agrega en caso de que no exista
the_list.update({"Combo 4" :["Agua", "Chicharrón preparado", "Dulce"]})

#Modifica por llave
the_list["Combo 4"] = ["HOLA"]
the_list.update({"Combo 4" :["Agua", "Chicharrón preparado", "Dulce"]})


#ZIP
names = ['Ana', 'Diana', 'Arely', 'Araceli']
heights = [61, 70, 67, 64]
zip_persons = zip(names,heights)
heights_persons = {key:value for key, value in zip(names, heights)}

try:
  print(the_list["Combo 5"])
except KeyError:
  print("No existe")

the_list_key = the_list.get("Combo 5", "No está")  
print(the_list_key)

the_list.pop("Combo 1", "No se encontró")
print(the_list)

for combo in the_list.keys():
  print(combo)

for combo in the_list.values():
  print(combo)

