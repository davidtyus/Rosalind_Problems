#!/usr/bin/env python3

def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    list1 = list(map(int, lines[2].split()[0:]))  
    list2 = list(map(int, lines[3].split()[0:]))  # Skipping 1st and 2nd lines (which have lengths)

    return list1, list2


def binary_search(list_a, to_find, low=0, high=None):
    if high is None:
        high = len(list_a) -1
    
    if low > high:
        return -1  
    
    half = (high + low) // 2
    guess= list_a[half]

    if list_a[half] == to_find: 
        return half +1 #Rosalind system is 1-based so add 1 
    elif guess < to_find: 
        return binary_search(list_a, to_find,half+1, high)
    else:
        return binary_search(list_a,to_find,low, half - 1)
    

file = "rosalind_bins.txt"
a,b = read_lists_from_file(file)

ans = []
for each in b: 
    ind=binary_search(a,each) 
    ans.append(str(ind))


print(" ".join(ans)) 