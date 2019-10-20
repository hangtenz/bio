s = input()
s2 = ""
s3 = ""
n = len(s)
for i in range(n):
    s2 += s[n-1-i]
for i in range(n):
    if(s2[i]=='A'):
        s3+='T'
    elif(s2[i]=='T'):
        s3+='A'
    elif(s2[i]=='C'):
        s3+='G'
    elif(s2[i]=='G'):
        s3+='C'
print(s3)