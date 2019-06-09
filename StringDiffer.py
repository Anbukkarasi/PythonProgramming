s1 = input("Enter s1")
s2 = input("Enter s2")
n = int(input("Enter n"))
c=0
for i in range(0,len(s1)):
    if(s1[i] != s2[i]):
        c = c + 1
if(c == n):
    print('Yes')
else:
    print('No')
