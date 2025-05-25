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
# https://codesignal.com/learn/course/93/unit/3/practice/2

def evaluatePath(numbers):
    # TODO: implement the function
    n = len(numbers)
    position = 0
    moves = 0
    reversed_direction = False
    
    while True:
        step = numbers[position]
        
        if step == 0:
            return (position, moves)
        
        next_pos = position + step if not reversed_direction else position - step
        
        if 0 <= next_pos < n:
            position = next_pos
            moves +=1
        else:
            if not reversed_direction:
                reversed_direction = True
            else:
                return (position, moves)

numbers = [3, 4, 1, 1, -3, 1]
print(evaluatePath(numbers))
# (4, 5)

