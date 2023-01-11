class Number():
    def __init__(self, value):
        self.value = value
        def str_to_list(str):
            lst = []
            i = 0
            j = i + 3
            while str != '':
                lst.append(int(str[i:j]))
                str = str[j:]
            return lst
        self.lst = str_to_list(self.value)

    def __add__(self, gumareli):
        lst1 = self.lst
        lst2 = gumareli.lst
        i = len(lst1)
        j = len(lst2)
        if i < j:
            k = j - i
            while k != 0:
                lst1.insert(0, 0)
                k -= 1
        if i > j:
            k = i - j
            while k != 0:
                lst2.insert(0, 0)
                k -= 1
        new_list = [None] * len(lst1)
        for i in range(0, len(lst1)):
            new_list[i] = lst1[i] + lst2[i]
        for j in range(len(new_list) - 1, -1, -1):
            if new_list[j] > 999:
                new_list[j] = str(new_list[j])
                if j != 0:
                    new_list[j], new_list[j - 1] = new_list[j][1::], new_list[j - 1] + 1
                else:
                    new_list[j] = new_list[j][1::]
                    new_list.insert(0, '1')
        return new_list

    def __sub__(self, haneli):
        
        














num1 = Number('11111113333333')
num2 = Number('5555555550000000')
sum = num1 + num2
sub = num2 - num1
print(f'Sum is {sum} and substance is {sub} .')
a = 11111113333333
b = 5555555550000000
print(a - b)