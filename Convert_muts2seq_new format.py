import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sequence', help='sequence of the reference/wt protein/DNA/RNA')
parser.add_argument('-f', '--file', help='name of the input file with sequences of genotypes')
parser.add_argument('-o', '--output', help='name of the output file where mutations are written', default='output.txt')
parser.add_argument('-v', '--values', help='fitness values of inputed sequences', default='No')
args = parser.parse_args()

with open(args.output, 'w') as f:
    reference = args.sequence
    print(reference, file =f)
    with open(args.file) as csv_file:
        csv_reader = csv.reader(csv_file)
        # Wild-type sequence
        reference = args.sequence
        for row in csv_file:
            if row == '\n':
                print(reference, file=f)
            else:
                row = row.strip()
            #separate sequence from fitness
            separate = row.split(";")
            positions = separate[0].split(":")
            newRow=[]
            term = reference
            for x in positions:
            #TODO check that the aminoacid in the sequence is consistant wih the mutant file
                position = int(x[1:-1])
                mut = x[-1]
                head = term[:position -1]
                tail = term[position:]
                #newRow.append(term)
                term = head+mut+tail
            #print(newRow)
            if args.values == "Yes":
                print( term +";" + separate[1], file=f)
                term = reference
            else:
                print(term, file=f)
                term = reference

