#pedimos las secuencias a traves del teclado y lo convertimos en una lista
Secuencias= input("Dame una secuencias de DNA se paradas por una coma para tranformarla en RNA").split(",")
#con el metodo replace remplazamos cada aparicion de T por una U 
RNA= [secuencia.replace("T", "U").strip() for secuencia in Secuencias] 
#imprimimos la lista 
print(RNA)