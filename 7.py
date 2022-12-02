f=open('1378.txt').readline().strip()

c=0
d={x:0 for x in sorted(set(f))}

for i in range(len(f)-4):
    if f[i]=='C'and f[i+1]=='B' and f[i+3]=='B' and f[i+4]=='C':
        c+=1
        d[f[i+2]]+=1
print(max(d),c)

        
