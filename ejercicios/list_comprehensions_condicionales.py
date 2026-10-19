palabras = ["sol","murcielago", "mar" , "elefante","luz"]

lista = [palabra for palabra in palabras if len(palabra) > 3]

print(lista)

listaFor = []

for palabra in palabras:
    if (len(palabra) > 3):
        listaFor.append(palabra)
        
print(listaFor)