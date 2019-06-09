n = int(input("Enter n"))
k = int(input("Enter k"))
nlist = []
klist = []
for i in range(0,n):
  nlist.append(int(input()))
for i in range(0,k):
  klist.append(int(input()))
for j in klist:
  nlist.append(j)
  print(max(nlist))
