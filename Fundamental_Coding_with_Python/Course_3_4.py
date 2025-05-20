# Reference

def solution(orig_strs, substrs):
    result_arr = []

    for original, substring in zip (orig_strs,substrs):
        start_pos = original.find(substring)
        match_indices = []

        while start_pos != -1:
            match_indices.append(str(start_pos))
            start_pos = original.find(substring, start_pos + 1)
        result_arr.append(f"The substring '{substring}' was found in the original string '{original}' at position(s) {', '.join(match_indices)}.")
    print(result_arr)
    return result_arr


orig_strs= ["HelloWorld",'LearningPython']
substrs = ["loW",'ear']
solution(orig_strs, substrs)


# Quiz 1
# https://codesignal.com/learn/course/92/unit/4/practice/1

def replace_substring1(text, old, new):
    # TODO: Implement the function
    print(text.replace(old, new))
    return text.replace(old, new)


def replace_substring2(text, old, new):
    # TODO: Implement the function
    
    result = []
    i = 0
    len_old = len(old)
    
    while i < len(text):
        if text[i: i + len_old] == old:
            result.append(new)
            i += len_old
        else:
            result.append(text[i])
            i +=1
    print("".join(result))
    return "".join(result)

replace_substring1("it is a beautiful day", "beautiful", "gloomy") # "it is a gloomy day"
replace_substring2("it is a beautiful day", "beautiful", "gloomy") # "it is a gloomy day"


# Quez 2
# https://codesignal.com/learn/course/92/unit/4/practice/2
def solution2(sentences, words):
    # TODO: implement the solution
    
    ans = []
    
    for original, word in zip(sentences, words):
        result=[]
        i = 0
        len_word = len(word)
        if word[0].isupper():
            reversed_word = word[-1].upper() + word[1:-1] + word[0].lower()
        else:
            reversed_word = word[::-1]
            
        while i < len(original):
            if original[i:i+len_word].upper() == word.upper():
                if original[i].isupper():
                    result.append(reversed_word.capitalize())
                else:
                    result.append(reversed_word)
                i += len_word
            else:
                result.append(original[i])
                i += 1
        ans.append("".join(result))
    print(ans)
    return ans

sentences = ['lower case sentence', 'upper case Sentence', 'another Sentence here', 'final Sentence yay']
words = ['sentence', 'sentence', 'sentence', 'sentence']
solution2(sentences, words)

#['lower case ecnetnes', 'upper case Ecnetnes', 'another Ecnetnes here', 'final Ecnetnes yay']
#['lower case ecnetnes', 'upper case Ecnetnes', 'another Ecnetnes here', 'final Ecnetnes yay']


def solution2_1(sentences, words):
    # TODO: implement the solution
    result = []

    for sentence, word in zip(sentences, words):
        reversed_word = word[::-1]

        i = 0
        new_sentence = ""

        while i < len(sentence):
            if sentence[i:i+len(word)].lower() == word:
                original_chunk = sentence[i:i+len(word)]
                # 첫 글자가 대문자라면 대문자 유지
                if original_chunk and original_chunk[0].isupper():
                    reversed_cap = reversed_word.capitalize()
                    new_sentence += reversed_cap
                else:
                    new_sentence += reversed_word
                i += len(word)
            else:
                new_sentence += sentence[i]
                i += 1

        result.append(new_sentence)
    print(result)
    return result

solution2_1(sentences, words)
#['lower case ecnetnes', 'upper case Ecnetnes', 'another Ecnetnes here', 'final Ecnetnes yay']



# Quez 3
# https://codesignal.com/learn/course/92/unit/4/practice/3
def spot_swaps(source: str, target: str) -> list:
    result = []
    source = list(source)
    target = list(target)
    
    i = 0
    while i < len(source)-1:
        if source[i] == target[i+1] and source[i+1] == target[i]:
            result.append((i, source[i], target[i]))
            i += 2
        else:
            i += 1     
    print(result)  
    return result

source = "firsttest"
target = "firtestst"
spot_swaps(source, target)
# []
