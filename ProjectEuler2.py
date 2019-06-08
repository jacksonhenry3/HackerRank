def g(n, I):
    if n < len(I):
        return(I[n])
    return(g(n-1,I)*4+g(n-2,I))
s = [0,2]
t = int(input().strip())
for a in range(t):
    L = len(s)
    n = int(input().strip())
    G = s[L-1]
    while g(L, s)<n:
        s.append(g(L, s))
        L += 1
    print(sum(G if G<n else 0 for G in s))
