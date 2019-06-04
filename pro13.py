ni=int(input())
cc=0
for i in range(1,ni+1):
  if ni%i==0:
    cc+=1
if cc==2:
  print("yes")
elif cc>2:
  print("no")
