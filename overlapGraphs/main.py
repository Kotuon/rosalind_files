
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8
import fastaParser  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)

    dnaSequences = fastaParser.parse(file)

    output = ""

    for dna1 in dnaSequences:
        s1 = dna1.sequence
        for dna2 in dnaSequences:
            s2 = dna2.sequence
            if s1 != s2 and s1.endswith(s2[:3]):
                output += dna1.label + ' ' + dna2.label + '\n'

    print(output)

    filereader.writeFile(output)


main()
