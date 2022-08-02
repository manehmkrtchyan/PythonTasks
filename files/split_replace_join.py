source = input("enter the string: ")
sep = str(input("enter the separator: "))
index = int(input("enter the index where you want to stop splitting: "))
lst = []
def split(source, sep, index):
    """This function returns the list of the words in the string usig sep as separator. 
    index parameter is the index of the maximum number of the splits to do.  """
    
    ele = ''
    for i in source:
        if source.index(i) != index:
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
    #ARMAN JAN ESTEX COUNTY CHSTACVEC ANEL, PAHANJY MIQICH POXEL EM, 
    #COUNTI POXAREN INDEX OV EM AREL, VOR ED INDEXY UNECOX TARIC AJ SPLIT CHANI
split(source, sep, index)


source = input("enter the text: ")
old = input("enter the substring you want to change: ")
new = input("enter the new string: ")
count = int(input("enter the number of the wods you want to change: "))
def replace(source, old, new, count):
    result = ''
    lst = source.split(" ")
    n = 0
    for i in lst:
        if n <= count:
            if i == old:
                i = new
            n += 1
        result += i + " "
    return result
print(replace(source, old, new, count))




data = []
ele = input("Enter the words  ")
while ele != '':
    data.append(ele)
    ele = input("Enter the words  ")
sep = input("enter the separator")
def join(data, sep):
    res = ""
    for i in data:
        a = i + sep
        res += a
    return res
print(join(data, sep))
