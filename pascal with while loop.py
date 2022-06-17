from math import factorial
def pascal(m, n):
    res=0
    i=0
    while i<m:
        j=0
        while j<=i:
            if i==m-1 and j==n-1:
                res = factorial(i)//(factorial(j)*factorial(i-j))
            j+=1
        i+=1
    return res
print (pascal(8, 4))
