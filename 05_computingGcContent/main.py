
import os
import sys


class FastaSequence:
    def __init__(self, label, sequence, gcContent):
        self.label = label
        self.sequence = sequence
        self.gcContent = gcContent


def fastaParser(file):
    fastaList = []
    for line in file:
        if line[0] == ">":
            fastaList.append(FastaSequence(line.replace('\n', ''), "", 0.0))
        else:
            fastaList[-1].sequence += line.replace('\n', '')

    return fastaList


def calculateGc(fastaList):
    for item in fastaList:
        item.gcContent = ((item.sequence.count('C') + item.sequence.count('G'))
                          / len(item.sequence))

        item.gcContent *= 100.0


def compareGc(fastaList):
    highest = 0
    for i in range(1, len(fastaList)):
        if fastaList[i].gcContent > fastaList[highest].gcContent:
            highest = i

    return highest


def main():
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(directory)

    fileName = input("Enter file name: ")

    file = open(directory + "\\" + fileName, "r")

    myList = fastaParser(file)
    calculateGc(myList)

    for item in myList:
        print(item.label + '\n' + item.sequence + '\n' +
              "{:.9}".format(str(item.gcContent)))

    highest = compareGc(myList)
    print("\nHighest:")
    print(myList[highest].label + '\n' +
          "{:.9}".format(str(myList[highest].gcContent)))


main()
