
import sys

sys.path.append('../rosalind_files')
import filereader


def main():
    file = filereader.getFile()
    fileData = file.read().replace("\n","")
    
    print(fileData)


main()
