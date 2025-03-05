#!/usr/bin/env python3


def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    list1 = list(map(int, lines[1].split()[0:]))  
    list2 = list(map(int, lines[3].split()[0:]))  # Skipping 2nd and fourth lines (which have lengths)

    return list1, list2



def merge_sorted_arrays(a,b): 
    
    i=0
    j=0
    merged=[]

    while i < len(a) and j<len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i+=1
            elif b[j] < a[i]:
                merged.append(b[j])
                j+=1
            else:
                merged.append(a[i])
                i+=1

    if j<len(b):
         merged.extend(b[j:len(b)])
    elif i<len(a):
         merged.extend(a[i:len(a)])

    
    return merged


file="rosalind_mer.txt"
lista, listb = read_lists_from_file(file)
ans=merge_sorted_arrays(lista,listb)

formatted=' '.join(map(str, ans))

print(formatted)

with open("sorted.txt", "w") as file:
  file.write(formatted)



