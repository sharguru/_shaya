i,r=map(int,input().split())
o=[]
for x in range(i+1,r):
  if x%2==0:
    o.append(x)
print(*o)
