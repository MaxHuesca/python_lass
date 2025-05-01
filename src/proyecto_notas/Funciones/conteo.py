def count_bases(dna): 
    dna=dna.upper()
    print(f"A: {dna.count("A")},C: {dna.count("T")}, C: {dna.count("C")}, G: {dna.count("G")}")
       
seq="ATGACGATAGA"
count_bases(seq)
