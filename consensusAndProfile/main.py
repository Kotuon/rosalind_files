
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8
import fastaParser  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)

    dnaSequences = fastaParser.parse(file)
    sequenceLength = len(dnaSequences[0].sequence)

    # ACGT
    keys = ['A', 'C', 'G', 'T']

    table = dict((keys[i], [0 for j in range(sequenceLength)])
                 for i in range(0, 4))

    for i in range(0, sequenceLength):
        for line in dnaSequences:
            table[line.sequence[i]][i] += 1

    output = ""
    for i in range(0, sequenceLength):
        currMax = ('',  -1)
        for key in keys:
            if table[key][i] > currMax[1]:
                currMax = (key, table[key][i])
        output += currMax[0]

    print(output)
    for k, v in table.items():
        print(k + ": " + ' '.join(map(str, v)))


main()
