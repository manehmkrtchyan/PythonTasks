"bubble sort"
def bubble_sort(lst):
    n = len(lst) - 1
    swapped = False
    for i in range(n):
        for j in range(n - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            break
    return(lst)   

print(bubble_sort([5, 2, 4, 8, 3, 0])) 

"selection sort"
def selection_sort(lst):
    n = len(lst) 
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

print(selection_sort([9, 15, 0, 5, 5, 4, 7, 2, 1]))    

"insertion sort"
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst
print(insertion_sort([4,8,3,7,8,4,0]))

"merge sort"
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]=right[j]
            j += 1
            k += 1
    return lst

print(merge_sort([54,26,93,17,77,31,44,55,20]))