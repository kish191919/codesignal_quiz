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

# Quiz 1
# https://codesignal.com/learn/course/94/unit/5/practice/1

def solution1(s):
    # TODO: implement the solution here
    s = list(s)
    ans = ""
  
    while 0 < len(s): 
        temp = []
        if len(s) % 2 == 1 and len(s) != 1:
            for i in range(0, len(s)-1, 2): 
                temp.append((s[i],s[i+1]))
            result = []
            for a, b in temp:
                if a == b:
                    result.append(a)
                    ans += b
                else:
                    c = max(ord(a), ord(b))
                    result.append(chr(c))
                    ans += chr(min(ord(a), ord(b)))
            result.append(s[-1])
            print(result)
            s = result

        elif len(s) % 2 == 0:
            for i in range(0, len(s)-1, 2): 
                temp.append((s[i],s[i+1]))
            result = []
            for a, b in temp:
                if a == b:
                    result.append(a)
                    ans += b
                else:
                    c = max(ord(a), ord(b))
                    result.append(chr(c))
                    ans += chr(min(ord(a), ord(b)))
            print(result)
            s = result
        elif len(s) == 1:
            result = []
            ans += s[0]
            result.append(s[0])
            s = []

    print(list(ans))
    return list(ans)

s='BCAAB'
solution1(s)
#  ['B', 'A', 'A', 'B', 'C']



def solution1A(s):
    removed = []
    while s:
        new_s = ''
        i = 0
        while i < len(s) - 1:
            a, b = s[i], s[i + 1]
            if a <= b:
                removed.append(a)
                new_s += b
            else:
                removed.append(b)
                new_s += a
            i += 2
        if i == len(s) - 1:
            # 문자열 길이가 홀수일 경우 마지막 문자 남음
            new_s += s[-1]
        if len(new_s) == 1:
            # 마지막 남은 문자도 제거
            removed.append(new_s[0])
            break
        s = new_s
    print(removed)
    return removed

s='BCAAB'
solution1A(s)
#  ['B', 'A', 'A', 'B', 'C']