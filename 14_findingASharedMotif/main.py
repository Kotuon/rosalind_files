
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8
import fastaParser  # nopep8


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)

    dnaSequences = fastaParser.parse(file)
    sequenceLength = len(dnaSequences[0].sequence)

    longestSubstring = ""
    for i in range(0, sequenceLength):
        for dna in dnaSequences:
            


main()
