s = input()
l=[]
if '%' in s:
  l = s.split("%")
  print (int(l[0]) % int(l[1]))
else:
  l = s.split("/")
  print(int(l[0]))
  print(int(l[1]))
  print (int(l[0]) / int(l[1]))
