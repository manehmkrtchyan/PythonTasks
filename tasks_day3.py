'1'
def square_of_sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum ** 2
def sum_of_squares():
    sum = 0
    for i in range(1, 101):
        sum += i ** 2
    return sum
print(square_of_sum() - sum_of_squares())

'2'
input_file = open('text.txt', 'r')
input_text = input_file.read()
titled_text = input_text.title()
new_file = open('numbers.txt', 'w')
new_file.write(titled_text)

'3'
number = int(input("Enter a number here: "))
def palindrome(num):
    old_num = num
    reversed = ''
    while num != 0:
        digit = num % 10
        reversed += str(digit)
        num = num // 10
    return str(old_num) == reversed
print(palindrome(number))