def info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")
        
        
info(nombre="Valita", edad=19)