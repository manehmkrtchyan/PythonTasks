"1.3"
def ex_1_3(a,b,c):
    if a<b and a<c:
        return b**2 + c**2
    elif b<a and b<c:
        return a**2 + b**2
print (ex_1_3(2, 5, 4))

"1.5"
def sum(a, b):
    sum = 0
    while a < b:
        sum+=a
        a+=1
    return sum

print (sum(3, 6))

"1.7"
"some new changes"
"some other changes"




"1.8"
def cube_root(n):
    root = 1
    while not guess_enough(root, n):
        root = improved(root, n)
    return root

def abs(n):
    return n if n>0 else -n

def guess_enough(root, target):
    if abs(root**3-target)<0.000001:
        return True
    else:
        return False

def improved(root, target):
    return ((target/(root**2))+(2*root))/3

print (cube_root(27))