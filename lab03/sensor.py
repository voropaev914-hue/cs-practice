t = float(input())
n = int(input())
e = x = c = 0
s = 0.0
m = float('-inf')

for _ in range(n):
    l = input().strip()
    if l == "error":
        e += 1
    else:
        v = float(l)
        c += 1
        s += v
        if v > m:
            m = v
        if v > t:
            x += 1

print(n)
print(e)
print(x)
print(f"{m:.1f}")
print(f"{s/c:.1f}")