a,b=(map(int,input().split()))
d=list(map(int,input().split()))
co=d.count(a)
print(co)
c=0

for i in range(0,a):
    c=c+d[i]
print(c)
if co==a and c==b:
    print("yes")
else:
    print("no")
