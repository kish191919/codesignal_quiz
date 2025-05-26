# Reference
#

def solutionA(st, arr):
    total = 0
    count = 0
    ans =""

    for s, a in zip(st, arr):
        a /= 2
        next_char = "a" if s == "z" else chr(ord(s)+1)
        ans += next_char
        count +=1
        total = total + a

        if total > 20:
            break

    print(ans[::-1], arr[count:])
    return(ans[::-1], arr[count:])

solutionA("books", [10, 20, 30, 50, 100])


def solutionB(inputString, numbers):
    result = ''
    sum_so_far = 0
    i = 0
    while i < len(inputString) and sum_so_far <= 20:
        result += 'a' if inputString[i] == 'z' else chr(ord(inputString[i]) + 1)
        half_number = round(numbers[i] / 2)
        sum_so_far += half_number
        i += 1
    return result[::-1], numbers[i:]

solutionB("books", [10, 20, 30, 50, 100])

# Quiz 1
# https://codesignal.com/learn/course/94/unit/3/practice/1
def solution1(strings, numbers):
    # TODO: implement the solution according to the task
    result = ''
    so_far_sum = 0
    i  = 0
    
    while so_far_sum <= 100 and i < len(numbers):
        if strings[i] in ['a', 'e', 'i', 'o', 'u']:
            break
        else:
            result += 'z' if strings[i] == 'a' else chr(ord(strings[i]) -1)
            so_far_sum += abs(numbers[i]) * 2
        i += 1
    
    print(result,numbers[i:])
    return(result,numbers[i:])

solution1('xyzabc', [10, 20, 30, 40, 50, 60])
# ('wxy', [40, 50, 60])


# Quiz 2
# https://codesignal.com/learn/course/94/unit/3/practice/2
def solution2(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # TODO: implement the solution based on the provided task description
    
    total = 0
    i = 0
    result = ""
    
    while i < len(inputString) and total < 100 and i < len(numbers):
        if inputString[i] in vowels:
            result += 'a' if inputString[i] == 'u' else vowels[vowels.find(inputString[i])+1]
        elif inputString[i] in consonants:
            result += 'b' if inputString[i] == 'z' else  consonants[consonants.find(inputString[i])+1]
        total += (numbers[i] * 3)
        i +=1
    print(result,numbers[i:])
    return(result,numbers[i:])


inputString = 'example'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solution2(inputString, numbers)
# ('iyenqmi', [8, 9, 10])

inputString = 'zero'
numbers = [0, 0, 0]
solution2(inputString, numbers)
# ('bis', [])


# Quiz 3
# https://codesignal.com/learn/course/94/unit/3/practice/3

def solution3(arr, text):
    # TODO: implement
    total = 0
    result = ''
    i = 0
    
    while i < len(text) and i < len(arr) and total < 30:
        
        total += abs(arr[i]-3)
        if total > 30:
            break
        if text[i].isalpha():
           result += 'a' if text[i]=='z' else chr(ord(text[i])+1)  
        else:
            result += text[i]
        i += 1
    return result, arr[i:]


arr = [5, 10, 15, 20, 25]
text = "hello world"
print(solution3(arr, text))

#("ifm", [20, 25])