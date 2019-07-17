s1 = input()
flag = True
for i in range(0,len(s1),1):
  for j in range(i+1,len(s1),1):
    if(s1[i] == s1[j]):
      flag = False
      break
if(flag):
  print("yes")
else:
  print("no")
