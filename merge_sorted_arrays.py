#!/usr/bin/env python3

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
                merged.append(b[j])
                
                i+=1
                j+=1

    if j<len(b):
         merged.extend(b[j:len(b)])
    elif i<len(a):
         merged.extend(a[i:len(a)])

    
    return merged

#print(merge_sorted_arrays([1,3,4,5,7],[2,4,8,9]))


