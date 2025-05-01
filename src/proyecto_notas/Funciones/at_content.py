def at_content(seq, sig_figs): 
    """
    Calcula el contenido AT de una secuencia de ADN,
    redondeando a un número específico de cifras decimales.
    Parámetros:
    dna (str): Secuencia de ADN (ej. 'ATGCGC')
    sig_figs (int, opcional): número de cifras decimales (por defecto = 2)
    Retorna:
    float: contenido AT redondeado
    """
    seq= seq.upper()
    a_cont=seq.count("A")
    t_cont=seq.count("T")
    return round((a_cont+t_cont)/len(seq),sig_figs)

secuencia=input("Ingresa una secuenica de DNA:")

at_content(secuencia,2)
#Evaluando el funcionamiento at_content
assert at_content(secuencia, 2)==0.5
