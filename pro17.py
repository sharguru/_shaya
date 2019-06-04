u=int(input())
s=0
t=u
while t>0:
  d=t%10
  s=d**len(str(u))
  t=t//=10
if t==u:
  print("yes")
else:
  print("no")
