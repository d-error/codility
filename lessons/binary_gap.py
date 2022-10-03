# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    binary_N = bin(N)[2:] #O(log N)
    counter = 0
    answer = 0
    for digit in binary_N: #(O(N))
        if digit == '0':
            counter += 1
        if digit == '1':
            if counter > answer:
                answer = counter
            counter = 0

    return answer


if __name__ == "__main__":
    B = 561892
    assert solution(B) == 3

