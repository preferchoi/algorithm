<<<<<<< HEAD
from itertools import permutations


def find():
    minV = 100
    for p in permutations(range(N)):  # 순열 생성
        s = 0
        for i in range(N):
            s += m[i][p[i]]  # 순열을 이용해 합 구하기
        if minV > s:
            minV = s;
    return minV


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for x in range(N)]  # 중첩리스트에 숫자 저장
    print('#{} {}'.format(tc, find()))
=======
# def re_1(s):
#     return s[::-1]
#
#
# def re_2(s):
#     q = ''
#     for i in s:
#         q = i + q
#     return q
#
#
# def re_3(s):
#     s = list(s)
#     for i in range(len(s) // 2):
#         s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
#     return ''.join(s)
#
#
# s = 'qwerty'
# print(re_1(s))
# print(re_2(s))
# print(re_3(s))
#
# s1, s2, s3 = 'asd', 'asd', 'fgh'
# s4, s5 = s1, s1[:2] + 'd'
# print(s1 == s2, s1 is s2)
# print(s1 == s3, s1 is s3)
# print(s1 == s4, s1 is s4)
# print(s1 == s5, s1 is s5)
#
#
# def my_strcmp(s1, s2):
#     s1, s2 = list(s1), list(s2)
#
#     if len(s1) < len(s2):
#         len_s = len(s1)
#     elif len(s1) >= len(s2):
#         len_s = len(s2)
#
#     for i in range(len_s):
#         if s1[i] != s2[i]:
#             if s1[i] > s2[i]:
#                 return 1
#             else:
#                 return -1
#     return 0
#
#
# print(my_strcmp('a', 's'))
#
#
# def itoa(n):
#     s = ''
#     while n != 0:
#         t = n % 10
#         s = chr(t + 48) + s
#         n = n // 10
#
#     return s
#
#
# def aaa(n):
#     return str(n)
#
#
# print(ord('s'), chr(100))
# print(itoa(10))
# print(aaa(10))
#
#
# '''
# 문자열을 정렬하는데 중복을 제거하면서 정렬
# dddbbbaaaccc -> abcd
# O(n) 안에
#
# a = 97
# '''
#
# s = 'dddbbbaaaccca'
#
# a = [0 for i in range(26)]
#
# for i in s:
#     a[ord(i) - 97] = 1
#
# res = ''
# for i in range(len(a)):
#     res += chr(97+i)*a[i]
# print(res)
#
#
# def find(t, p):
#     n = -1
#     for i in range(N - M):
#         for j in range(M):
#             if t[i + j] != p[j]:
#                 break
#             if j == M-1:
#                 return i
#
#     return n
#
# t = 'a pattern matching algorithm test'
# p = 'rithm'
# N = len(t)
# M = len(p)
# print(find(t, p))
#
#
s = '1 2 3'
s1, s2, s3 = map(int, s.split())
print(s1, s2, s3)
>>>>>>> 531f4484279cb70f8b12d16cdd7a020e4f1856c9
