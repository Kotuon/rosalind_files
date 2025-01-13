
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)
    fileData = file.read()

    print(fileData)


main()
