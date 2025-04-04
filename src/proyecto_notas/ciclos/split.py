texto="ATG CGT TAA GGC" 
#sin valores en sus argumentos (por default)
lista= texto.split()
print(lista) 

#Cambiando el separador 
texto="ATG,CGT,TAA,GGC" 
lista= texto.split(",")
print(lista) 

#Cambiando el separador hasta un maximo de su ocurrencia 
texto="ATG,CGT,TAA,GGC" 
lista= texto.split(",",2)
print(lista) 