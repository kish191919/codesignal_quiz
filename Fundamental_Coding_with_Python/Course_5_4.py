# Reference
# 

def calculate_jumpA(forest, start, direction):

    step = 0

    while step < len(forest):
        step +=1
        i = start
        while i < len(forest):
            if forest[i] == 1:
                break
            i += step
            if i >= len(forest):
                print(step)
                return step
    return None
        


forest = [0, 1, 0, 0, 0, 0, 1, 1]
start = 0
direction = 1

calculate_jumpA(forest, start, direction)
# 4


def calculate_jumpB(forest, start, direction):

    jump = 1

    while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
        pos = start
        while 0 <= pos < len(forest):
            if forest[pos] == 1:
                break
            pos += jump * direction
        else:
            return jump

        jump += 1
    return -1

calculate_jumpB(forest, start, direction)
# 4

# Quiz 1
# https://codesignal.com/learn/course/94/unit/4/practice/1

def solution1(dungeon, health):
    # TODO: Implement the solution
    jump = 1
    result = {}
    initial_health = health

    while jump <= len(dungeon):
        pos = 0
        initial_health = health
        while pos < len(dungeon) and initial_health > 0:
            initial_health -= dungeon[pos]
            pos += jump
            # print("initial_health: ", initial_health)
            if initial_health <0:
                initial_health = -1
                break
        # print("health : ", initial_health, "jump: ", jump) 

        if initial_health != -1:
            result[jump] = initial_health
        jump +=1

    max_health = -1
    print(result)
    for step, health in result.items():
        if health > max_health:
            max_health = health
            max_jump = step
    print(max_jump)
    return max_jump

dungeon = [0, -1, 1, 0, -1]
health = 3
solution1(dungeon, health)
# 1


def solution1A(dungeon, health):
    # TODO: Implement the solution
    n = len(dungeon)
    best_x = -1
    min_loss = float('inf')

    for x in range(1, n + 1):
        pos = 0
        total_loss = 0
        alive = True

        while pos < n:
            loss = dungeon[pos]
            total_loss += loss
            if health - total_loss <= 0:
                alive = False
                break
            pos += x

        if alive:
            if total_loss < min_loss:
                min_loss = total_loss
                best_x = x

    return best_x if best_x != -1 else -1

print(solution1A(dungeon, health))

# Quiz 2
# https://codesignal.com/learn/course/94/unit/4/practice/2

def largest_step(garden, start, direction):
    length = len(garden)
    i = 0
    all_flowers = set(garden)
    max_step = -1
    
    if length == 1:
        return 1

    for step in range(1, length):
        result = set()
        
        if direction == 1:
            for idx in range(start, length, step):
                print(garden[idx])
                if garden[idx] not in result:
                    result.add(garden[idx])
            
            if sorted(result) == sorted(all_flowers):
                max_step = max(max_step, step)
        else:
            for idx in range(start, -1, step * direction):
                print(garden[idx])
                if garden[idx] not in result:
                    result.add(garden[idx])
            if sorted(result) == sorted(all_flowers):
                max_step = max(max_step, step)
    print(max_step)
    return max_step


print("2-1")
print(largest_step([1], 0, 1))
# 1


def largest_stepB(garden, start, direction):
    # TODO: implement the function
    n = len(set(garden))
    garden_lenght = len(garden)
    max_step = -1
    
    # 특별 케이스: 시작 지점 하나만으로 모든 꽃 종류를 커버하는 경우
    if len({garden[start]}) == n:
        return 1
    
    for step in range(1, garden_lenght):
        visited = set()
        pos = start
        
        while 0 <= pos < garden_lenght:
            visited.add(garden[pos])
            pos += step * direction
        if len(visited) == n:
            max_step = max(max_step, step)
    print(max_step)
    return max_step


print("2-2")
print(largest_stepB([1], 0, 1))
# 1

# array1 = [1,2,3,4,5]
# print(array1[-0:])
# print(array1[:-0])
# print(array1[0:])
# print(array1[:])
# print(array1[:0])
# print(array1[:-1])


# Quiz 3
# https://codesignal.com/learn/course/94/unit/4/practice/3
def solution3(array1, array2):
    # TODO: Your implementation goes here
    n = len(array1)
    min_distance = 1000
    # print("array1: ", array1)
    # print("array2: ", array2)
    
    for i in range(n):
        rotated = array1[-i:] + array1[:-i]
        
        distance = sum(abs(a-b) for a, b in zip(rotated, array2))
        if min_distance > distance:
            min_distance = distance
            best_array = rotated
            best_array_number = int("".join(map(str,rotated)))
        elif min_distance == distance:
            current_array_number = int("".join(map(str,rotated)))
            if current_array_number < best_array_number:
                best_array = rotated
            
    print(best_array, min_distance)
    return best_array, min_distance

array1, array2 = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
solution3(array1, array2)
# [3, 4, 5, 1, 2], 6