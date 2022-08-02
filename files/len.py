word = input("enter the word: ")
def length(word):
    i = 0
    for s in word:
        i += 1
    return i
print(length(word))