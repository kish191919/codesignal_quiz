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