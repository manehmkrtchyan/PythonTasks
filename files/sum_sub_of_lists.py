str1 = input("Enter the first number: ")
str2 = input("Enter the second number: ")

def str_to_list(str):
    lst = []
    i = 0
    j = i + 3
    while str != '':
        lst.append(int(str[i:j]))
        str = str[j:]
    return lst

def sum(lst1, lst2):
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

def sub(lst1, lst2):
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
    new_lst_2 = [-x for x in lst2]
    return sum(str_to_list(str1), new_lst_2)


