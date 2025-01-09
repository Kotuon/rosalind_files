
import os
import sys


def getFile(fileName):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    # print(directory)

    return open(directory + "\\" + fileName, "r")


def writeFile(outputString):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    outFile = open(directory + "\\" + "output.txt", "w")
    outFile.write(outputString)
    outFile.close()
