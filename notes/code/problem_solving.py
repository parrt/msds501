# Sum digits in string

s = "501"
n = 0
for d in s:
    n += int(d)
print(n)


# Reverse list

A = [1, 9, 2, 4]
"""
example swap (this is a common pattern also):
t = A[3]
A[3] = A[0]
A[0] = t

OR,

A[0],A[3] = A[3],A[0] # but this requires creation of a 2-element tuple/list.
"""
print(A)
n = len(A)
for i in range(n//2): # 0..n/2-1 (stop halfway!)
    t = A[n-i-1]
    A[n-i-1] = A[i]
    A[i] = t

print(A)
