#Creamos la tupla con la funcion tuple a partir de un string
seq= tuple("ATGCGTAGC")
bases = list("ATCG")
#Impimimos cada ocurrencia con el metodo count y el formateo de cadenas
print(f"A: {seq.count("A")}, C: {seq.count("C")}, T: {seq.count("T")},G: {seq.count("G")} ") 
#con un ciclo iterativo y formateo de cadenas 
for base in bases: 
    print(f"{base}: {seq.count(base)}", end= " ") 

#compresion de listas 
freq= [(f"{base}: {seq.count(base)}") for base in bases]
print("\n", freq)
