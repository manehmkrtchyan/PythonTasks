'1'
n = int(input("Enter the the length of the list: "))

self = []
for i in range(1, n + 1):
    self.append(i)

target  = []
ele = input("Enter the target list: ")
while ele != "":
    target.append(ele)
    ele = input("Enter the target list: ")
target = [int(ele) for ele in target]

def build(self, target):
    output=[]
    for i in self:
        if i in target:
            output.append("Push")
        elif(i<=max(target)):
            output.append("Push")
            output.append("Pop")
        else:
            break
    return output
print(build(self, target))

'2'
nums1 = []
ele1 = input("Enter the nums1 list: ")
while ele1 != "":
    nums1.append(ele1)
    ele1 = input("Enter the nums1 list: ")
nums1 = [int(ele1) for ele1 in nums1]

nums2 = []
ele2 = input("Enter the nums2 list: ")
while ele2 != "":
    nums2.append(ele2)
    ele2 = input("Enter the nums2 list: ")
nums2 = [int(ele2) for ele2 in nums2]

max = max(max(nums1), max(nums2))
intersection = []
for i in range(1, max + 1):
    if i in nums1 and i in nums2:
        intersection.append(i)

print(set(intersection))

'3'
lst = []
num = input("Enter a number: ")
while num != "":
    lst.append(num)
    num = input("Enter a number: ")
lst = [int(num) for num in lst]

from statistics import mode
def degree(lst):
    return(lst.count(mode(lst)))

sublists = []
for i in range(len(lst) + 1):
    for j in range(i + 1, len(lst) + 1):
        sublists.append(lst[i:j])
print(sublists)

same_degrees = []
for sublist in sublists:
    if degree(sublist) == degree(lst):
        same_degrees.append(sublist)
print(same_degrees)

smallest = same_degrees[0]
for each in same_degrees:
    if len(each) < len(smallest):
        smallest = each
print(smallest)

'4'
given_list = []
num = input("Enter a number: ")
while num != "":
    given_list.append(num)
    num = input("Enter a number: ")
given_list = [int(num) for num in given_list]

l = 0
r = 0
for i in range(len(given_list)):
    if given_list[i] % 2 == 0:
        given_list[l], given_list[r] = given_list[i], given_list[l]
        l += 1
    r += 1
print(given_list)

'5'
given_list = []
num = input("Enter a number: ")
while num != "":
    given_list.append(num)
    num = input("Enter a number: ")
given_list = [int(num) for num in given_list]

unique_list = []
for num in given_list:
    if given_list.count(num) == 1:
        unique_list.append(num)
sum = 0
for i in unique_list:
    sum += i
print(sum)

'6'
def needle_in_heystack(needle, haystack):
    if needle in haystack:
        return(haystack.index(needle)) 
    else:
        return(-1)
print(needle_in_heystack('ll', 'hello'))

'7'
s = input("Enter the string here: ")
splitted = s.split()
print(len(splitted[-1]))

'8'
def is_palindrome(s):
    s = s.lower()
    s = ''.join(i for i in s if i.isalpha())
    if s == s[::-1]:
        return True
    return False
print(is_palindrome('A man, a plan, a canal: Panama'))



'9'
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
lst = []
def uniq(emails):
    for email in emails:
        local_name = email[:email.index('@')]
        domain = email[email.index('@'):]
        local_name = local_name.replace(".", "")
        local_name = local_name[:local_name.index('+')] if '+' in local_name else local_name
        new = (local_name + domain) 
        lst.append(new)
    print(len(set(lst)))

uniq(emails)


'10'
lst = [1, 3, 3, 3, 5, 5, 5, 7, 8]
target = 3

def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end:
        mid = (start + end) // 2
        if target == lst[mid]:
            return mid
        if target < lst[mid]:
            end = mid - 1
        else: 
            start = mid + 1
    return -1
idx = binary_search(lst, target)

i = 1
was_left = 0
while lst[idx - i] == lst[idx]:
    i += 1
    was_left = 1

if was_left == 1:
    print(idx - i)
else:
    print(idx)
