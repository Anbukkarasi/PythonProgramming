s1 = input()
c=0
s='0123456789'
for i in range(0,len(s1),1):
  if s1[i] in s:
    c = c+1

print(c)
