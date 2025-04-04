secuencia = "ATGCGTAGC" 
#Convertimos a tupla 
seq_tup = tuple(secuencia) 
#lo recorremos con ciclo for ya que es un iterable e imprimimos cada elemento 
for base in seq_tup:
    #modificamos el caracter impreso por default que es el salto de linea por un espacio
    print(base, end=" ")