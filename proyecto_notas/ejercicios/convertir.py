#Guardamos el archivo de entrada en una variable y creamos el de salida 
inputfile= "dna_sequence.txt"
outputfile= "dna_sequence.fa" 
#abrimos los archivos 
with open (inputfile, "r") as infile, open (outputfile, "w") as outfile: 
   #ciclo for para it extrañendo cada linea
    for line in infile: 
        #cada linea tiene 2 elementos por lo que al crear la lista desempaquetamos cada elemento separaado en cada variable id y seq 
        id, seq = line.strip().split("\t")
        #escribimos en el archivo de salida en formato fasta 
        outfile.write(f">{id}\n{seq.upper()}\n") 
