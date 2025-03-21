#ingresar numeros por el teclado y guardarlos como lista por la funcion split 
numero_str= input("Inserte 4 numeros separados pos espacios ").split()
print(numero_str) 
#Map es un objeto iterable que puede ser usado por sum 
print(f"La suma de los numeros es {sum(map(int,numero_str))}")
#cambiar los numeros de la lista de caracteres a int para sumarlos con la funcion map()
numero_str=list(map(int, numero_str))
suma=sum(numero_str)
print(numero_str)
print(f"La suma de lso numeros insertados es {suma}") 

