s = input("Enter String")
s1=''
s = s.strip()
s = s.lstrip()
s = s.rstrip()
for i in s:
    if( i != ' '):
        s1 = s1 + i
print(s1)
