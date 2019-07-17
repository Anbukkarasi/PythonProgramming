s1 = input()
s2 = 'aeiou'
flag = False
for i in range(0,len(s1),1):

  if(s1[i] in s2):
    print('yes')
    flag = True
    break;
if (flag == False):
  print('no')
