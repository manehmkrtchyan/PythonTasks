"1"
def info(name, adress):
    print(f"my name is {name} and my adress is {adress}")

name = input("input your name ")
adress = input("input your adress ")
info(name, adress)

"2"
name = input("Enter your name here ")
def hello(name):
    print(f"Hello dear {name}!")
hello(name)
 
"3"
def area(a, b):
    return f"res {a*b}"

num1 = float(input("enter a "))
num2 = float(input("enter b "))

print(area(num1, num2))

"4"
def area_hoxamas(a, b):
    return f"area is {a**b/43560}"

num1 = float(input("enter a "))
num2 = float(input("enter b "))

print(area_hoxamas(num1, num2))

"5"

def price(m, n):
    return f"{m*0.10+n*0.25} $"

m = float(input("enter the quantity of low quality bottles "))
n = float(input("enter the quantity of high quality bottles "))
print(price(m, n))

"6"
price:float = float(input("enter the price of the order "))
def teyavchar():
    teyavchar = price*18/100
    return f"{float(teyavchar):.2f}"
def harker():
    harker:float = price*20/100
    return harker
print(f"The price is {price} , the teyavchar is {teyavchar()}, the hark is {harker()}!")

"7"
def sum_from_1_to_tiv(tiv):
    sum = 0
    i = 1
    while 1 < tiv:
        sum += tiv
        tiv -= 1
    return sum
tiv = int(input("enter the number"))
print(sum_from_1_to_tiv(tiv))

"8"
quantity1 = int(input("Nermuceq manruqneri qanaky: "))
quantity2 = int(input("Nermuceq hushanverneri qanaky: "))
def yndhanur_qash(quantity1, quantity2):
    return 75*quantity1 + 112*quantity2

print(f"Dzer gnumneri yndhanur qashy kazmum e {yndhanur_qash(quantity1, quantity1)} gram.")

"9"
gumar = int(input("Enter the intitial summ of your money: "))
def tari_1_2_3(gumar):
    i = 0
    while i < 3:
        gumar = gumar + gumar*4/100
        print (gumar)
        i += 1
tari_1_2_3(gumar)

"10"
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
def sum(a, b):
    return a+b
def dif(a, b):
    return a-b
def div(a, b):
    return a/b
def div_whole(a, b):
    return a//b
def div_fractional(a, b):
    return a%b 
def log(a):
    import math 
    return math.log10(a)
print (f"the sum is {sum(a, b)}, \nthe difference is {dif(a, b)}, \
\nthe division is {div(a, b)}. \nthe whole part of division is {div_whole(a, b)} \
\nthe fractional part of division {div_fractional(a, b)}, \
\nthe base 10 log of the first number is {log(a)}." )

"11"
mpg = int(input(f"Input MPG: "))
def convert(mpg): 
    l_100km = 378.5 / (mpg * 1.609)
    return l_100km
print(convert(mpg))

"12"
foot = int(input(f"enter foots: "))
inch = int(input(f"enter inches: "))
def height_in_sm(foot, inch):
    return foot * 12 * 2.54 + inch * 2.54
print(f"Your height is {height_in_sm(foot, inch)} sm")

"13"
foot = int(input("enter foot")) 
def feet_convert(foot):
    print(f"Foot to inches = {12 * foot}") 
    print(f"Foot to yards = {1/3 * foot}")
    print(f"Foot to miles = {1/5280 * foot}")
feet_convert(foot)

"14"
from cmath import pi
r = int(input(f"enter the radius of the circle: "))
def area(r):
    import math
    print (f"The area of the circle is {pi * r ** 2}")
def volume(r):
    import math
    print (f"The volume of the ball is {4 / 3 * pi * r ** 3}")
area(r)
volume(r)    

"15"
height = float(input(f"enter the height: "))
r = float(input(f"enter the radius: "))
from cmath import pi
def volume(height, r):
   return height * pi * r ** 2 
print(f"{volume(height, r):.1f}")

"16"
d = float(input("Enter the height: "))
a = 9.8
v = 0
def speed(d):
    from math import sqrt
    return sqrt(v ** 2 + 2 * a * d)
print(speed(d))

"17"
h = int(input("enter the height: "))
b = int(input("enter the base: "))
def area(h, b): 
    return b * h / 2
print(area(h,b))

"18"
s1 = int(input("enter the first side of the triangle: "))
s2 = int(input("enter the second side of the triangle: "))
s3 = int(input("enter the third side of the triangle: "))
def area_kisaparagic(s1, s2, s3):
    import math
    s = float((s1 + s2 + s3) / 2)
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
print(area_kisaparagic(s1, s2, s3))

"19"
d = int(input("enter the days: "))
h = int(input("enter the hours: "))
m = int(input("enter the minutes: "))
s = int(input("enter the seconds: "))
def to_sec(d, h, m, s):
    return s + m * 60 + h * 3600 + d * 24 * 3600
print(to_sec(d, h, m, s))

"20"
import time
t = time.localtime()
print(time.asctime(t))

"21"
import time
month = int(input("Enter the month number here: "))
def days(month):
    list = [1, 3, 5, 7, 8, 10, 12]
    if month in list:
        return 31
    elif month == 2:
        return 28 or 29
    return 30
print(days(month))

"22"
letter = input("enter a letter here: ")
def letter_type(letter):
    list = ["a", "e", "i", "o", "u"]
    if letter in list:
        print("Tary dzaynavor e")
    elif letter == "y":
        print("Tary karogh e linel e'v dzaynavor, e'v baghadzayn")
    else: print("Tary baghadzayn e")
letter_type(letter)

"23"
dzmer = ["dektember", "hunvar", "petrvar"]
garun = ["mart", "april", "mayis"]
amar = ["hunis", "hulis", "ogostos"]
ashun = ["september", "hoktember", "noyember"]
amis = input("greq amsva anuny: ")
day = int(input("greq amsva ory: "))
def tarva_exanak(amis):
    if amis in dzmer:
        print("dzmer")
    elif amis in garun:
        print("garun")
    elif amis in amar:
        print("amar")
    else:
        print("ashun")
tarva_exanak(amis)
    
"25"
def celsius():
    i = 0
    while i < 100:
        print (f"{i} - {i * 33.8}")
        i += 10
celsius() 

"26"
def fizzbuzz():
    n = 1
    while n < 100:
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbazz")
            n+=1
        elif n % 3 == 0:
            print("fizz")
            n += 1
        elif n % 5 == 0:
            print("bazz")
            n+=1
        
        else:
            n += 1
fizzbuzz()

"28"
from operator import truediv
tiv = int(input("enter a number"))
def chisht_bajanarar(tiv):
    i = 1
    list = []
    while i < tiv:
        if tiv % i == 0:
            list.append(i)
            i += 1
        else: 
            i += 1
    return list
print(list(chisht_bajanarar(tiv)) )