
def pangram(string):
    for char in string:
        if string.count(char) > 1 or len(string) > 26:
            break
    else:
        return("The string is pangram")
    return "The string isn't pangram"

def palindrom(string):
    string = "".join(string.lower().split())
    return True if string == string[::-1] else False

def reverse(str1):
    lst = str1.split()
    return " ".join([word[::-1] for word in lst])

item = []

def stack(func):
    def st(*args):
        print(func.__name__)
        func(*args)
    return st

@stack 
def push(it):
    item.append(it)

@stack
def pop(it):
    item.pop(it)

@stack
def peek():
    print(item[-1])

@stack
def top():
    print(item[0])

@stack
def is_empty():
    if len(item) == 0:
        print("Is empty")
    else:
        print("Isn't empty")

@stack
def clear():
    global item
    item = []
    print(item)

@stack 
def show():
    for x in item:
        print(x, end = ' ')
    
def seven(word):
    a = word
    for i in range(len(word)):
        word = a[:i] + a[i].upper() + a[i + 1:]
        print(word)

def five(string, substring):
    lst = []
    while substring in string:
        lst.append(string.index(substring))
        string = string[string.index(substring) + len(substring):]
    return lst
    if substring not in string:
        return []

def bubble_sort_opt(lst):
    n = len(lst) - 1
    swapped = False
    for i in range(n):
        for j in range(n - i):
            if lst[j] > lst[j + 1]:
                swapped = True        
                lst[j], lst[j + 1] = lst[j + 1], lst[j]     
        if not swapped: break
    return lst

items = []

def stack(func):
    def st(*args):
        print(func.__name__)
        func(*args)
    return st

@stack                    
def push(it):             
    items.append(it)

def bubble_sort_opt(lst):
    n = len(lst) - 1
    swapped = False
    for i in range(n):
        for j in range(n - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped: break
    return lst
# print(bubble_sort_opt([1,3,6,4,7,2,8,1,9,3]))

items = []
def stack(func):
    def st(*args):
        print(func.__name__)
        func(*args)
    return st

@stack
def push(it):
    items.append(it)

def func(): 
    x= 4
    action = (lambda n: x ** n) 
    return action
# file = open("sevagir.txt", "r").read().split()
# print(len(file))


A = [ [2, 1, 3], [3, 1, 5] ]  
B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


"""Sudoku"""
sudoku = [
    [7,	2,	6,	4,	9,	3,	8,	1,	5],
    [3,	1,	5,	7,	2,	8,	9,	4,	6],
    [4,	8,	9,	6,	5,	1,	2,	3,	7],

    [8,	5,	2,	1,	4,	7,	6,	9,	3],
    [6,	7,	3,	9,	8,	5,	1,	2,	4],
    [9,	4,	1,	3,	6,	2,	7,	5,	8],

    [1,	9,	4,	8,	3,	6,	5,	7,	2],
    [5,	6,	7,	2,	1,	4,	3,	8,	9],
    [2,	3,	8,	5,	7,	9,	4,	6,	1]
]

a = [[A[j][i] for j in range(len(A))] for i in range(len(A[0])) ]
# def valid_rows(sudoku):
#     breaked = False
#     for row in sudoku:
#         for ele in row:
#             if row.count(ele) != 1:
#                 breaked = True
#                 break
#     return True if not breaked else False  
# def valid_columns(sudoku):
#     breaked = False
#     for i in range(10):
#         col = [row[i] for row in sudoku]
#         for ele in col:
#             if col.count(ele) != 1:
#                 breaked = True
#                 break
#     if not breaked:
#         return True if not breaked else False
# def valid_box(sudoku):
#     subs = [range(3), range(3,6), range(6,9)]
#     boxes = []
#     for i in subs:
#         for j in subs:
#             boxes.append()

sudoku = [
    [7,	2,	6,	4,	9,	3,	8,	1,	5],
    [3,	1,	5,	7,	2,	8,	9,	4,	6],
    [4,	8,	9,	6,	5,	1,	2,	3,	7],

    [8,	5,	2,	1,	4,	7,	6,	9,	3],
    [6,	7,	3,	9,	8,	5,	1,	2,	4],
    [9,	4,	1,	3,	6,	2,	7,	5,	8],

    [1,	9,	4,	8,	3,	6,	5,	7,	2],
    [5,	6,	7,	2,	1,	4,	3,	8,	9],
    [2,	3,	8,	5,	7,	9,	4,	6,	1]
]

ls = [1, 2, 3, 4]
x = iter(ls)


tp = (1, 3, "hello", {1: "you", 2: "they"})


text = b'I am a string'.decode()
text1 = "hello".encode()
# print(text1)
# print(type(text1))

ls = [[None]*2]*3
ls[1][1] = 8

d = {'a':'a', "b":'b'}
d.setdefault('c',"c")
# print(d)

from collections import Counter


x = "h h h dd kk ddd kkf fll dd"

c =Counter(x)
# print(c)



# i = 10
# (i(5%2))

with open('data.bin', 'wb') as f: 
    f.write(b'\xf1\xf2\xf3\xf4\xf5')
with open('data.bin', 'rb') as f: data = f.read()
assert data == b'\xf1\xf2\xf3\xf4\xf5'

x = bytearray(5)

name = "Max"
name2 = "Ann"
formatted = '{0} loves food. See {1} cook.'.format(name, name2) 
print(([i * 2 for i in range(10, 5)]))
print(list(range(10, 5, -1)))


