n = int(input("Enter n"))
l = []
for i in range(0,n):
  s = input()
  l.append(s)
for i in range(0,len(l)-1):
    print(len(l[i]))
    if len(l[i]) > len(l[i+1]):
        t = l[i]
        l[i] = l[i+1]
        l[i+1] = t
    elif(len(l[i]) == len(l[i+1])):
        if(l[i] > l[i+1]):
            t = l[i]
            l[i] = l[i+1]
            l[i+1] = t
print(l)
