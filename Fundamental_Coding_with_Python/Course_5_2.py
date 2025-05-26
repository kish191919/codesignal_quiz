# reference
# "banana", the output should be [294, 222, 99].

from collections import Counter
def solutionA(text_input):
    temp = Counter(text_input)

    result = []
    for ch, qty in temp.items():
        next_ch = 'a' if ch == 'z' else chr(ord(ch) + 1)
        next_ch = ord(next_ch)
        result.append(next_ch * qty)
    
    # result = sorted(result, reverse=True)
    result.sort(reverse=True)

    print(result)
    return result

solutionA("banana") 
# [294, 222, 99]

def solutionB(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    combined_values = []
    for letter, freq in frequency_dict.items():
        combined_values.append(ord(letter) * freq)
    combined_values.sort(reverse=True)
    print(combined_values)
    return combined_values


solutionB("banana")
# [294, 222, 99]


# Quiz 1
# https://codesignal.com/learn/course/94/unit/2/practice/1
from collections import defaultdict
def solution1(numbers):
    # TODO: implement the function according to problem statement
    
    result = []
    ans = []
    for n in numbers:
        if n % 10 == 0:
            n = 1
        else:
            n += 1
        result.append(n)
    result_dict = defaultdict(int)
    for num in result:
        if result_dict[num]:
            result_dict[num] += 1
        else:
            result_dict[num] = 1
    # result_dic = {}
    # for num in result:
    #     if num not in result_dic:
    #         result_dic[num] = 1
    #     else:
    #         result_dic[num] += 1
    for num, freq in result_dict.items():
        ans.append(num * freq)
    ans = sorted(ans)
    print(ans)
    return ans

numbers = [5, 10, 15, 10, 5, 15]
solution1(numbers)


# Quiz 2
# https://codesignal.com/learn/course/94/unit/2/practice/2

def solution2(s):
    # TODO: Replace 'pass' with your implementation
    temp = {}

    for ch in s:
        if ch == "a":
            temp["a"] = ord("x")
        elif ch =="b":
            temp["b"] = ord("y")
        elif ch == "c":
            temp["c"] = ord("z")
        else:
            temp[ch] = ord(ch) -3
    
    temp_qty = {}
    for ch in s:
        if ch not in temp_qty:
            temp_qty[ch] =1
        else:
            temp_qty[ch] +=1
    
    result = {}
    for ch, num in temp.items():
        freq = temp_qty[ch]
        total = num * freq
        result[ch] = total
    print(result)
    return result

solution2("abc")
# {'a': 120, 'b': 121, 'c': 122}


def solution2A(s):
    freq = Counter(s)
    print(freq)
    result = {}

    for char in sorted(freq):
        original_freq = freq[char]
        shifted_char = chr((ord(char) - ord("a")-3) % 26 + ord("a")) 
        shifted_ascii = ord(shifted_char)
        result[char] = shifted_ascii * freq[char]
    return result

solution2A("aabccc")
# {'a': 240, 'b': 121, 'c': 366}


from collections import Counter

def solution3(sentence):
    # TODO: Implement the solution following the task description
    result = []
    for char in sentence:
        if not char.isalnum():
            continue
        else:
            if char.isnumeric():
                prev_num = int(char) - 1 if int(char) != 0 else 9
                result.append(prev_num)
            elif char.islower():
                shfted_char = chr((ord(char) - ord("a") -1) % 26 + ord("a"))
                result.append(shfted_char)
            elif char.isupper():
                shfted_char = chr((ord(char) - ord("A") -1) % 26 + ord("A"))
                result.append(shfted_char)
    freq = Counter(result)
    ans = []
    print(freq)
    for ch, freq in freq.items():
        total = abs(ord(str(ch)) - freq)
        ans.append(total)
    ans.sort()
    print(ans)
    return ans


sentence = "Hello, 123!"
solution3(sentence)
# [47, 48, 49, 70, 99, 105, 109]


def solution3A(sentence):
    # TODO: Implement the solution following the task description
    transformed = []

    # 1단계: 각 문자 변환
    for char in sentence:
        if char.islower():  # 소문자 알파벳
            transformed_char = 'z' if char == 'a' else chr(ord(char) - 1)
        elif char.isupper():  # 대문자 알파벳
            transformed_char = 'Z' if char == 'A' else chr(ord(char) - 1)
        elif char.isdigit():  # 숫자
            transformed_char = '9' if char == '0' else str(int(char) - 1)
        else:  # 공백이나 기호는 그대로
            transformed_char = char
        transformed.append(transformed_char)
    filtered = [ c for c in transformed if c.isalnum()]
    freq = Counter(filtered)


    result = [ abs(ord(c) - count) for c, count in freq.items()]
    print(sorted(result))
    return sorted(result)

sentence = "Hello, 123!"
solution3A(sentence)
# [47, 48, 49, 70, 99, 105, 109]