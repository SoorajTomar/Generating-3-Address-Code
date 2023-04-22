a=input("Enter expression")
s=list(a[2:])
print(s)
d={'-':1,'+':2,'*':3,'/':4}
j=0
while len(s)!=1:
    maxp=0
    k=0
    for i in s:
        maxp=max(maxp,d.get(i,0))
    if maxp==0:
        break
    for i in range(len(s)):
        if d.get(s[i],0)==maxp:
            k=i
            break
    ans=["t"+str(j)]+["="]+s[i-1:i+2]
    print(*ans)
    s=s[:i-1]+["t"+str(j)]+s[i+2:]
    j+=1
print(*(list(a[:2])+s))
