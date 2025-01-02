

import filereader


def getCodonDict():
    file = filereader.getFile("../rnaCodonTable.txt")

    codonDict = {}
    
    for line in file:
        codon = line.split()
        codonDict[codon[0]] = codon[1]

    return codonDict
