n = int(input())
k= int(input())

l=[]
s = 0
s1 = 0
for i in range(0,n,1):
  l.append(int(input()))
r= int(input())
for i in range(0,n,1):
  s = s + l[i]
for i in range(0,n,1):
  if (i != k):
    s1 = s1 + l[i]
b = (int)(s1/2)
if(r == (int)(s/2)):
  print(r - b)
elif(r == b):
  print("Bon Appetit")
