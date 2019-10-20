k = int(input())
f = open('p12.txt')
dna = []
for line in f:
    dna.append(line.strip())

def generate_motif(k,ans):
    if(k==0): return ans
    ans2  = []
    for i in range(len(ans)):
        ans2.append(ans[i]+'A')
        ans2.append(ans[i]+'C')
        ans2.append(ans[i]+'T')
        ans2.append(ans[i]+'G')
    return generate_motif(k-1,ans2)

motif = generate_motif(k,[''])

min_distance = 99999
idx_distance = -1

def motif_distance(motif,dna):
    min_distance = 99999
    for i in range(len(dna)-k):
        temp_dna = dna[i:i+k]
        distance = 0
        for j in range(len(motif)):
            if(temp_dna[j]!=motif[j]):
                distance+=1
        if(distance<min_distance):
            min_distance = distance
    return min_distance                

for i in range(len(motif)):
    distance = 0
    for j in range(len(dna)):
        distance += motif_distance(motif[i],dna[j])
    if(distance<min_distance):
        min_distance = distance
        idx_distance = i
print(motif[idx_distance])
