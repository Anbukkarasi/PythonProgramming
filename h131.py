import math
n = int(input())
l=[]
for i in range(1,n+1,1):
  l.append(int(input()))

l1 = l
l2 = l
l3 = []

l1.sort()
l2.sort(reverse=True)
s = len(l) - 1

t = math.ceil((s+1)/2)

for i in range(0,t,1):
  l3.append(l2[i])
  if(i!=s):
    l3.append(l2[s])
    s=s-1

print(l3)
