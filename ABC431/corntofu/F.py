import sys, copy
input = sys.stdin.readline

mod = 998244353
fact = [1]
pfs = [0 for _ in range(1000001)]
n, d = map(int, input().split())
for i in list(map(int, input().split())):
    pfs[i] += 1
for i in range(1, 1000001):
    pfs[i] += pfs[i - 1]
for i in range(1, 1000001):
    fact.append(fact[-1] * i % mod)
ans = 1
for i in range(1, 1000001):
    a = pfs[min(i + d, 1000000)] - pfs[i - 1] 
    b = pfs[i] - pfs[i - 1]
    ans = ans * fact[a] * pow(fact[b] * fact[a - b], mod - 2, mod) % mod

print(ans)
