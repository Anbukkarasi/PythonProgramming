n = int(input("Enter n"))
k = int(input("Enter k"))
c=0
for i in range(n,k+1):
    for j in range(2,i):
        if(j*j == i):
            c = c+1

print(c)  
