# https://medium.com/@johnadjanohoun/metas-most-asked-coding-interview-questions-the-complete-list-of-73-leetcode-problems-47e96767adc7#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhYTY0ZWZjMTNlZjIzNmJlOTIxZjkyMmUzYTY3Y2M5OTQxNWRiOWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDYwMjQ3NDY2NjI1MDY3ODU3NzgiLCJlbWFpbCI6Imtpc2gxOTE5QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3NDg0NTQ4NzAsIm5hbWUiOiLquLDshLHtmZgiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSWRQVXVsVjlmS1lGODIwdThDZkJ0TGJoWjBJbi1DZElvRzUxMkNxZ2RZT1JSY0xBPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IuyEse2ZmCIsImZhbWlseV9uYW1lIjoi6riwIiwiaWF0IjoxNzQ4NDU1MTcwLCJleHAiOjE3NDg0NTg3NzAsImp0aSI6IjE0NmE4ZGFjMGFmOGFkZGRmMTNjMWFiODVlZDE4ZTY4MjViNDZlYjYifQ.paCNTAZo9NxjAKKvE22RFVhi-C8YvQIqQyFeXTZa9--BpPMKzPD3UTQZL3cugDu5uOaq5gcNxklAxnMDTZUCFdBmT-sRvecsmE-HO57xDPJOZYB6G1Jll9Iu0SkxQW_ZUhRIe4sdVMFj42JbQrR5m6ud5viU0EJOpcVTjwCkbDX2oc3BmdFxe53JRQNPc48rrLEq5KtMewzPZzrdlVfc8vLjn-s9PImV1hPxH-SsQw6UcXjcHIkJxV8f7ZxQbW52qeVFBryKewz0oMmIxCfqXq4trXy_2Gi1sJYErrdBvcjpj5vuTVbd2inNM6Wvcf9wtUNzGkZOEsEQ4rpjk_Ak2g


def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])
        max_len = max(max_len, right-left + 1)
    print(max_len)
    return max_len

s = "abcbac"
lengthOfLongestSubstring(s)


# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/


def romanToInt(self, s: str) -> int:

    symbol_map ={"I" :1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0

    for idx in range(len(s)-1):
        if symbol_map[s[idx]] >= symbol_map[s[idx+1]]:
            total +=symbol_map[s[idx]]
        else:
            total -=symbol_map[s[idx]]
    total += symbol_map[s[-1]]
    print(total)
    return total
    



# https://leetcode.com/problems/3sum/submissions/1647364811/
# Time Exceed

def threeSum(nums):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in result:
                    temp = sorted([nums[i], nums[j], nums[k]])
                    result.append(temp)
    print(result)
    return result
    

def threeSum(nums):

    nums.sort()
    result = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums)-1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0 :
                left += 1
            elif total > 0 :
                right -=1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] ==nums[left-1]:
                    left +=1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
    return result


# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1: 
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    print(nums)


#31. Next Permutation
# https://leetcode.com/problems/next-permutation/description/


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >=0:
        j = n-1

        while nums[i] >= nums[j]:
            j -= 1
    
        nums[i], nums[j] = nums[j], nums[i]

    nums[i+1:] = reversed(nums[i+1:])
    print(nums)


nums =[1,2,7,6,5,4,3,2,1]
nextPermutation(nums)


# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
def multiply(num1, num2):

    num1 = num1[::-1]
    num2 = num2[::-1]

    total = 0
    i_index = 0
    for a in num1:
        i = 10 ** i_index
        j_index = 0
        for b in num2:
            j = 10 ** j_index
            total += (int(a) * i) * (int(b) * j)
            j_index += 1
        i_index += 1
    return str(total)



def multiply(num1, num2):

    res = 0
    carry1 = 1

    for i in num1[::-1]:
        carry2 = 1
        for j in num2[::-1]:
            res += int(i) * int(j) * carry1 * carry2
            carry2 *= 10
        carry1 *= 10
    return str(res)


#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def groupAnagrams(strs):

    anagrams = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())


# Add Binary
# https://leetcode.com/problems/add-binary/submissions/1647431147/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)

        total = a + b
        return bin(total)[2:]
    


