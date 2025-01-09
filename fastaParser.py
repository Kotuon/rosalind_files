

class FastaSequence:
    def __init__(self, label, sequence):
        self.label = label
        self.sequence = sequence


def parse(file):
    fastaList = []
    for line in file:
        if line[0] == ">":
            fastaList.append(FastaSequence(
                line.replace('\n', '').replace('>', ''), ""))
        else:
            fastaList[-1].sequence += line.replace('\n', '')

    return fastaList
