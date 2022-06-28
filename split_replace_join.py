# source = input("enter the string: ")
# sep = str(input("enter the separator: "))
# count = int(input("enter the index, where you want to stop splitting: "))
# lst = []
# def split(source, sep, count):
#     """This function returns the list of the words in the string usig sep as separator. 
#     count parameter is the index of the maximum number of the splits to do.  """
#     ele = ''
#     for i in source:
#         if source.index(i) != count:
#             if i == sep:
#                 lst.append(ele)
#                 ele = ''
#             else:
#                 ele += i
#         else:
#             break
#     if ele != sep:
#         lst.append(ele)
#     print(lst)
# split(source, sep, count)


source = input("enter the text: ")
old = input("enter the substring you want to change: ")
new = input("enter the new string: ")
count = int(input("enter the index where you want to stop replacing: "))
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


