#"ex.1.11"
def f_recursive(n):
    if n in (0, 1, 2):
        return n
    return f_recursive(n-1) + f_recursive(n-2) + f_recursive(n-3)

print(f_recursive(5))

def f_iterative(n):
    a=0
    b=1
    c=2
    if n==0:
        return a 
    if n==1:
        return b
    if n==2:
        return c
    while n>0:
        a, b, c = a+b, b+c, a 
        n-=1
    return c

print (f_iterative(5))


#"ex.1.12"
def pascal_triangle(m, n):
    if n==1:
        return 1
    elif m==n:
        return 1
    return pascal_triangle(m-1, n-1) + pascal_triangle(m-1, n)

print(pascal_triangle(3, 2))


#"ex.1.13"
def fast_pow_iterative(m, n):
    res=1
    count=0
    if n==0:
        return 1
    if n%2==0:
        while count<n/2:
            res*=m*m
            count+=1
        return res
    else:
        while count<n-1:
            res*=m
            count+=1
        return res*m

print (fast_pow_iterative(2, 7))

#ex.1.14
def double(n):
    return 2*n
def halve(n):
    return n/2

def fast_mul(a, b):
    if b==0:
        return 0
    if b%2==0:
        return double(fast_mul(a, halve(b)))
    else: 
        return a + fast_mul(a, b-1)
print (fast_mul(3, 5))        