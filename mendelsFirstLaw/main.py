
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8


def determineProbability(kmn):
    amount = sum(kmn)
    totalPairs = amount * (amount - 1) / 2
    recPairs = kmn[2] * (kmn[2] - 1) / 2
    mixPairs = kmn[1] * (kmn[1] - 1) / 2
    mixRecPairs = kmn[1] * kmn[2]

    totalOut = totalPairs * 4
    totalRecOut = (recPairs * 4) + mixPairs + (mixRecPairs * 2)

    print(totalRecOut)

    return (totalOut - totalRecOut) / totalOut


def main():
    file = filereader.getFile()
    fileData = file.read().replace("\n", "")

    kmn = list(map(int, fileData.split()))

    probability = determineProbability(kmn)

    print(kmn)
    print(probability)


main()
