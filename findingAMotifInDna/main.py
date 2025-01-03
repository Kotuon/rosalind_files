
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)
    fileData = file.read()

    seq, sub = fileData.split()

    output = ""

    lastIndex = 0
    while (True):
        index = seq.find(sub, lastIndex)

        if index == -1:
            break
        else:
            output += str(index + 1) + " "
            lastIndex = index + 1

    print(output.strip())


main()
