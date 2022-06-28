source = input("enter the string: ")
sep = str(input("enter the separator: "))
count = int(input("enter the index, where you want to stop splitting: "))
lst = []
def split(source, sep, count):
    ele = ''
    for i in source:
        if source.index(i) != count:
            if i == sep:
                lst.append(ele)
                ele = ''
            else:
                ele += i
        else:
            break
    if ele != sep:
        lst.append(ele)
    print(lst)
split(source, sep, count)

