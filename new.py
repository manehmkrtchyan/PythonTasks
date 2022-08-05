'1'
input_file = open('numbers.txt', 'r')
input_text = input_file.read()
nums = input_text.split()
sum = 0
for num in nums:
    sum += int(num)
print(sum)

'2'
input_file = open('text.txt', 'r')
input_text = input_file.read()
titled_text = input_text.title()
new_file = open('numbers.txt', 'w')
new_file.write(titled_text)

'3'
lst = [1, 2, 3, 4, 2, 5, 4, 4, 1, 3, 6, 1]
dict = {}
keys = dict.keys()
for ele in lst:
    if ele in keys:
        dict[ele] += 1
    else: dict.update({ele: 1})
print(dict)

'4'
input_file = open('text.txt', 'r')
input_text = input_file.read()
print(len(input_text))

'5'
string = list('976707420402504845181893511000')
del string[2::3]
''.join(string)
empty = ''
for i in string:
    empty += i
print(empty)

'6'
input_file = open('text.txt', 'r')
input_text = input_file.read()
words = input_text.split()
dict = {}
keys = dict.keys()
for word in words:
    if word in keys:
        dict[word] += 1
    else: dict.update({word: 1})
print(dict)

'7'
lst = [4, 5, 3, 1, 2]
squares = []
for num in lst:
    squares.append(num**2)
sorted = sorted(squares)
print(sorted)

'8'
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(sum)

'9'
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

'10'
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(start, end + 1):
    if i % 2 == 1:
        print(i, end = ' ')