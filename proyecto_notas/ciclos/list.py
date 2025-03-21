apes=["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

#Anteriormente se usaba + para concatenar cadenas con el uso de str 
for ape in apes: 
    name_len=len(ape)
    first_letter= ape[0]
    print(ape + "is an ape. Its name starts with" + first_letter)
    print("Its name has " + str(name_len) + "letters") 

#Actualmente se usa fstring para formatear cadenas 

for ape in apes: 
    name_len=len(ape)
    first_letter= ape[0]
    print(f"{ape} is an ape. Its name starts with {first_letter}")
    print(f"Its name has {name_len} letters")
