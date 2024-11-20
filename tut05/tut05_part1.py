a= input();
a=a.split()
for i in range(len(a)):
  a[i]=int(a[i])
a.sort();
ans=[]
for i in range(len(a)):
  l=i+1;
  r=len(a)-1;
  if(i>0 and a[i]==a[i-1]):
    continue;
  while l<r:
    if(l>i+1 and a[l]==a[l-1]):
      l+=1;
      continue
    if(r<len(a)-1 and a[r]==a[r+1]):
      r-=1;
      continue;
    if(a[i]+a[l]+a[r]==0):
      ans.append([a[i],a[l],a[r]])
      l+=1
      r-=1
    elif(a[i]+a[l]+a[r]<0):
      l+=1
    else:
      r-=1
print(ans)


