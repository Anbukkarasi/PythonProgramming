n= int(input())
while(n!=0):
  r = int(n %10)
  n = int(n / 10)
  print(r,end="")
