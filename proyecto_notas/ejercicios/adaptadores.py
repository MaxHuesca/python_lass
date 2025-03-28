#Guardamos el archivo de entrada en una variable y creamos el de salida 
inputfile= "input_adapters.txt"
outputfile= "input_no_adapters.txt"
#abrimos el archivo en la variable infile y el de salida en outfile 
with  open (inputfile, "r")  as infile, open (outputfile, "w") as outfile:
   #lso adaptadores se encuentran en cada linea por lo que 
   for linea in infile: 
      secuencia_limpia= linea.strip()[14:]
      outfile.write(f"{secuencia_limpia}\n")