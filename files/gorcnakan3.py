"1"
tiv = int(input("enter the number: "))
a = 0
lst = []
while tiv != 0:
    a = tiv % 10
    lst.append(a)
    tiv = tiv // 10
num = [str(i) for i in lst]
nums = "".join(num)
print(int(nums))

"2"
tuple = (1, 2, 3)
num = "".join(str(i) for i in tuple)
print(num)

"3"
lst = [1, 5, 99, 3, -1]
max = lst[0]
min = lst[0]
for i in lst:
    if i > max:
        max = i
    elif i < min:
        min = i

        
sum = max + min
print(sum)

"4"
lst = [1, 0, 5, 6, 8, 4, 9]

for i in range(0, len(lst)-1):
    if lst[i] % 2 == 0:
        print(i)
    
"5"
word  = input("enter the word: ")
i = len(word)
# while i > 0:
#     i -= 1
#     print (word[i], end="")

for i in range(len(word)-1, -1, -1):
    print (word[i] , end="")

"6"
def bajanarar(a):
    return [i for i in range(1, a) if a % i == 0]
#print(bajanarar(6))
def is_prime(a):
    if bajanarar(a) == [1]:
        return True

n = int(input("enter a number: "))

def smallest_prime(n):
    a = n + 1
    while not is_prime(a):
        a += 1
    return a
print(smallest_prime(n))

"7"

data = []
ele = (input("enter a number: "))
while ele != "":
    data.append(ele)
    ele = (input("enter a number: "))
data = [int(x) for x in data]

def get_median(data):
    if len(data) % 2 == 0:
        return (data[len(data)//2] + data[(len(data)//2 - 1)]) / 2
    else:
        return data[len(data)//2]
print (get_median(data))