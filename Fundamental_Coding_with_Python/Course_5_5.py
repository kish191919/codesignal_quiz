# Reference
# https://codesignal.com/learn/course/94/unit/5

def solution(balloons):
    n = len(balloons)

    step = 0
    while True:
        step +=1
        new_balloons = balloons.copy()
        for i in range(n):
            share = balloons[i] // 2
            new_balloons[i] -= share
            new_balloons[(i+1)%n] += share
        print(new_balloons, balloons)
        if new_balloons ==balloons:
            break

        balloons = new_balloons
    print(step)
    return step

balloons = [4, 6, 2]
solution(balloons)

# Step 0: [4, 6, 2]
# Step 1: [2, 8, 2]
# Step 2: [3, 4, 5]
# Step 3: [4, 2, 6]
# Step 4: [2, 5, 5]
# Step 5: [4, 2, 6]