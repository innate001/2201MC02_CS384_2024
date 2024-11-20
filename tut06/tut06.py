def main():
  Int =set(map(int,input().split()))
  Sym =set(['@','&','%'])
  x = 0;
  while 1:
    x=input("Enter Your Password : ")
    if len(x)<8 :
      print("Too Short")
      continue
    a,A,d,s=[],[],[],[]
    f=True
    for i in x:
      if i.isupper() : A.append(i)
      elif i.islower() : a.append(i)
      elif i.isdigit() :
        d.append(i)
        if int(i) not in Int :
          f=False;
          print(f"Invalid Number {i}")
      else :
        s.append(i)
        if i not in Sym :
          f=False;
          print(f"Invalid Symbol {i}");
    if len(a)==0:
      print("add Lowercase letters too")
      f=False;
    if len(A)==0:
      print("add Uppercase case letters too")
      f=False;
    if len(d)==0:
      print("add some numbers too")
      f=False;
    if len(s)==0:
      print("No Symbols")
      f=False;
    if f:
      print("Password Saved")
      break;
  print(f"your password is : {x}")

if __name__== "__main__": main()