#Pedimos las secuencias y las ponemos en una lista 
Secuencias= input("Inserte secuencias de DAN separadas por una coma").split()
#Guardamos listas dentro de otras listas con corchetes cuadrados (listas anidadas), por cada secuencia insertada 
Nucleotidos=[[f" A:{secuencia.count('A')} C: {secuencia.count('C')} G:{secuencia.count('G')} T:{secuencia.count('T')}"] for secuencia in Secuencias] 

print(Nucleotidos)