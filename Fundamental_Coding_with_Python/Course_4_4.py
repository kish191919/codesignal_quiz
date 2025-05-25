# reference
# https://codesignal.com/learn/course/93/unit/4

def solution(num1, num2):
    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
    
    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = n1 + n2 + carry
        if total > 9:
             carry = 1
        else:
            carry = 0
        curr = total%10
        res.append(str(curr))
        i, j = i - 1, j - 1

    return ''.join(res[::-1])  # reverse the list and join into a single string

print(solution("456", "77"))
# "533"


# Quiz1
# https://codesignal.com/learn/course/93/unit/4/practice/1
def solution1(num1, num2):
    # TODO: implement the function
    if len(num1) > len(num2):
        return 1
    
    if len(num1) < len(num2):
        return -1
    
    for i, j in zip(num1, num2):
        if i > j:
            return 1
        if j > i :
            return -1
    
    return 0

print(solution1('12345', '1234'))
# 1

# Quiz 2
# https://codesignal.com/learn/course/93/unit/4/practice/2
def solution2(num1, num2):
    num2 = num2.rjust(len(num1), '0')
    
    i = len(num1) -1
    borrow = 0
    result = []
    
    while i>=0:
        d1 = int(num1[i])
        d2 = int(num2[i]) + borrow
        
        if d1 < d2:
            d1 += 10
            borrow =1
        else:
            borrow = 0
        
        diff = d1 - d2
        result.append(str(diff))
        i -= 1
    ans = "".join(result[::-1]).lstrip('0')
    return ans or '0'

print(solution2('398746', '199234'))
# '199512'


# Quiz 3
# https://codesignal.com/learn/course/93/unit/4/practice/3

def solution3(num1, num2):
    # TODO: Implement Function
    if num1 == "0" or num2 =="0":
        return "0"
        
    result = ["0"] * (len(num1) + len(num2))
    
    for i in range(len(num1) -1 , -1, -1):
        for j in range(len(num2) -1, -1, -1):
            n1 = int(num1[i])
            n2 = int(num2[j])
            mul = n1 * n2
            p1 = i + j 
            p2 = i + j + 1
            
            total = mul + int(result[p2])
            result[p2] = total%10
            result[p1] = int(result[p1]) + total//10

    ans = "".join(map(str, result)).lstrip("0")
    print(ans)
    return ans

solution3("123456789", "987654321")
# 121932631112635269