
def solution(A):
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2*left_sum), m)
    return m


# def solution(A): # solution starting from middle point
#     p = int((len(A)-1)/2)
#     s = sum(A)
#
#     sum_l = lambda A, p = sum(A[:p])
#
#     ans = abs(s - 2*sum_l)
#     ans_lo = abs(s - 2*sum_l+2*A[p-1])
#     ans_hi = abs(s - 2*sum_l-2*A[p])
#
#     def switch():
#         global ans, p, ans_lo, ans_hi
#         if ans == min([ans, ans_lo, ans_hi]):
#             return ans
#         elif ans_lo == min([ans, ans_lo, ans_hi]):
#             ans = ans_lo
#             p = p - 1
#
#         elif ans_hi == min([ans, ans_lo, ans_hi]):
#             ans = ans_hi
#             p = p + 1
#
#     while True: # usar iteração dentro de A[1:] pra não estourar a régua
#         switch()
#         ans_lo = abs((sum_r + A[p - 1]) - (sum_l - A[p - 1]))
#         ans_hi = abs((sum_r - A[p]) - (sum_l + A[p]))


if __name__ == '__main__':
    # A = [-1000, 1000]
    # assert solution(A) == 2000

    B = [3, 1, 2, 4, 3]
    print(solution(B))