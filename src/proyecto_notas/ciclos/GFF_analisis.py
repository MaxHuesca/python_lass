#leemos el archivo con with open para cerrarlos automaticamente 
with open ("C:\Users\vrahu\OneDrive\Documentos\Ismadlsh\CCG\2025-S2\Git-Py\python_class\proyecto_notas\genes.gff") as archivo:
    #con el ciclo for iremos leyendo cada linea del archivo 
    for linea in archivo: 
        #por cada linea va a quitar los espacios extra con strip y separara cada tabulador como un elemento de la lista columanas
        i=1
        columas=linea.strip().split("\t")
        taman=int(columas[3]) - int(columas[4])+1
        print(f"El {columas[2], i} tiene una longitud de {taman}")
        i+=1
        