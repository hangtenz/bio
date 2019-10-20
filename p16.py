f = open('p16.txt')
name = []
dna = []
state = 0
for line in f:
    line = line.strip()
    if(state%4 == 0):
        name.append('>'+line[1:])
    elif(state%4 == 1):
        dna.append(line)
    state += 1

for i in range(len(name)):
    print(name[i])
    print(dna[i])
