# Reference
# https://codesignal.com/learn/course/92/unit/2

def parse_and_multiply_numbers(input_string):
    num = ""
    numbers = []

    for char in input_string:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""
    if num:
        numbers.append(int(num))
    result = 1
    print(numbers)
    for number in numbers:
        result *= number
    return result

# print(parse_and_multiply_numbers('13k4k'))


# Quiz 1
# https://codesignal.com/learn/course/92/unit/2/practice/1

def solution1(s):
    # TODO: Implement the function that could solve the task
    s = s.split("-")
    result = []
    for c in s:
        if c.isnumeric():
            digit = ord("a") + int(c) - 1
            ch = chr(digit)
            result.append(ch)
        elif c.isalpha():
            num = ord(c) - ord("a") + 1
            result.append(str(num))
   
    result = "-".join(result)
    print(result)
    return result

s = "13-9-14-15"
solution1(s)


# Quiz 2
# https://codesignal.com/learn/course/92/unit/2/practice/2
def solution2(s):
    # TODO: implement
    num = ""
    numbers = []
    for c in s:
        if c.isnumeric():
            num += c
        elif not c.isnumeric() and num !="":
            numbers.append(int(num))
            num = ""
    if num != "":
        numbers.append(int(num))
    print(sum(numbers))
    return sum(numbers)

s = "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"
solution2(s)


# Quiz 3
# https://codesignal.com/learn/course/92/unit/2/practice/3

def solution3(input_string):
    # TODO: implement your solution here
    result = ""
    temp = ""
    for ch in input_string:     
        if ch.isnumeric():
            temp += str(ch)
        elif temp != "" and ch.isalpha():
            result += ch + temp
            temp = ""
        else:
            if ch == " " and temp != "":
                continue
            else:
                result += ch
    if temp != "":
        result += temp
    print(result)
    return result

input_string = "I have 2 apples and 5! oranges and 3 grapefruits."
solution3(input_string)