# Reference
def solution(arrayA, arrayB):
    indexA = 0
    indexB = None
    in_arrayA = True
    max_value = float('-inf')

    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            max_value = max(max_value,arrayB[indexB])
        else:
            if arrayB[indexB] == 0:
                print(max_value)
                return max_value
            else:
                indexA = arrayB[indexB]
        in_arrayA = not in_arrayA
    
arrayA = [2, 4, 3, 1, 6]
arrayB = [4, 0, 3, 2, 0]

solution(arrayA, arrayB)


# Quiz 1
# https://codesignal.com/learn/course/94/unit/1/practice/1

def solution1(arrayA, arrayB):
    # TODO: Implement the function
    visited_a = set()
    b_indices = []    
    index_a = 0
    
    while index_a not in visited_a:
        visited_a.add(index_a)
        index_b = arrayA[index_a] -1
        b_indices.append(index_b + 1 )
        index_a = arrayB[index_b] - 1
    print(b_indices)
    return b_indices

arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]

solution1(arrayA, arrayB)
#expected_output = [1, 4, 3, 2, 5]



# Quiz 2
# https://codesignal.com/learn/course/94/unit/1/practice/2

def solution2(arrayA, arrayB, arrayC):
    # TODO: implement
    # a -> b -> a-> c-> a
    pos = 0
    turn = 0   # 0: A→B, 1: B→A, 2: A→C, 3: C→A
    visitedB = set()
    visitedC = set()
    
    maxB = -1
    maxC = -1
    
    while True:
        if turn % 4 == 0: # a->b
            if pos >= len(arrayA): break
            next_index = arrayA[pos]
            if next_index >= len(arrayB): break
            if next_index in visitedB: break
            visitedB.add(next_index)
            maxB = max(maxB, arrayB[next_index])
            pos = next_index
        elif turn % 4 == 1: # b -> a
            if pos >= len(arrayA): break
            pos = arrayB[pos]
            if pos >= len(arrayA): break
        elif turn % 4 == 2: # a -> c
            if pos >= len(arrayA): break
            next_index = arrayA[pos]
            if next_index >= len(arrayC): break
            if next_index in visitedC: break
            visitedC.add(next_index)
            maxC = max(maxC, arrayC[next_index])
            pos = next_index
        elif turn % 4 == 3: # c -> a
            if pos >= len(arrayA): break
            pos = arrayC[pos]
            if pos >= len(arrayC): break
        turn += 1
        
    print(f"{maxB} + {maxC} = {maxB + maxC}")
    return maxB + maxC

arrayA = [2, 1, 3, 0]
arrayB = [1, 3, 2, 4]
arrayC = [4, 2, 5, 3]
solution2(arrayA, arrayB, arrayC)
# 7


# Quiz 3
# https://codesignal.com/learn/course/94/unit/1/practice/3

def solution3(roadA, roadB):
    # TODO: implement the function according to the description above
    result = []
    
    for start in range(len(roadA)):
        visitedA = set()
        visitedB = set()
        
        pos = start
        on_roadA = True
        step = 0
        
        while True:
            if on_roadA:
                if pos in visitedA:
                    break
                visitedA.add(pos)
                pos = roadA[pos]
            else:
                if pos in visitedB:
                    break
                visitedB.add(pos)
                pos = roadB[pos]
            step += 1
            on_roadA = not on_roadA
        result.append(step)
    print(result)
    return result


roadA, roadB = [1, 0, 2], [2, 0, 1]
solution3(roadA, roadB)
# [2, 4, 4]