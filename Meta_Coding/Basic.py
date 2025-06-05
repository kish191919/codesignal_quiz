
# str
# immutable, slicing
s = 'Hello World'
s.upper()
s.lower()
s.startswith('H')

s = '   Hello World  '
s.strip()
s.split(" ")
s.find('h')   # -1
# s.index('h')  # Error   => Find is better


# list
# 수정가능 (mutable), in order, duplicated

l = [1, 2, 3]
l.index(2)
# l = lst.index(4)   # Error

l.append(4)
print(l.index(4))

last = l.pop()
print(last)

l.remove(1)  # value is removed
print(l)

l = [1,2,3,4,4,4,5,6]
l.insert(0, 300)  # [300, 1, 2, 3, 4, 4, 4, 5, 6]

l.sort()          # [1, 2, 3, 4, 4, 4, 5, 6, 300]

l.reverse()       # [300, 6, 5, 4, 4, 4, 3, 2, 1]

l = reversed(l)   # <list_reverseiterator object at 0x101161db0>
print(list(l))    # [1, 2, 3, 4, 4, 4, 5, 6, 300]



# Tuple
# immutable, 순서형 데이터 구조, 중복가능

t = ('a', 'b', 'c')
print(t[0])  # a
print(t[2])  # c

# t[0] = 'd'   # Error

# 튜플에 데이터를 직접 추가할수 없음
# 우회 방법: 리스트로 변환해서 추가
t = list(t)
t.append("d")
t = tuple(t)
print(t)         # ('a', 'b', 'c', 'd')

# 다른 예시: 튜플 결합
t = t + ('e',)      # ('a', 'b', 'c', 'd', 'e')
print(t)

print(t.count('a'))   # 1
print(t.index('c'))   # 2

print(t)              # ('a', 'b', 'c', 'd', 'e')
print(t[::-1])        # ('e', 'd', 'c', 'b', 'a')
print(sorted(t))      # ['a', 'b', 'c', 'd', 'e']
print(reversed(t))  # <reversed object at 0x104c1e2c0>

print(tuple(reversed(t)))   # ('e', 'd', 'c', 'b', 'a')

t = t + ('a',)
print(t)

# Set
# 중복 불가, 순서 없음, mutuble

a = {1, 2, 3}






 

