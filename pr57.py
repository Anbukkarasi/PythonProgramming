a = input()
b = input()
l = list(a)
print(l)
for i in range(0,len(l)-1):
  s = l[i] + l[i+1]
  print(s)
  if s in b:
    print("yes")
    break
