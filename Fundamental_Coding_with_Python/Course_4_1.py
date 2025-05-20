# Reference
# https://codesignal.com/learn/course/93/unit/1

def solution(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            if i < j:
                result.append((i,j))
    print(result)
    return result

list1 = [1, 3, 7]
list2 = [2, 8, 9]
solution(list1, list2)
# [(1, 2), (1, 8), (1, 9), (3, 8), (3, 9), (7, 8), (7, 9)]


# Quiz 1
# https://codesignal.com/learn/course/93/unit/1/practice/1
def common_elements(listA, listB):
    # TODO: Implement the function to find the common elements in the two arrays
    result = []
    for a in listA:
        for b in listB:
            if a == b:
                result.append(a)
    print(result)
    return result

listA = [1, 2, 3]
listB = [2, 3, 4, 1]
common_elements(listA, listB)
# [1, 2, 3]


# Quiz 2
# https://codesignal.com/learn/course/93/unit/1/practice/2

def stringSearch(sourceArray, searchArray):
    # TODO: implement
    result = []
    
    for sid, sstr in sourceArray:
        for tid, tstr in searchArray:
            if sid <= tid and sstr in tstr:
                result.append((sid, sstr))
                break  # 한 번 매칭되면 다음 source로 넘어감
    print(result)
    return result

sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
searchArray = [(4, 'abcdefghi'), (5, 'defghiabc')]
stringSearch(sourceArray, searchArray)
# [(1, 'abc'), (2, 'def'), (3, 'ghi')]

# [(1, 'abc'), (1, 'abc'), (2, 'def'), (2, 'def'), (3, 'ghi'), (3, 'ghi')]
# [(1, 'abc'), (1, 'abc'), (2, 'def'), (2, 'def'), (3, 'ghi'), (3, 'ghi')]


# Quiz 3
# https://codesignal.com/learn/course/93/unit/1/practice/3

def solution3(listA, listB):
    # TODO: Find the pairs of integers a, b where a belongs to listA and b belongs to listB such that a is greater than 
    
    result = []
    for a in listA:
        for b in listB:
            if a > b and (a,b) not in result:
                result.append((a,b))
    print(result)
    return result

listA = [500, 200, -400, -700]
listB = [200, -300, 400, -500, 700]

solution3(listA, listB)
# [(500, 200), (500, -300), (500, 400), (500, -500), (200, -300), (200, -500), (-400, -500)]


import math
# Quiz 4
# https://codesignal.com/learn/course/93/unit/1/practice/4
def solution4(arr1, arr2):
    # TODO: Implement this function
    result = []
    
    for a in arr1:
        for b in arr2:
            total = a + b
            if total >= 0:
                sqrt_val = math.isqrt(total)
                if sqrt_val * sqrt_val == total:
                    result.append((a, b))
    print(result)                
    return result

arr1= [0, 1, 2, -100, 100]
arr2= [-100, 100, 30, 0, -1, -2, -3]
solution4(arr1, arr2)
# [(0, 100), (0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (-100, 100), (100, -100), (100, 0)]       

