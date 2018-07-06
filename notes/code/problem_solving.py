# Sum digits in string

s = "501"
n = 0
for d in s:
    n += int(d)
print(n)


# String to int

s = "501"
a = [c for c in reversed(s)]
n = 0
i = 0
for d in a:
    n += 10**i * int(d)
    i += 1
print(f"'{s}' -> {n}")


n = 0
for i,d in enumerate(reversed(s)):
    n += 10**i * int(d)
print(f"'{s}' -> {n}")


n = 0
for d in s:
    n = 10*n + int(d)  # Horner's rule: "shift and add"
print(f"'{s}' -> {n}")


s = "1101"
n = 0
for d in s:
    n = 2*n + int(d)  # Horner's rule: "shift and add"
print(f"'{s}' -> {n}")


# Combine lists

a = [9, 3]
b = [1, 4, 10]
n = max(len(a),len(b))
c = []
for i in range(n):
    if i < len(a): c.append(a[i])
    if i < len(b): c.append(b[i])
print(c)


# Zip
a = [9, 3]
b = [1, 4, 10]
n = max(len(a),len(b))
c = []
for i in range(n):
    x = y = None
    if i < len(a): x = a[i]
    if i < len(b): y = b[i]
    c.append((x,y))
print(c)
