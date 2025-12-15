def to_rna(dna_strand):
    rna = ''
    for elem in dna_strand:
        if elem == 'G': rna += 'C'
        elif elem == 'C': rna += 'G'
        elif elem == 'T': rna += 'A'
        elif elem == 'A': rna += 'U'
        else: rna += elem
    return rna