# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # write your code in Python 3.6
    for i in range(K):
        A = A[-1:] + A[:-1]
    return A