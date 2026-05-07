
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8
import codonDict  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)
    fileData = file.read().replace("\n", "")

    condonList = codonDict.getCodonDict()

    outputString = ""

    for i in range(0, len(fileData), 3):
        outputString += condonList[fileData[i:i+3]]

    print(outputString.replace("O", ""))


main()
