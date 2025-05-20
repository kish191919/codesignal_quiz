# Reference
# https://codesignal.com/learn/course/93/unit/2

def solutiona(sentence):
    words = sentence.split(' ')
    result =''
    # we will proceed progressively
    for word in words:
        if len(word) % 2 ==0:
            for i in range(len(word)):
                if i % 2 == 1:
                    result += word[i]
    print(result)
    return result

def solutionb(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 0:  # check if the length of word is even
            for i in range(1, len(word), 2):  # loop over odd characters
                result += word[i]
    print(result)
    return result

sentence = "Python is a high-level programming language." 
solutiona(sentence)
solutionb(sentence)


# Quiz1
# https://codesignal.com/learn/course/93/unit/2/practice/1
def solution(sentence):
    # TODO: implement the solution here
    result = ''
    
    words = sentence.split(" ")
    
    for word in words:
        if len(word) % 2 == 1:
            for idx in range(0, len(word), 2):
                result += word[idx]
    print(result[::-1])
    return result[::-1]
                
sentence = "Coding tasks are fun and required"
solution(sentence)
# "danfeasst"

# Quiz 2
# https://codesignal.com/learn/course/93/unit/2/practice/2
def solution2(sentence):
    # TODO: implement the solution here
    result = ""
    words = sentence.split(" ")
    
    for word in words:
        if len(word) % 2 == 1:
            most_frequent_ch = {}
            most_frequent_ch[word[0]] = 1
            i = 1
            while i < len(word):
                if word[i] in most_frequent_ch:
                    most_frequent_ch[word[i]] +=1
                else:
                    most_frequent_ch[word[i]] = 1
                i += 1
            max_item = max(most_frequent_ch.items(), key=lambda x:x[1])
            if max_item[1] == 1:
                result += word[0]
            else:
                result += max_item[0]
    print(result.lower())
    return result.lower()


sentence = "Isn't it fascinating"
solution2(sentence)
# "ia"



from collections import defaultdict

def solution2a(sentence):
    # TODO: implement the solution here
    result = ""
    words = sentence.split(" ")
    
    for word in words:
        if len(word) % 2 == 1:
            most_frequent_ch = defaultdict(int)
            most_frequent_ch[word[0]] = 1
            i = 1
            while i < len(word):
                most_frequent_ch[word[i]] +=1
                i += 1
            max_item = max(most_frequent_ch.items(), key=lambda x:x[1])
            if max_item[1] == 1:
                result += word[0]
            else:
                result += max_item[0]
    print(result.lower())
    return result.lower()

sentence = "Isn't it fascinating"
solution2a(sentence)
# "ia"



def solution3(sentence, c):
    # TODO: implement
    words = sentence.split(' ')
    
    result = ''
    
    for word in words:
        if len(word) % 2 == 0:
            i = len(word) // 2
            
            while i < len(word):
                if ord(word[i]) < ord(c):
                    result += word[i]
                i += 1
    print(result)
    return result

sentence = "Python is a high-level programming language."
c = 'n'
solution3(sentence, c)
# "hleel"