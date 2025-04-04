Secuencias= input("Inserte secuencias de DAN separadas por una coma").split() 
#Paro=["TAA", "TAG", "TGA"]
#Secuencias_paro=[[(secuencia[i:i+3])  for i in range(0, len(secuencia),3)]  for secuencia in Secuencias if secuencia in Paro]
Secuencias_paro=[secuencia for secuencia in Secuencias if "TAA" in secuencia or Secuencias if "TGA" in secuencia or Secuencias if "TAG" in secuencia ]
print(Secuencias_paro)