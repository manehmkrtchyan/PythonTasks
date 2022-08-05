'1'
string = 'hello'
n = int(input("Enter the amount of moves: "))
ending = ''
for i in string[len(string) - n::]:
    ending += i
print(ending)
start = ''
for j in string[:len(string) - n:]:
    start += j
print(start)
answer = ending + start
print(answer)

'2'
multiples = []
sum = 0
for num in range(1, 1001):
    if num % 3 == 0 or num % 5 == 0:
        multiples.append(num)
        sum += num
print(multiples)
print(f"The sum of multiples is {sum}")

'3'
def fib(n):
    a = 0
    b = 1
    while n!= 0:
        a, b = a + b, a
        n -= 1
    return b

num = 0
sum = 0
while fib(num) < 4000000:
    if fib(num) % 2 == 0:
        sum += fib(num)
    num += 1
print(sum)