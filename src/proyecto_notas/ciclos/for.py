#Uso de enumarate en un for  
secuencia="GTTCGAATACG" 

# en la sintaxis despues del for primero va a ir el indice y despues la variable que alamcenara en el iterable 
for i, base in enumerate(secuencia): 
    print(f"Posicion {i} : {base}") 

#Uso de zip para iterar en varios iterables 
bases="ATTTGGGC"
complementos="TAAAGGGC" 

for base, complemento in zip(bases, complementos): 
    print(f"{base}:{complemento}") 