
s=input()
a=[]
f=True
for c in s :
  if(c=='(' or c=='{' or c=='['):
    a.append(c)
  elif(c==')'):
    if(a[-1]=='('):
      a.pop()
    else:
      f=False
      break
  elif(c=='}'):
    if(a[-1]=='{'):
      a.pop()
    else:
      f=False
      break
  elif(c==']'):
    if(a[-1]=='['):
      a.pop()
    else:
      f=False
      break
if(f and len(a)==0):
  print("It is Balanced")
else :
  print("Not Balanced")
