import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    contents = line.strip().split('\t')
    outfile.write(contents[len(contents)-1])
    outfile.write('\t')
    for i in range(len(contents)-1):
        outfile.write(contents[i])
        if (i != len(contents)-2):
            outfile.write('\t')
        else:
            outfile.write('\n')
