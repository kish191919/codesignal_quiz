
# https://codesignal.com/learn/course/92/unit/1
# Quiz 1
input = "Hello neat pythonistas_123"
# this will print: 'olleH taen 321_satsinohtyp'

def solution1(input_str):

    input_list = input_str.split(" ")
    reversed_word = [ "".join(reversed(word)) for word in input_list ]
    result = " ".join(reversed_word)
    print(result)
    return result


solution1(input)


# Quiz 2
# https://codesignal.com/learn/course/92/unit/1/practice/1

input = "abc 123 def"

def solution2(s):
    # TODO: Implement the solution here
    # input : "abc 123 def"
    # output : "cab 312 fde"
    s_list = s.split(" ")
    result = []
    for word in s_list:
        temp = word[-1]+word[:-1]
        result.append(temp)

    result = " ".join(result)
    print(result)
    return result

solution2(input)


# Quiz 3
# https://codesignal.com/learn/course/92/unit/1/practice/2

