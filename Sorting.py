import numpy as np
import sys
import collections
import heapq
import argparse

def bubble_sort(s):
    for i in range(len(s)):
        swap = 0
        for j in range(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                swap = 1
        if not swap:
            break

    return s

def selection_sort(s):
    for i in range(len(s)-1):
        index = i
        for j in range(i+1, len(s)):
            if s[j] < s[index]:
                index = j
        s[i], s[index] = s[index], s[i]

    return s

def insertion_sort(s):
    for i in range(1, len(s)):
        tmp = s[i]
        j = i-1
        while j >= 0 and tmp < s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = tmp
    
    return s

def shell_sort(s):
    gap = len(s) // 2
    while gap >= 1:
        for i in range(gap, len(s)):
            tmp = s[i]
            j = i-gap
            while j >= gap and tmp < s[j]:
                s[j+gap] = s[j]
                j -= gap
            s[j+gap] =  tmp
        gap /= 2

    return s


def merge(a, b):
    result = []
    while a and b: 
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    if a: result.extend(a)
    if b: result.extend(b)

    return result 

def merge_sort(s):
    if len(s) < 2:
        return s 

    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    return merge(merge_sort(left), merge_sort(right))


def heapify(s, i):
    left = 2*i+1
    right = 2*i+2
    largest = i 
    if left < l and s[left] > s[largest]:
        largest = left
    if right < l and s[right] > s[largest]:
        largest = right 
    if largest != i: 
        s[i], s[largest] = s[largest], s[i]
        heapify(s, largest)

def build_maxheap(s):
    for i in range(l//2, -1, -1):
        heapify(s, i)

def heap_sort(s):
    global l
    l = len(s)
    build_maxheap(s)
    for i in range(len(s)-1, 0, -1):
        s[i], s[0] = s[0], s[i]
        l -= 1 
        heapify(s, 0)
    return s


def counting_sort(s):
    min_value = min(s)
    max_value = max(s)
    count = [0] * (max_value - min_value + 1)
    for i in s:
        count[i-min_value] += 1 
    
    result = []
    for i in range(len(count)):
        num = count[i]
        result.extend([i+min_value]*num)
    return result

def partition(s, l, r):
    pivot = s[l]
    index = l + 1
    for i in range(index, r+1):
        if s[i] < pivot:
            s[i], s[index] = s[index], s[i]
            index += 1
    s[l], s[index-1] = s[index-1], s[l]
    
    return index - 1


def quick_sort(s):
    def helper(arr, l, r):
        if l < r: 
            index = partition(s, l, r)
            helper(arr, l, index-1)
            helper(arr, index+1, r)
    
        return s
    
    ans = helper(s, 0, len(s)-1)
    
    return ans
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Select sort algorithm.')
    parser.add_argument('--method', default = "bubble_sort")
    args = parser.parse_args()

    algorithm = [bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort, heap_sort, counting_sort, quick_sort]

    d = {}
    for f in algorithm:
        d[f.__name__] = f

    s = [1,6,12,90,22,7,4,996,336]
    args.method = "quick_sort"
    s = d[args.method](s)
    print(s)
