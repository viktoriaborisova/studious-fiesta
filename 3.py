f=open('1788.txt')
f=list(map(int,f.readlines()))
count=0
d=[]
for i in range(len(f)):
    for j in range(1,len(f)-1):
        if (i+j)%10==0:
            d.append(i+j)
            count+=1
print(count,max(d))
