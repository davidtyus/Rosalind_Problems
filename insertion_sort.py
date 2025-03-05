#!/usr/bin/env python3

def read_list_from_txt(filename):
    with open(filename, 'r') as file: 
        nums=list(map(int, file.read().split()))
    return nums[1:] #first number is just the length


#swap counter

def insertion_sort(a): 
    counter=0
    for i in range(1, len(a)):
        k=i
        while k>0 and a[k] < a[k-1]:
            a[k],a[k-1] = a[k-1],a[k]
            counter+=1
            k-=1
    return counter

file="rosalind_ins.txt"
num_list = read_list_from_txt(file)

print(insertion_sort(num_list))
