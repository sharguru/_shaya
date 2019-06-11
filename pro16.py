s,t=map(int,input().split())
for i in range(s,t+1):
  u=0
  for j in range(1,t):
    if i%j==0:
      u+=1
  if u==2:
    print(i,end=" ")
