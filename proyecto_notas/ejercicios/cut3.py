#pedimos las secuencias y las separamos por comas para convertirla en una lista
secuencias= input("Dame secuencias separadas por comas ").split(",")
#con compresion de listas hacemos la lista con los 3 primeros nucleotidos de cada linea 
cut3=[secuencia[0:3] for secuencia in secuencias]
#imprimios la lista
print(cut3)
