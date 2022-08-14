'1'
lst = [1, 1, 3, 4, 4, 4, 5, 5, 7, 8, 9]
def remove_duplicates(lst):
    i = 1
    k = 1
    for j in range(1, len(lst)):
        if lst[j] != lst[j - 1]:
            k += 1
            lst[i] = lst[j]
            i += 1
    for r in range(k, len(lst)):
        lst.insert(r, '_')
        del lst[r + 1]
    print(k)        
    return lst
print(remove_duplicates(lst))

'2'
nums1 = [2, 4, 4, 6, 8, 8, 12]
nums2 = [1, 1, 3, 5, 7, 7, 7, 9]
def merge(lst1, lst2):
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst1):
        res.append(lst2[j])
        j += 1
    return res
print(merge(nums1, nums2))

'3'
nums1 = [1, 2, 3, 4, 1]
nums2 = [1, 2, 3, 4]
def is_unique(lst):
    return True if lst == list(set(lst)) else False
print(is_unique(nums1))
print(is_unique(nums2))

'4'
from itertools import count
lst = [1, 2, 4, 2, 1]
def find_the_unique(lst):
    for i in lst:
        if lst.count(i) == 1:
            return i
print(find_the_unique(lst))

'5'
lst = [0, 1, 2, 3, 4, 5, 7, 8, 9]
def find_n(lst):
    n = len(lst)
    return n
def missing(n, lst):
    nums = []
    for i in range(n):
        nums.append(i)
    return set(nums) - set(lst)
print(missing(find_n(lst), lst))

'6'
given_list = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]
sublists = []
for i in range(len(given_list) + 1):
    for j in range(i + 1, len(given_list) + 1):
        sublists.append(given_list[i:j])
with1 = []
for sublist in sublists:
    if not 0 in sublist:
        with1.append(sublist)
max = with1[0]
for ele in with1:
    if len(ele) > len(max):
        max = ele
print(max)

'7'
nums = [6,2,6,5,1,2]
nums.sort()
sum = 0
for i in nums[::2]:
    sum += i
print (sum)

'8'
def prime_factors(n):
    def is_prime(number):   
        d = 2
        while d*d <= number:
            while (number % d) == 0:            
                number //= d
            d += 1
        if number > 1:       
            return True
        else:
            return False
    prod = 1
    factor = 2
    lst = []
    while prod <= n:
        if is_prime(factor) and n % factor == 0:
            prod *= factor
            lst.append(factor)
        factor += 1    
    return lst
print(prime_factors(600851475143))        


