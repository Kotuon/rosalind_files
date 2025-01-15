
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8


evMatrix = [1, 1, 1, 3/4, 1/2, 0]
offspringCount = 2


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)
    fileData = file.read().replace("\n", "")

    values = list(map(int, fileData.split(' ')))

    result = 0
    for i in range(len(values)):
        result += evMatrix[i] * offspringCount * values[i]

    print(result)


main()
