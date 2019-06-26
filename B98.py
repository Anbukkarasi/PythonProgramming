n= int(input())
L = []
for i in range(1,n+1,1):
  L.append(int(input()))
for j in range(0,n+1,1):
  if L[j] > L[j+1]:
    print(j)
    break;
