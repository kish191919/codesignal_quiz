# https://medium.com/@johnadjanohoun/metas-most-asked-coding-interview-questions-the-complete-list-of-73-leetcode-problems-47e96767adc7#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhYTY0ZWZjMTNlZjIzNmJlOTIxZjkyMmUzYTY3Y2M5OTQxNWRiOWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDYwMjQ3NDY2NjI1MDY3ODU3NzgiLCJlbWFpbCI6Imtpc2gxOTE5QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3NDg0NTQ4NzAsIm5hbWUiOiLquLDshLHtmZgiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSWRQVXVsVjlmS1lGODIwdThDZkJ0TGJoWjBJbi1DZElvRzUxMkNxZ2RZT1JSY0xBPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IuyEse2ZmCIsImZhbWlseV9uYW1lIjoi6riwIiwiaWF0IjoxNzQ4NDU1MTcwLCJleHAiOjE3NDg0NTg3NzAsImp0aSI6IjE0NmE4ZGFjMGFmOGFkZGRmMTNjMWFiODVlZDE4ZTY4MjViNDZlYjYifQ.paCNTAZo9NxjAKKvE22RFVhi-C8YvQIqQyFeXTZa9--BpPMKzPD3UTQZL3cugDu5uOaq5gcNxklAxnMDTZUCFdBmT-sRvecsmE-HO57xDPJOZYB6G1Jll9Iu0SkxQW_ZUhRIe4sdVMFj42JbQrR5m6ud5viU0EJOpcVTjwCkbDX2oc3BmdFxe53JRQNPc48rrLEq5KtMewzPZzrdlVfc8vLjn-s9PImV1hPxH-SsQw6UcXjcHIkJxV8f7ZxQbW52qeVFBryKewz0oMmIxCfqXq4trXy_2Gi1sJYErrdBvcjpj5vuTVbd2inNM6Wvcf9wtUNzGkZOEsEQ4rpjk_Ak2g


# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/?envType=problem-list-v2&envId=nhuldf1t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # t에 있는 문자와 개수 세기
        target_count = Counter(t)
        required = len(target_count)  # t에 있는 고유 문자 개수
        formed = 0  # 윈도우 내에서 조건을 만족한 문자 개수

        window_count = {}  # 현재 윈도우 안의 문자 개수

        # 결과 저장용: (윈도우 길이, 왼쪽 인덱스, 오른쪽 인덱스)
        answer = (float("inf"), None, None)

        left = 0  # 왼쪽 포인터
        for right in range(len(s)):  # 오른쪽 포인터를 하나씩 이동
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # 필요한 문자를 정확히 맞게 채웠다면 formed 증가
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # 윈도우가 조건을 만족하면 왼쪽 포인터 이동해서 최소 길이 찾기
            while left <= right and formed == required:
                # 현재 윈도우가 더 짧으면 정답 갱신
                if right - left + 1 < answer[0]:
                    answer = (right - left + 1, left, right)

                # 왼쪽 문자 줄이기
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed -= 1  # 조건 불만족으로 감소
                left += 1

        # 정답 윈도우가 있으면 자르기
        if answer[0] == float("inf"):
            return ""
        return s[answer[1]:answer[2] + 1]
    



# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # 단어 목록
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                        "Seventeen", "Eighteen", "Nineteen"]

        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n // 10] + " " + helper(n % 10)
            else:
                return LESS_THAN_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + THOUSANDS[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()
    

# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # Step 1: 원래 노드를 전부 복사해서 매핑 저장
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: 복사된 노드에 next와 random 설정
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new.get(curr.next)
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]

# 143. Reorder List
# https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            print("curr: ", curr)
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        print("prev: ", prev)
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2



# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        left = 0
        n = len(s) 
        visited = set()

        for right in range(n):
            if s[right] in visited:
                while left < right and s[right] in visited:
                    visited.remove(s[left])
                    left += 1
            visited.add(s[right])
            print(visited)
            max_len = max(max_len, len(visited))
        print(max_len)
        return max_len

s = "abcbac"
lengthOfLongestSubstring(s)


# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=nhuldf1t


class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        # Remove the space
        s = s.strip()
        sign = '+'

        if s.startswith('-'):
            sign = '-'
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        # Remove characters
        for char in s:
            if char.isdigit():
                if char == 0 and result == "":
                    continue
                else:
                    result += char 
            else:
                break

        if result == '':
            return 0
        else:
            if sign == "-":
                result =  int(result) * -1
            else:
                result =  int(result)
        result = min(result, 2**31-1)
        result = max(result, -2**31)
        return result


class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove the space
        s = s.strip()
        sign = 1

        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        current = 0
        for idx in range(len(s)):
            if not s[idx].isdigit():
                break
            current = current * 10 + int(s[idx])

        current = sign * current

        current = min(current, 2**31-1)
        current = max(current, -2**31)
        return current


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


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 127654321
        left = len(nums) - 2
        right = len(nums) - 1

        while nums[left] >= nums[right] and left >= 0 and right >= 1:
            left -=1
            right -=1 
        
        if left >= 0:
            right = len(nums) - 1
            while nums[left] >= nums[right] and left >= 0 and right >=1:
                right -=1
            nums[left], nums[right] = nums[right], nums[left]
        
        nums[left+1:] = reversed(nums[left+1:])

        print(nums)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <2:
            return nums
        result = []

        for idx in range(len(nums)-2, -1, -1):
            i = idx
            
            if nums[idx] < nums[idx+1]:
                break
            print(idx)
            if idx == 0:
                return nums.reverse()
            
        j = len(nums) -1
        while nums[i] >= nums[j]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        nums[i+1:] = reversed(nums[i+1:])
        print(nums)
        return nums


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



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
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
    

# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2[:]
        nums1.sort()

# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans = ""
        s = s.strip()
        for char in s:
            if char.isalnum():
                ans += char.lower()
        return ans == ans[::-1]
    


def read(buf: List[str], n: int) -> int:
    buf4 = [''] * 4  # read4가 읽은 문자 저장할 임시 버퍼
    total_read = 0   # 총 읽은 문자 수

    while total_read < n:
        count = read4(buf4)  # 최대 4글자 읽기
        if count == 0:  # 파일 끝이면 중단
            break

        # buf4에서 읽은 문자들을 buf에 복사
        for i in range(min(count, n - total_read)):
            buf.append(buf4[i])
            total_read += 1

    return total_read


# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i !=j:
                    product *= nums[j]
            answer.append(product)
        return answer
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        left = 1

        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
    

# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 0

        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/description/







# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/?difficulty=EASY
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],c=0) -> Optional[ListNode]:

        sum_ = l1.val + l2.val + c
        m = sum_ // 10
        remain = sum_ % 10

        new_node = ListNode(remain)

        if (l1.next != None) or (l2.next != None) or m != 0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            
            new_node.next = self.addTwoNumbers(l1.next, l2.next, m)
        return new_node
    


# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_node = result = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                new_node.next = list1
                list1 = list1.next
            else:
                new_node.next = list2
                list2 = list2.next
            new_node = new_node.next

        if list1:
            new_node.next = list1
        else:
            new_node.next = list2
        
        return result.next
    
# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while k < zeros:
                if nums[left] == 0:
                    zeros -=1
                left +=1
            max_len = max(max_len, right-left + 1)
        return max_len
    


