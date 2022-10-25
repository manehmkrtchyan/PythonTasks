def seven(word):
    a = word
    for i in range(len(word)):
        word = a[:i] + a[i].upper() + a[i + 1:]
        print(word)

def five(string, substring):
    lst = []
    while substring in string:
        lst.append(string.index(substring))
        string = string[string.index(substring) + len(substring):]
    return lst
    if substring not in string:
        return []
