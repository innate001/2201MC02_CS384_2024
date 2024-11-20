def fun(s):
    n = len(s)
    s = list(s)
    result = []
    c = [0] * n
    result.append(''.join(s))
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                s[0], s[i] = s[i], s[0]
            else:
                s[c[i]], s[i] = s[i], s[c[i]]
            result.append(''.join(s))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i+=1;

    return result

s = str(input())
ans = fun(s)
for x in ans:
    print(x)