# # 반복을 사용한 n!
# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# # 재귀를 사용한 n!
# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#     return n * factorial_recursive(n - 1)