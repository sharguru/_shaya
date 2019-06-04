e,r=map(int,input().split())
o=[]
for i in range(e+1,r+1):
  if i%2!=0:
    o.append(i)
print(*o)
