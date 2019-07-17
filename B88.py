s1 = input()
l = list(s1)
newl = []
flag = True
print(l[0] > l[1])
for i in range(0,len(l),1):
  for j in range(i+1,len(l),1):
    if(l[i] > l[j]):
      t = l[i]
      l[i] = l[j]
      l[j] = t
  newl.append(l[i])

print("".join(newl))
