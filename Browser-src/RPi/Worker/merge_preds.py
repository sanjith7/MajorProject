filenames = []
for j in range(1,40): #This is to be replaced with the array obtained as input from the manager node.
    filenames.append('result{0}.txt'.format(j))
with open('result.txt', 'w') as outfile:
    for fname in filenames:
        try:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line+ " ")
        except:
            continue
