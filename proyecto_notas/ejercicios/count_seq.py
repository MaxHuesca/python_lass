
inputfile = "dna_sequence_2.fa"

with open (inputfile, "r") as infile: 
    #creamos una lista con cada elemento como una linea del archivo  con el metodo readline 
    lineas=infile.readlines() 
    #con comopresion de listas hacemos una lista de todas las lineas que inicie con >
    num_lineas = [linea for linea in lineas if linea[0]== ">"] 
    print(f"{len(num_lineas)}")