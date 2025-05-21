# Reference
# https://codesignal.com/learn/course/93/unit/3

def solution(numbers, obstacle):
    position = 0
    moves = 0
    while position < len(numbers):
        if numbers[position] == obstacle:
            print(position)
            return position
        moves += 1
        position += numbers[position]
        
    print("return moves: ", moves)
    return moves

numbers = [2, 3, 3, 4, 2, 4] 
obstacle = 4

solution(numbers, obstacle)
# 5

# Quiz 1 (Need to solve again)
# https://codesignal.com/learn/course/93/unit/3/practice/1
def solution1(numbers):
    # TODO: implement the function according to the task description
    result = []
    
    for idx in range(len(numbers)):
        if numbers[idx] < 0:
            result.append(-1)
        else:
            found_obstacle = False
            for step in range(1, numbers[idx] + 1):
                if idx + step < len(numbers) and numbers[idx + step] < 0:
                    result.append(idx + step)
                    found_obstacle = True
                    break
            if not found_obstacle:
                result.append(numbers[idx])
    print(result)
    return result


numbers = [1, 2, 3, 2, -3, 5, 2, 7, -1, 4]
solution1(numbers)
# [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]

