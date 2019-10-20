dna = input()

array = []

for i in range(len(dna)):
    array.append((dna[i:len(dna)],i))
array.sort()
ans = ""

f = open('p13.txt', 'w' )
for i in range(len(array)):
    ans += str(array[i][1]) + ', '
ans = ans[:-2]
f.write(ans)
