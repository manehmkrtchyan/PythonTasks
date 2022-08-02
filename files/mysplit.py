text = '127. 7. 45, 55'
lst = []
def mysplit(a):
    ele = ''
    for i in text:
        if i != ",":
            if i == a:
                lst.append(ele)
                ele = ''
            else:
                ele += i
        else:
            break
    if ele != a:
        lst.append(ele)
    print(lst)
mysplit(".") 

