#pedimos las secuencias a traves del teclado y lo convertimos en una lista
Secuencias= input("Dame una secuencias de DNA se paradas por invertirlas").split(",") 
#invertimos cada secuencia convitiendolo en una lista 
Seq_invert=[secuencia.split()[::-1] for secuencia in Secuencias] 

print(Seq_invert)