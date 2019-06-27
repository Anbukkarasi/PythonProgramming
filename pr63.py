s1 = input()
c=0
max = 0
n = len(s1)
for i in range(0,n,1):
  for j in range(i+1,n,1):
   if(s1[i] != s1[j]):
    c = c + 1
   else:
     break
  if (c > max):
    max = c
  c = 0
print(max)
  
