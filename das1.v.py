lst = [1, 2, 3, 5, 8, 15, 49, 456]
def bin_search(lst, key):
    """This is the iterative algorithm"""
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if key == lst[mid]:
            return mid
        if key < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
print(bin_search(lst, 456))

lst = [1, 5, 9, 45, 78, 678]
key = 678
start = 0
end = len(lst)-1
def binary_search_rec(lst, start, end, key):
    """This is the recursive algorithm"""
    if end >= start:
        mid = (start + end) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search_rec(lst, start, mid - 1, key)
        else:
            return binary_search_rec(lst, mid + 1, end, key)
    else:
        return -1
#result = binary_search_rec(lst, 0, len(lst)-1, key)
print(binary_search_rec (lst, start, end, key))


"2"
lst = [5, 6, 7, 9, 8, 14, 36]
k = 0
for ele in lst[1::]:
    if ele % lst.index(ele) == 0:
        k += 1
print(k)


"3"
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(sum)

"4"
num = int(input("Enter a number: "))
def prod(num):
    prod = 1
    while num > 0:
        digit = num % 10
        prod *= digit
        num = num // 10
    return prod
def sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    return sum
def difference(num):
    return prod(num) - sum(num)
print(difference(num))

"5"
def fib_rec(n):
    if n in (0, 1):
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
print(fib_rec(3))