from os import remove


def contain(data, val):
    i=0
    while i<len(data):
        if data[i]==val:
            return True
        else:
            return False 


def pop(data, i):
    if i==None:
        data = data - data[len(data)-1]
    else:
        data = data - data[i]
        return data[i]

def remove_all(data, value):
    while i< len(data):
        if data[i] == value:
            remove(data[i])
            i+=1

def reverse(data):
    while i<len(data):
        

