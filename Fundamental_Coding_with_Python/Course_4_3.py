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

    print("--------")
    print("return moves: ", moves)
    return moves

numbers = [2, 3, 3, 4, 2, 4] 
obstacle = 4

solution(numbers, obstacle)
# 5

