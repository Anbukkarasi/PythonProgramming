l = []
for i in range(1,9,1):
  l.append(int(input()))
if l[0] == l[2] and l[3] == l[5]  and l[4] == l[6] and l[1] == l[7]:
    print("yes")
else:
    print("no")
