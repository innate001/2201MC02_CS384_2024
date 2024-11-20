def check(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def rotate(n):
    s = str(n)
    f=True
    for i in range(len(s)):
      f&=check(int(s[i:] + s[:i]))
    return f
n=int(input())
if rotate(n):
  print("YES!!")
else:
  print("Nahh")