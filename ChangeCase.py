s = input("Enter String")
s1=''
for i in range(0,len(s)):
  if(s[i].isupper()):
    s1 = s1 + s[i].lower()
    #print(s[i])
  if(s[i].islower()):
    s1=s1 + s[i].upper()
    #print(s[i])
print(s1) 

        
