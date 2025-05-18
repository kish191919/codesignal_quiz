
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

input = "CapitaL letters"
def solution3(input_str):
    # TODO: implement the string transformation function
    # input : "CapitaL letters"
    # output : "ovggvih XzkrgzO"
    input_str = input_str.split(" ")
    reordered = [input_str[-1]] + input_str[:-1]
    result = []
    for word in reordered:
        temp_word = ""
        for ch in word:
            if ch.islower():
                remain = 26 - (ord(ch) - ord("a"))
                remain_ch = chr(remain + ord("a")-1)
                temp_word += remain_ch
            elif ch.isupper():
                remain = 26 - (ord(ch) - ord("A"))
                remain_ch = chr(remain + ord("A")-1)
                temp_word += remain_ch
        result.append(temp_word)

    result = " ".join(result)
    print(result)
    return result

solution3(input)


# Quiz 4
# https://codesignal.com/learn/course/92/unit/1/practice/3

input = "SoME rAndoM _TeXT"

def solution4(input_str):
    # TODO: implement the function
    # input : "SoME rAndoM _TeXT"
    # output : "Some Random _text"
    input_str = input_str.split(" ")
    result = []
    for word in input_str:
        temp = ""
        for i in range(len(word)):
            if i == 0 and word[i].isalpha():
                ch = word[i].upper()
                temp += ch
            elif word[i].isalpha():
                temp += word[i].lower()
            else:
                temp += word[i]
        result.append(temp)
    result = " ".join(result)
    print(result)
    return result

solution4(input)