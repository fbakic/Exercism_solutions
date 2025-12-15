def to_rna(dna_strand):
    rna = ''
    interference = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U',
    }
    for elem in dna_strand:
        rna += interference[elem]
    return rna