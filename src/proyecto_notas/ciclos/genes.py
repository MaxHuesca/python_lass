#lista de genes 
genes=["p53", "BRAc1", "BRAc2", "NIP1"] 
#Usando for en un iterable en el sentido de la lista 
for gen in genes: 
    print(f"El nombre del gen es {gen}") 

#Usando for en un iterable en sentido reverso 
#opcion uno 
for gen in reversed(genes): 
    print(f"El nombre del gen es {gen}")  

#opcion dos 
for gen in genes[::-1]: 
    print(f"El nombre del gen es {gen}")   
