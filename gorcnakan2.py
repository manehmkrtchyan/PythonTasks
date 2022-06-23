"1"
lst = []
ele = input("Enter the words  ")

while ele != '':
    lst.append(ele)
    ele = input("Enter the words  ")
    if ele in lst:
        lst.remove(ele)
print(lst)

"2"
tiv = int(input("enter a number: "))
def bajanarar(tiv):
    return [i for i in range(1, tiv) if tiv % i == 0]
print(bajanarar(tiv))

"3"
n = int(input("enter a number: "))
def kataryal(n):
    return sum([i for i in range (1, n) if n % i == 0]) == n
print(kataryal(n))

"4"
sent = input("enter the sentence: ")
sent = sent.lower()
sent = sent.split(", ")
if sent == sent[::-1]:
    print("the sentence is palindrome")
else:
    print("the sentence is not palindrome")
print(sent)

"5"
lst = []
ele = input("enter a number: ")
while ele != "":
    lst.append(ele)
    ele = input("enter a number: ")
lst = [int(x) for x in lst]

mean = sum(lst) / len(lst)
print (mean)
less_than_mean = []
for ele in lst:
    if ele <= mean:
        less_than_mean.append(ele)
print(less_than_mean)
more_than_mean = []
for ele in lst:
    if ele > mean:
        more_than_mean.append(ele)
print(more_than_mean)  