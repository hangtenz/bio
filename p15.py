f = open('p15.fasta')
name = []
dna = []
for line in f:
    line = line.strip()
    if(line[0] == '>'):
        name.append(line[1:])
        dna.append("")
    else:
        dna[-1] = dna[-1] + line

idx_max = -1
max_cg = 0

for i in range(len(dna)):
    cg = 0
    for j in range(len(dna[i])):
        if(dna[i][j]=='C' or dna[i][j]=='G'):
            cg+=1
    p_cg = (cg/len(dna[i]))*100
    if(p_cg>max_cg):
        max_cg = p_cg
        idx_max = i
print(name[idx_max])
print(max_cg)