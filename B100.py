n= int(input())
p = 1
while(n!=0):
  r = int(n %10)
  n = int(n / 10)
  if r != 0:
    p = p * r
print(p,end="")
